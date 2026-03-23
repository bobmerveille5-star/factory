# Divergence Detector Skill

## Purpose
Détecter automatiquement les divergences entre le prix et un indicateur (RSI, MACD, Stochastic, etc.), identifiant les signaux de retournement potentiels.

## Trigger
Ce skill est invoqué quand l'utilisateur veut détecter des divergences pour anticiper les retournements de tendance.

## Inputs
- Indicateur source (RSI, MACD, Stochastic, CCI, etc.)
- Données de prix (OHLC)
- Paramètres de détection (tolerance, lookback)

## Outputs
- `DIVERGENCE_REPORT.md`: Rapport de divergences contenant:
  - Divergences haussières détectées
  - Divergences baissières détectées
  - Fiabilité de chaque divergence
  - Signaux générés

## Process

### 1. Types de divergences
**Divergence haussière (Bullish):**
- Prix fait des lows plus bas
- Indicateur fait des lows plus hauts
- Signal: Achat potentiel

**Divergence baissière (Bearish):**
- Prix fait des highs plus hauts
- Indicateur fait des highs plus bas
- Signal: Vente potentielle

**Divergence cachée (Hidden):**
- Prix fait des highs plus bas (trend haussier)
- Indicateur fait des highs plus hauts

### 2. Algorithme de détection
Pour chaque pivot de prix:
- Identifier pivot haut/bas
- Calculer slope prix
- Calculer slope indicateur
- Comparer directions

### 3. Paramètres configurables
- Lookback: Nombre de barres pour chercher divergence
- Tolerance: Différence autorisée pour match
- Min Strength: Force minimum du signal

## Output Example
```markdown
# Divergence Report

## Divergences Haussières

### D-001: RSI Divergence
- Bar: 1450
- Type: REGULAR
- Prix: Low 1.1800 → 1.1750 (bas plus bas)
- RSI: Low 25 → 35 (bas plus haut)
- Force: 85%
- Signal: BUY

## Divergences Baissières

### D-002: MACD Divergence
- Bar: 1520
- Type: HIDDEN
- Prix: High 1.2500 → 1.2550
- MACD: High 100 → 80
- Force: 70%
- Signal: SELL

## Signaux Actifs
| Divergence | Type | Direction | Force |
|------------|------|-----------|-------|
| RSI D-001 | REGULAR | BUY | 85% |
| MACD D-002 | HIDDEN | SELL | 70% |
```

## Validation
- Chaque divergence doit avoir un score de force
- Faux positifs minimisés avec tolérance
- Code performant (< 5ms par détection)

## Example
```
Input: RSI + prix, chercher divergences
Output: 3 divergences détectées (2 haussières, 1 baissière)
```