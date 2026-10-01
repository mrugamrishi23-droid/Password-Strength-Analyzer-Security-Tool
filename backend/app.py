from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path
import sqlite3
from datetime import datetime, timezone
from services.password_analyzer import analyze_password
from services.password_generator import generate_password

BASE = Path(__file__).resolve().parent.parent
DB_PATH = BASE / "analytics.db"
FRONTEND = BASE / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND), static_url_path="")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = db()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS analyses (
        analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER NOT NULL,
        classification TEXT NOT NULL,
        password_length INTEGER NOT NULL,
        unique_character_ratio REAL NOT NULL,
        weakness_count INTEGER NOT NULL,
        created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS findings (
        finding_id INTEGER PRIMARY KEY AUTOINCREMENT,
        analysis_id INTEGER NOT NULL,
        finding_type TEXT NOT NULL,
        severity TEXT NOT NULL,
        description TEXT NOT NULL,
        FOREIGN KEY (analysis_id) REFERENCES analyses(analysis_id)
    );
    """)
    conn.commit()
    conn.close()


def record_safe_metadata(result):
    conn = db()
    cur = conn.execute("INSERT INTO analyses(score, classification, password_length, unique_character_ratio, weakness_count, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                       (result["score"], result["classification"], result["metrics"]["length"], result["metrics"]["unique_character_ratio"], len(result["findings"]), datetime.now(timezone.utc).isoformat()))
    analysis_id = cur.lastrowid
    conn.executemany("INSERT INTO findings(analysis_id, finding_type, severity, description) VALUES (?, ?, ?, ?)",
                     [(analysis_id, f["type"], f["severity"], f["description"]) for f in result["findings"]])
    conn.commit(); conn.close()


@app.get("/")
def index():
    return send_from_directory(FRONTEND, "index.html")


@app.post("/api/analyze")
def analyze():
    data = request.get_json(silent=True) or {}
    password = data.get("password")
    context = data.get("context") or {}
    if not isinstance(password, str):
        return jsonify({"error": "Password field is required."}), 400
    # The password is only used during this request. It is never logged or persisted.
    try:
        result = analyze_password(password, context)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    record_safe_metadata(result)
    return jsonify(result)


@app.get("/api/dashboard/stats")
def dashboard_stats():
    conn = db()
    rows = conn.execute("SELECT classification, COUNT(*) count FROM analyses GROUP BY classification").fetchall()
    avg = conn.execute("SELECT COALESCE(AVG(score),0) avg_score, COUNT(*) total FROM analyses").fetchone()
    lengths = conn.execute("SELECT password_length, COUNT(*) count FROM analyses GROUP BY password_length ORDER BY password_length").fetchall()
    conn.close()
    distribution = {r["classification"]: r["count"] for r in rows}
    return jsonify({"total": avg["total"], "average_score": round(avg["avg_score"], 2), "distribution": distribution,
                    "length_distribution": [{"length":r["password_length"],"count":r["count"]} for r in lengths]})


@app.get("/api/analytics/weaknesses")
def weaknesses():
    conn = db()
    rows = conn.execute("SELECT finding_type, COUNT(*) count FROM findings GROUP BY finding_type ORDER BY count DESC").fetchall()
    conn.close()
    return jsonify({"weaknesses": [{"type": r["finding_type"], "count": r["count"]} for r in rows]})


@app.post("/api/generate-password")
def generate():
    data = request.get_json(silent=True) or {}
    try:
        length = int(data.get("length", 20))
        value = generate_password(length, bool(data.get("uppercase", True)), bool(data.get("lowercase", True)), bool(data.get("numbers", True)), bool(data.get("symbols", True)))
    except (ValueError, TypeError) as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"password": value, "note": "Generated transiently; it is not stored by this application."})


@app.get("/api/health")
def health():
    return jsonify({"status":"ok"})


init_db()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
