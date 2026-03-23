# Dashboard Creator Skill

## Purpose
Créer un dashboard visuel combinant plusieurs indicateurs avec des panneaux configurables, des alertes centralisées, et une vue d'ensemble du marché.

## Trigger
Ce skill est invoqué quand l'utilisateur veut créer un dashboard complet avec plusieurs indicateurs et analyses.

## Inputs
- Liste des indicateurs à inclure
- Layout du dashboard
- Alerts à configurer
- Timeframes à afficher

## Outputs
- `DASHBOARD_SPEC.md`: Spécification du dashboard contenant:
  - Liste des indicateurs
  - Configuration des panneaux
  - Alertes centralisées
  - Code pour chaque plateforme

## Process

### 1. Définition des panneaux
Pour chaque panneau:
- Indicateur à afficher
- Position (top, bottom, left, right)
- Taille relative
- Timeframe

### 2. Indicateurs recommandés par type
**Dashboard Trend:**
- 200 EMA (filtre direction)
- RSI (momentum)
- ATR (volatilité)

**Dashboard Scalping:**
- 9 EMA, 21 EMA (crossovers)
- Stochastic (oversold/overbought)
- Volume

**Dashboard Swing:**
- MACD (direction)
- ADX (force trend)
- RSI (momentum)

### 3. Alerts centralisées
- Alerte quand ANY indicateur donne signal
- Notification groupée
- Priorisation des signaux

### 4. Implémentation par plateforme
**MT5:** Plusieurs indicateurs dans sub-windows
**Pine:**Plusieurs indicateurs avec overlay
**NinjaTrader:** Multi-panels

## Output Example
```markdown
# Dashboard Specification

## Layout
+------------------+------------------+
|    RSI Panel     |   MACD Panel     |
+------------------+------------------+
|              Main Chart              |
+------------------+------------------+
|          Volume Panel               |
+-------------------------------------+
|            Alerts Panel             |
+-------------------------------------+

## Indicateurs
| Panel | Indicateur | Timeframe |
|-------|------------|-----------|
| RSI | RSI(14) | H1 |
| MACD | MACD(12,26,9) | H1 |
| Main | EMA(200), EMA(50) | H1 |
| Volume | Volume | H1 |

## Alerts Configurées
- Alert: RSI crosses 30/70
- Alert: MACD crossover
- Alert: Price crosses EMA200
- Alert: Volume spike > 2x average
```

## Validation
- Chaque panneau doit avoir un objectif clair
- Alerts doivent êtreactionnables
- Performance doit être acceptable

## Example
```
Input: [RSI, MACD, EMA(200)]
Output: Dashboard avec 4 panneaux + alerts centralisées
```