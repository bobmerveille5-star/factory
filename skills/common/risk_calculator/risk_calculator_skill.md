# Risk Calculator Skill

## Purpose
Calculer la taille de position optimale, le risk/reward ratio, et les niveaux de stop-loss/take-profit basés sur le risque défini par l'utilisateur.

## Trigger
Ce skill est invoqué quand l'utilisateur veut calculer la taille de position et les niveaux de trading pour gérer son risque.

## Inputs
- Capital disponible
- Pourcentage de risque par trade
- Stop-loss desired
- Entry price planned

## Outputs
- `RISK_CALCULATION.md`: Rapport contenant:
  - Position size
  - Stop-loss et take-profit
  - Risk/Reward ratio
  - Risque en dollars

## Process

### 1. Calcul de la taille de position
```
Position Size = (Capital × Risk%) / (Entry - Stop Loss)
```
- En lots ou en unités
- Arrondir selon rules du broker
- Tenir compte du leverage

### 2. Niveaux de prix
- **Stop Loss**: Prix de sortie perte
- **Take Profit**: Prix de sortie profit (basé sur R/R)
- **Break Even**: Déplacer SL à BE après profit

### 3. Risk/Reward
- Calcul: (TP - Entry) / (Entry - SL)
- Recommandé: R/R ≥ 2:1

### 4. Metrics additionnelles
- Risk en dollars
- Risk en pourcents
- Reward potentiel
- Reward/Risk ratio

## Output Example
```markdown
# Risk Calculation

## Paramètres
| Param | Valeur |
|-------|--------|
| Capital | $10,000 |
| Risk % | 2% |
| Entry | 1.2450 |
| Stop Loss | 1.2400 |

## Résultat
| Métrique | Valeur |
|----------|--------|
| Position Size | 2 lots |
| Risk Amount | $200 |
| Take Profit | 1.2550 |
| R/R Ratio | 2:1 |
| Reward | $400 |

## Niveaux
- ENTRY: 1.2450
- STOP LOSS: 1.2400 (-50 pips)
- TAKE PROFIT: 1.2550 (+100 pips)
- BREAKEVEN: 1.2450

## Résumé Trade
- Risque: $200 (2%)
- Récompense: $400 (4%)
- Ratio R/R: 2:1
- Probability conseillée: > 50%
```

## Validation
- Calculations doivent être数学iquement corrects
- Position size ne doit pas dépasser capital
- R/R doit être réaliste

## Example
```
Input: $10,000, risk 2%, entry 1.2450, SL 1.2400
Output: Position 2 lots, TP 1.2550, R/R 2:1
```