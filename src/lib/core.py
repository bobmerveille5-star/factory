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
    # Basics (7)
    'rsi': IndicatorPattern('RSI', {'period': 14, 'overbought': 70, 'oversold': 30}),
    'macd': IndicatorPattern('MACD', {'fast': 12, 'slow': 26, 'signal': 9}),
    'sma': IndicatorPattern('SMA', {'period': 20}),
    'ema': IndicatorPattern('EMA', {'period': 20}),
    'bollinger': IndicatorPattern('Bollinger', {'period': 20, 'std_dev': 2.0}),
    'atr': IndicatorPattern('ATR', {'period': 14}),
    'stochastic': IndicatorPattern('Stochastic', {'k': 14, 'd': 3}),
    
    # Advanced (10+)
    'vwap': IndicatorPattern('VWAP', {}),
    'adx': IndicatorPattern('ADX', {'period': 14}),
    'cci': IndicatorPattern('CCI', {'period': 20}),
    'williams_r': IndicatorPattern('Williams %R', {'period': 14}),
    'mfi': IndicatorPattern('MFI', {'period': 14}),
    'obv': IndicatorPattern('OBV', {}),
    'roc': IndicatorPattern('ROC', {'period': 12}),
    'envelopes': IndicatorPattern('Envelopes', {'period': 20, 'deviation': 0.1}),
    'donchian': IndicatorPattern('Donchian', {'period': 20}),
    'ichimoku': IndicatorPattern('Ichimoku', {'tenkan': 9, 'kijun': 26, 'senkou': 52}),
    'stddev': IndicatorPattern('StdDev', {'period': 20, 'std_dev': 2.0}),
    'trix': IndicatorPattern('TRIX', {'period': 15}),
    'ultimate': IndicatorPattern('Ultimate Oscillator', {'period1': 7, 'period2': 14, 'period3': 28}),
}


# Aliases for better detection
PATTERN_ALIASES = {
    'relative strength index': 'rsi',
    'moving average convergence': 'macd',
    'simple moving average': 'sma',
    'exponential moving average': 'ema',
    'bollinger bands': 'bollinger',
    'average true range': 'atr',
    'stoch': 'stochastic',
    'volume weighted average price': 'vwap',
    'average directional index': 'adx',
    'commodity channel index': 'cci',
    'williams r': 'williams_r',
    'money flow index': 'mfi',
    'on balance volume': 'obv',
    'rate of change': 'roc',
    'donchian channels': 'donchian',
}


def detect_patterns(description: str) -> List[str]:
    """Detect patterns in description."""
    found = []
    desc = description.lower()
    
    # Check aliases first
    for alias, key in PATTERN_ALIASES.items():
        if alias in desc:
            if key not in found:
                found.append(key)
    
    # Then check direct pattern names
    for key, pat in PATTERNS.items():
        if key in desc or pat.name.lower() in desc:
            if key not in found:
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