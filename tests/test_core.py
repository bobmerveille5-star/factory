"""Tests for Trading Indicator Factory."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from lib.core import detect_patterns, generate_rules, PATTERNS


def test_detect_rsi():
    """Test RSI detection."""
    assert 'rsi' in detect_patterns("RSI with alerts")
    assert 'rsi' in detect_patterns("Relative Strength Index")


def test_detect_macd():
    """Test MACD detection."""
    assert 'macd' in detect_patterns("MACD crossover")


def test_detect_multiple():
    """Test multiple patterns."""
    patterns = detect_patterns("RSI and MACD together")
    assert 'rsi' in patterns
    assert 'macd' in patterns


def test_detect_none():
    """Test no pattern detected."""
    assert detect_patterns("Random text") == []


def test_generate_rules():
    """Test rule generation."""
    rules = generate_rules("RSI with period 14")
    assert 'rsi' in rules['patterns']
    assert rules['confidence'] == 85


def test_generate_rules_empty():
    """Test rule generation with no pattern."""
    rules = generate_rules("Something else")
    assert rules['patterns'] == []
    assert rules['confidence'] == 30


def test_patterns_exist():
    """Test patterns are defined."""
    assert 'rsi' in PATTERNS
    assert 'macd' in PATTERNS
    assert PATTERNS['rsi'].name == 'RSI'


if __name__ == '__main__':
    import subprocess
    result = subprocess.run(['python3', '-m', 'pytest', __file__, '-v'], 
                          capture_output=True, text=True)
    print(result.stdout or result.stderr)