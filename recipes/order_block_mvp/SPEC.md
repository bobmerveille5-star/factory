# Order Block MVP - Specification

## Overview
Detect Order Blocks (OB) with BOS/CHoCH validation - MVP strict version.

## Inputs
swing_length: int = 5          # Nombre de barres pour swing
atr_period: int = 14            # ATR pour sizing
min_impulse_atr: float = 1.5   # Impulsion minimale en ATR
zone_expiry_bars: int = 30     # Expiration zone

## Detections

### Swing Detection
- swing_high: le plus haut des `swing_length` barres
- swing_low: le plus bas des `swing_length` barres

### BOS (Break of Structure) - Bullish
- condition: close[1] > swing_high[previous_swing]

### BOS - Bearish
- condition: close[1] < swing_low[previous_swing]

### CHoCH (Change of Character)
- condition: BOS dans direction opposée après trend

### Order Block
- Source: dernière bougie baissière avant BOS haussier
- Validation: body_size >= 0.5 * ATR

## State
- active_bullish_zones[]    # Zones non-mitigées
- active_bearish_zones[]   # Zones non-mitigées
- last_confirmed_bos        # Direction du dernier BOS
- last_swing_high          # Prix du dernier swing high
- last_swing_low           # Prix du dernier swing low

## Outputs
- draw_rectangle: zones actives
- draw_label: BOS/CHoCH
- alert: premier retest de zone

## Anti-bruit
- Zone invalidée si prix < zone_bottom (bullish) ou > zone_top (bearish)
- Zone expirée après `zone_expiry_bars` barres

## Cas limites
- Égalité highs/lows: prendre la barre la plus récente
- Historique insuffisant: attendre `swing_length` barres