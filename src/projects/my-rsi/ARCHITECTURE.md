# Architecture - my-rsi

## Schéma de données
Entrée: Prix OHLCV
Sortie: Valeurs indicateur

## Découpage par plateforme
- MT5: iRSI() avec handle
- MT4: iRSI() inline
- Pine: ta.rsi()
- NinjaTrader: RSI() class
