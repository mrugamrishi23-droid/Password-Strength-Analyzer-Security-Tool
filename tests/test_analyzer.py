import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from services.password_analyzer import analyze_password
from services.password_generator import generate_password


def test_common_password_is_weak():
    r = analyze_password("123456")
    assert r["classification"] == "VERY WEAK"
    assert r["metrics"]["is_common"]


def test_repetition_detected():
    r = analyze_password("aaaaaaaaaaaaaaaa")
    assert r["metrics"]["repetition"]["repeated_characters"]


def test_keyboard_pattern_detected():
    r = analyze_password("qwerty2026!")
    assert r["metrics"]["keyboard_patterns"]


def test_context_is_detected_but_not_returned_as_password():
    r = analyze_password("Rahul@123", {"first_name":"Rahul"})
    assert "first_name" in r["metrics"]["personal_info_overlap"]
    assert "password" not in r


def test_entropy_is_exposed_as_estimate():
    r = analyze_password("SyntheticDemo!123")
    assert r["metrics"]["entropy"]["estimated_bits"] > 0


def test_generator_uses_requested_length():
    assert len(generate_password(20)) == 20


def test_long_randomish_input_can_score_high():
    r = analyze_password("G7!mQ2#vL9@pX4$zT8&k")
    assert r["score"] >= 61
