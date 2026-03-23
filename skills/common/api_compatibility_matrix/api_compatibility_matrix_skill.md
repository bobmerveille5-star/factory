# API Compatibility Matrix Skill

## Purpose
Générer et maintenir une matrice de compatibilité entre les APIs des 4 plateformes supportées (MT5, MT4, Pine, NinjaTrader), permettant d'identifier les équivalences et les différences.

## Trigger
Ce skill est invoqué pour comparer les fonctionnalités entre plateformes ou lors de la création d'un nouveau projet multi-plateforme.

## Inputs
- Liste des fonctionnalités à comparer (optionnel)
- Documentation des APIs (optionnel, peut utiliser les doc_guards)

## Outputs
- `API_COMPATIBILITY_MATRIX.md`: Matrice de compatibilité contenant:
  - Tableau comparatif par fonctionnalité
  - Équivalences fonctionnelles
  - Limitations par plateforme
  - Recommandations de fallback

## Process

### 1. Collecte des APIs par plateforme
Pour chaque plateforme:
- Indicateurs intégrés (RSI, MACD, SMA, EMA, etc.)
- Fonctions de données (prix, volume)
- Fonctions de dessin (plot, ligne, forme)
- Fonctions de stratégie

### 2. Analyse des équivalences
Mapper les fonctionnalités:
- MT5.iRSI ↔ MQL4.iRSI ↔ ta.rsi() ↔ NinjaTrader.RSI()
- MT5.CopyRates ↔ MQL4 iCustom ↔ security() ↔ BarsArray

### 3. Génération de la matrice
```markdown
# API Compatibility Matrix

## Indicateurs

| Fonctionnalité | MT5 | MT4 | Pine | NinjaTrader |
|----------------|-----|-----|------|-------------|
| RSI | iRSI | iRSI | ta.rsi() | RSI() |
| MACD | iMACD | iMACD | ta.macd() | MACD() |
| SMA | iMA | iMA | ta.sma() | SMA() |
| EMA | iMA(MODE_EMA) | iMA(MODE_EMA) | ta.ema() | EMA() |
| Bollinger | iBands | iBands | ta.bbands() | Bollinger() |
| ATR | iATR | iATR | ta.atr() | ATR() |
| Stochastic | iStochastic | iStochastic | ta.stoch() | Stochastic() |

## Fonctions de Données

| Fonctionnalité | MT5 | MT4 | Pine | NinjaTrader |
|----------------|-----|-----|------|-------------|
| Prix cloture | Close[i] | Close[i] | close | Close[0] |
| Prix haut | High[i] | High[i] | high | High[0] |
| Volume | Volume[i] | Volume[i] | volume | Volume[0] |
| Time | Time[i] | Time[i] | time | Time[0] |

## Limites par Plateforme

### MT5
- Buffers illimités
- Handles d'indicateurs
- Multi-devises

### MT4
- Max 8 buffers
- Pas de handles
- Limité 1 devise

### Pine
- 30k lignes max
- Limité par sécurité
- Pas de données futures

### NinjaTrader
- NT8/NT9 différences
- Patterns .NET
- Backtest rapide
```

## Validation
- Chaque fonctionnalité doit avoir une équivalence
- Les limitations doivent être documentées
- Les workarounds doivent être suggérés

## Example
```
Input: ["RSI", "MACD", "SMA"]
Output: Matrice complète avec équivalences pour chaque fonction
```