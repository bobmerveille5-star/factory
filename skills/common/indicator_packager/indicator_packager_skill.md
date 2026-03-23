# Indicator Packager Skill

## Purpose
Combiner plusieurs indicateurs dans un seul fichier package (Expert Advisor ou script) avec gestion centralisée des entrées/sorties et du money management.

## Trigger
Ce skill est invoqué quand l'utilisateur veut créer un package complet incluant indicateurs + logique de trading + gestion du risque.

## Inputs
- Liste des indicateurs à inclure
- Logique de signal (entry/exit)
- Gestion du risque (position sizing, SL/TP)
- Type de sortie (EA, Script, Robot)

## Outputs
- `PACKAGER_SPEC.md`: Spécification du package contenant:
  - Architecture du package
  - Liste des composants
  - Configuration centralisée
  - Code complet

## Process

### 1. Architecture du package
**Composants:**
- Indicateurs (buffers)
- Signaux (logique entry/exit)
- Risk Manager (SL, TP, position size)
- Trade Manager (execution)
- GUI (paramètres)

### 2. Logique de trading
- Entry: Quelles conditions buy/sell
- Exit: Exit partial, trailing stop, time-based
- Filters: Filtrer par session, spread, margin

### 3. Risk Management
- Position sizing (fixed, % account, Kelly)
- Stop Loss / Take Profit
- Max spread
- Max trades par jour

### 4. Implémentation EA
**MT5/MQL4:**
- Class pour chaque indicateur
- OnTick() pour signaux
- Trade execution avec CTrade

## Output Example
```markdown
# Indicator Package - Trend Finder EA

## Composants
1. EMA 200 (filter direction)
2. RSI 14 (entry timing)
3. MACD (confirmation)
4. Signal Generator
5. Risk Manager
6. Trade Manager

## Logique Entry
- BUY: EMA200 bullish + RSI < 30 + MACD cross up
- SELL: EMA200 bearish + RSI > 70 + MACD cross down

## Risk Settings
- Position Size: 2% per trade
- Stop Loss: 50 pips
- Take Profit: 100 pips (2:1 R:R)
- Max Trades: 3 per jour

## Paramètres GUI
- Use Filter (bool)
- RSI Period (int)
- SL Pips (int)
- Risk % (double)

## Structure Code
class TrendFinderEA {
  - IndicatorManager
  - SignalGenerator
  - RiskManager
  - TradeManager
  - OnTick()
}
```

## Validation
- Package doit être complet et fonctionnel
- Risk management doit être robuste
- Code doit être propre et documenté

## Example
```
Input: [EMA200, RSI, MACD], logique "crossover + filter"
Output: EA complet avec risk management intégré
```