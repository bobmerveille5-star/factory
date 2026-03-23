#!/usr/bin/env python3
"""
Order Block Engine - Core Logic (V2)
Détecte swings, BOS/CHoCH, Order Blocks
"""

from dataclasses import dataclass, field
from typing import List, Optional
import json


@dataclass
class OHLC:
    open: float
    high: float
    low: float
    close: float
    volume: float = 0


@dataclass
class Event:
    type: str
    bar: int
    price: float
    data: dict = field(default_factory=dict)


@dataclass
class OrderBlock:
    index: int
    direction: str
    top: float
    bottom: float
    created_at: int
    mitigated: bool = False


class OrderBlockEngine:
    def __init__(self, swing_length: int = 5, zone_expiry_bars: int = 30):
        self.swing_length = swing_length
        self.zone_expiry_bars = zone_expiry_bars
        self.bullish_obs: List[OrderBlock] = []
        self.bearish_obs: List[OrderBlock] = []
    
    def find_swing_points(self, bars: List[OHLC]) -> dict:
        """Trouver swing highs et lows."""
        highs = []
        lows = []
        
        for i in range(self.swing_length, len(bars) - self.swing_length):
            # Swing high: plus haut que les N barres autour
            window = bars[i - self.swing_length : i + self.swing_length + 1]
            if bars[i].high == max(b.high for b in window):
                highs.append((i, bars[i].high))
            
            # Swing low: plus bas que les N barres autour
            if bars[i].low == min(b.low for b in window):
                lows.append((i, bars[i].low))
        
        return {'highs': highs, 'lows': lows}
    
    def detect_bos(self, bars: List[OHLC], swings: dict) -> List[Event]:
        """Détecter BOS."""
        events = []
        highs = swings.get('highs', [])
        lows = swings.get('lows', [])
        
        # BOS haussier: besoin d'au moins un swing high
        if highs:
            last_high_idx, last_high = highs[-1]
            for i in range(last_high_idx + 1, len(bars)):
                if bars[i].close > last_high:
                    events.append(Event('bos_bull', i, last_high, {'swing_idx': last_high_idx}))
                    break
        
        # BOS baissier: besoin d'au moins un swing low
        if lows:
            last_low_idx, last_low = lows[-1]
            for i in range(last_low_idx + 1, len(bars)):
                if bars[i].close < last_low:
                    events.append(Event('bos_bear', i, last_low, {'swing_idx': last_low_idx}))
                    break
        
        return events
    
    def create_ob(self, bars: List[OHLC], bos: Event) -> Optional[OrderBlock]:
        """Créer Order Block après BOS."""
        if not bars:
            return None
            
        if bos.type == 'bos_bull':
            # OB haussier: dernière bougie baissière avant BOS
            for i in range(bos.bar - 1, max(0, bos.bar - 10), -1):
                if bars[i].close < bars[i].open:  # Bearish
                    return OrderBlock(i, 'bullish', bars[i].high, bars[i].low, bos.bar)
        
        elif bos.type == 'bos_bear':
            # OB baissier: dernière bougie haussière avant BOS
            for i in range(bos.bar - 1, max(0, bos.bar - 10), -1):
                if bars[i].close > bars[i].open:  # Bullish
                    return OrderBlock(i, 'bearish', bars[i].high, bars[i].low, bos.bar)
        
        return None
    
    def process(self, bars: List[OHLC]) -> dict:
        events = []
        
        # Trouver swings
        swings = self.find_swing_points(bars)
        
        # Détecter BOS
        bos_events = self.detect_bos(bars, swings)
        
        for bos in bos_events:
            events.append(bos)
            
            # Créer OB
            ob = self.create_ob(bars, bos)
            if ob:
                if ob.direction == 'bullish':
                    self.bullish_obs.append(ob)
                else:
                    self.bearish_obs.append(ob)
                
                events.append(Event('ob_created', bos.bar, ob.top, {
                    'direction': ob.direction, 'top': ob.top, 'bottom': ob.bottom
                }))
        
        return {
            'events': [{'type': e.type, 'bar': e.bar, 'price': e.price, 'data': e.data} for e in events],
            'swings': swings,
            'bullish_obs': [{'index': ob.index, 'top': ob.top, 'bottom': ob.bottom} for ob in self.bullish_obs],
            'bearish_obs': [{'index': ob.index, 'top': ob.top, 'bottom': ob.bottom} for ob in self.bearish_obs]
        }


# === TESTS ===

def test_bullish_bos():
    """Test: BOS haussier"""
    # données avec swing high à ~1.113 puis cassure à 1.120
    bars = [
        OHLC(1.100, 1.105, 1.098, 1.104),
        OHLC(1.104, 1.108, 1.103, 1.107),
        OHLC(1.107, 1.110, 1.106, 1.109),
        OHLC(1.109, 1.113, 1.108, 1.112),  # 3 - swing high
        OHLC(1.112, 1.114, 1.110, 1.111),
        OHLC(1.111, 1.112, 1.107, 1.108),
        OHLC(1.108, 1.109, 1.104, 1.105),
        OHLC(1.105, 1.106, 1.101, 1.102),
        OHLC(1.102, 1.103, 1.098, 1.099),
        OHLC(1.099, 1.100, 1.095, 1.096),
        OHLC(1.096, 1.097, 1.091, 1.092),
        OHLC(1.092, 1.093, 1.087, 1.088),
        OHLC(1.088, 1.089, 1.083, 1.084),
        OHLC(1.084, 1.085, 1.079, 1.080),
        OHLC(1.080, 1.120, 1.078, 1.119),  # 14 - BOS! > 1.113
    ]
    
    engine = OrderBlockEngine(swing_length=3, zone_expiry_bars=10)
    result = engine.process(bars)
    
    print("=== Test: Bullish BOS ===")
    print(f"Swings: {result['swings']}")
    print(f"Events: {result['events']}")
    
    bos_bull = [e for e in result['events'] if e['type'] == 'bos_bull']
    assert len(bos_bull) > 0, "Should detect bullish BOS"
    print("✓ BOS haussier détecté!")


def test_range():
    """Test: Range - pas de BOS"""
    bars = [
        OHLC(1.100, 1.105, 1.098, 1.104),
        OHLC(1.104, 1.107, 1.102, 1.106),
        OHLC(1.106, 1.109, 1.104, 1.108),
        OHLC(1.108, 1.111, 1.106, 1.110),
        OHLC(1.110, 1.113, 1.108, 1.112),
        OHLC(1.112, 1.115, 1.110, 1.114),
        OHLC(1.114, 1.117, 1.112, 1.116),
    ]
    
    engine = OrderBlockEngine(swing_length=2, zone_expiry_bars=10)
    result = engine.process(bars)
    
    print("\n=== Test: Range ===")
    print(f"Events: {result['events']}")
    
    bos_count = len([e for e in result['events'] if 'bos' in e['type']])
    assert bos_count == 0, "Should not detect BOS in range"
    print("✓ Pas de BOS en range")


if __name__ == "__main__":
    test_bullish_bos()
    test_range()
    print("\n=== All tests passed ===")