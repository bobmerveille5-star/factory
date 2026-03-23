"""
Trading Indicator Factory - Core Library
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class ProjectSpec:
    """Project specification."""
    name: str
    description: str = ""


@dataclass
class IndicatorPattern:
    """Indicator pattern definition."""
    name: str
    params: Dict


# === PATTERNS ===
PATTERNS = {
    'rsi': IndicatorPattern('RSI', {'period': 14, 'overbought': 70, 'oversold': 30}),
    'macd': IndicatorPattern('MACD', {'fast': 12, 'slow': 26, 'signal': 9}),
    'sma': IndicatorPattern('SMA', {'period': 20}),
    'ema': IndicatorPattern('EMA', {'period': 20}),
    'bollinger': IndicatorPattern('Bollinger', {'period': 20, 'std_dev': 2.0}),
    'atr': IndicatorPattern('ATR', {'period': 14}),
    'stochastic': IndicatorPattern('Stochastic', {'k': 14, 'd': 3}),
}


def detect_patterns(description: str) -> List[str]:
    """Detect patterns in description."""
    found = []
    desc = description.lower()
    for key, pat in PATTERNS.items():
        if key in desc or pat.name.lower() in desc:
            found.append(key)
    return found


def generate_rules(description: str) -> Dict:
    """Generate rules from description."""
    patterns = detect_patterns(description)
    return {
        'patterns': patterns,
        'confidence': 85 if patterns else 30,
        'params': [PATTERNS[p].params.copy() for p in patterns] if patterns else []
    }