# Market Structure Skill

## Purpose
Analyser la structure du marché en identifiant les niveaux de support/résistance, les cassures (breaks of structure), et les changements de趋势 (CHoCH).

## Trigger
Ce skill est invoqué quand l'utilisateur veut analyser la structure du marché pour comprendre la tendance et les niveaux clés.

## Inputs
- Données de prix (OHLCV)
- Configuration (S/R levels, lookback)
- Mode (Structure, CHoCH, BOS)

## Outputs
- `MARKET_STRUCTURE_REPORT.md`: Rapport contenant:
  - Niveaux S/R identifiés
  - Cassures détectées
  - Changements de structure
  - Score de tendance

## Process

### 1. Identification S/R
- Trouver niveaux horizontaux
- Identifier trend lines
- Calculer force de chaque niveau
- Trier par importance

### 2. Break of Structure (BOS)
- Quand prix casse niveau S/R important
- Confirmer avec close au-delà
- Mesurer momentum

### 3. Change of Character (CHoCH)
- Quand structure change de direction
- Signal précoce de retournement
- Valider avec volume

### 4. Score de tendance
- **Strong Uptrend**: BOS récents vers le haut
- **Strong Downtrend**: BOS récents vers le bas
- **Ranging**: Pas de BOS clairs
- **Transitioning**: CHoCH en cours

## Output Example
```markdown
# Market Structure Report

## Supports et Résistances

### Résistances
| Niveau | Prix | Touches | Force |
|--------|------|---------|-------|
| R1 | 1.2500 | 5 | 90% |
| R2 | 1.2700 | 3 | 70% |

### Supports
| Niveau | Prix | Touches | Force |
|--------|------|---------|-------|
| S1 | 1.2000 | 4 | 85% |
| S2 | 1.1800 | 2 | 50% |

## Événements Structure

### BOS-001
- Type: BULLISH BREAKOUT
- Niveau: R1 (1.2500)
- Confirmation: Close > 1.2500
- Momentum: 85%

### CHoCH-001
- Type: BEARISH CHoCH
- Direction: Downtrend
- Bar: 1450

## Tendance
- Direction: UPTREND
- Score: 75%
- Confiance: HIGH
```

## Validation
- Chaque niveau doit avoir score de force
- BOS/CHoCH doivent être datés
- Tendance documentée avec confiance

## Example
```
Input: Prix EURUSD, analyser structure
Output: 3 résistances, 2 supports, 1 BOS haussier
```