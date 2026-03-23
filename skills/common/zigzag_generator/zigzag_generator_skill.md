# ZigZag Generator Skill

## Purpose
Générer des indicateurs ZigZag configurables avec paramètres ajustables (profondeur, deviation, backstep) pour identifier les swings et points pivots.

## Trigger
Ce skill est invoqué quand l'utilisateur veut un indicateur ZigZag personnalisé ou comme base pour d'autres analyses.

## Inputs
- Configuration ZigZag (depth, deviation, backstep)
- Source de prix (High/Low ou Custom)
- Options d'affichage

## Outputs
- `ZIGZAG_SPEC.md`: Spécification du ZigZag contenant:
  - Paramètres de configuration
  - Points pivots identifiés
  - Signaux de cassure
  - Code pour chaque plateforme

## Process

### 1. Paramètres ZigZag
- **Depth**: Profondeur minimum pour former un pivot
- **Deviation**: Écart minimum en % pour nuevo pivot
- **Backstep**: Barres minimum entre pivots
- **Source**: High/Low ou prix custom

### 2. Algorithme
Pour chaque barre:
- Vérifier si nouvelle formation de pivot
- Calculer highs/lows locaux
- Tracer lignes entre pivots
- Détecter cassures

### 3. Signaux additionnels
- **Breakout**: Cassure du dernier pivot
- **Retest**: Retour sur pivot cassé
- **Pivot Change**: Changement de direction

## Output Example
```markdown
# ZigZag Specification

## Paramètres
| Param | Défaut | Plage | Description |
|-------|--------|-------|-------------|
| Depth | 12 | 5-100 | Profondeur min |
| Deviation | 5 | 1-50 | Écart en % |
| Backstep | 3 | 1-10 | Barres min |

## Points Pivots
| Pivot | Bar | Prix | Type |
|-------|-----|------|------|
| P-001 | 1200 | 1.2450 | HIGH |
| P-002 | 1150 | 1.2200 | LOW |
| P-003 | 1100 | 1.2400 | HIGH |

## Signaux
- BREAKOUT: Cassure 1.2450 → target 1.2600
- RETEST: Retour sur 1.2450 attendu
```

## Validation
- Chaque paramètre doit avoir plage valide
- Performance acceptable (< 2ms/bar)
- Points cohérents avecprix

## Example
```
Input: Depth=12, Deviation=5, Backstep=3
Output: ZigZag avec points pivots identifiés
```