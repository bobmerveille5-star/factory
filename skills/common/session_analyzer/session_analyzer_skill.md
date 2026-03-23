# Session Analyzer Skill

## Purpose
Analyser le comportement du marché par session de trading (Asia, London, New York) pour identifier les patterns et volatilité caractéristiques de chaque session.

## Trigger
Ce skill est invoqué quand l'utilisateur veut comprendre quel type de trading est optimal pour chaque session et adapter sa stratégie.

## Inputs
- Données de prix
- Sessions à analyser (Asia, London, NY)
- Lookback period

## Outputs
- `SESSION_ANALYSIS.md`: Rapport contenant:
  - Caractéristiques de chaque session
  - Volatilité par session
  - Directionnalité
  - Recommandations

## Process

### 1. Définition des sessions
- **Asia**: 00:00-09:00 UTC (Tokyo, Sydney, Singapore)
- **London**: 08:00-17:00 UTC (London, Europe)
- **New York**: 13:00-22:00 UTC (NY, US)

### 2. Métriques par session
- Range moyen (pips)
- Volatilité (ATR ou écart type)
- Direction (close - open)
- Volume relatif

### 3. Patterns typiques
- Asia: Range-bound, faible volatilité
- London: Haute volatilité, directional
- NY: Haute volatilité, range возможно

## Output Example
```markdown
# Session Analysis - EURUSD

## Asia Session (00:00-09:00 UTC)
- Avg Range: 25 pips
- Volatility: LOW
- Direction: MIXTE
- Caractéristiques: Range-bound, faible liquidité
- Tips: Éviter breakouts, trader ranges

## London Session (08:00-17:00 UTC)
- Avg Range: 65 pips
- Volatility: HIGH
- Direction: BULLISH
- Caractéristiques: Meilleure liquidité, mouvements amples
- Tips: Breakouts, trend following

## New York Session (13:00-22:00 UTC)
- Avg Range: 55 pips
- Volatility: HIGH
- Direction: MIXTE
- Caractéristiques: Overlap London-NY volatile
- Tips: News trading, reversals

## Recommandations
- Scalping: Asia ou NY overlap
- Swing: London
- News: NY uniquement
```

## Validation
- Sessions doivent correspondre aux heures UTC
- Volatilité doit être cohérente avec données
- Recommandations actionnables

## Example
```
Input: EURUSD 1 mois de données
Output: Analyse complète par session avec recommandations
```