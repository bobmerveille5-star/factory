# Correlator Skill

## Purpose
Calculer et afficher les corrélations entre plusieurs paires de devises, métaux ou indices, permettant d'identifier les opportunités de diversification et les signaux confirmer.

## Trigger
Ce skill est invoqué quand l'utilisateur veut analyser les corrélations entre actifs pour confirmer des trades ou gérer le risque.

## Inputs
- Liste des paires à correlationner
- Timeframe d'analyse
- Lookback period

## Outputs
- `CORRELATION_REPORT.md`: Rapport contenant:
  - Matrice de corrélation
  - Paires les plus corrélées
  - Signaux de divergence
  - Recommandations

## Process

### 1. Calcul des corrélations
- Pearson correlation coefficient
- Range: -1 (inversé) à +1 (parfait)
- > 0.7: forte corrélation positive
- < -0.7: forte corrélation négative

### 2. Types de corrélations
- **Contemporaine**: Corrélation actuelle
- **Lagged**: Corrélation avec délai (leading indicator)

### 3. Applications
- **Diversification**: Choisir actifs peu corrélés
- **Confirmation**: Confirmer signal avec actif corrélé
- **Spread Trading**: Paires inversement corrélées

## Output Example
```markdown
# Correlation Matrix - H4

## Paires analysées
EURUSD, GBPUSD, USDJPY, GOLD, US30

## Matrice de Corrélation
|       | EUR | GBP | JPY | GOLD | US30 |
|-------|-----|-----|-----|------|------|
| EUR   | 1.0 | 0.8 | -0.6| 0.7  | 0.3  |
| GBP   | 0.8 | 1.0 | -0.5| 0.6  | 0.4  |
| JPY   |-0.6 |-0.5 | 1.0 |-0.4  |-0.2  |
| GOLD  | 0.7 | 0.6 |-0.4 | 1.0  | 0.1  |
| US30  | 0.3 | 0.4 |-0.2 | 0.1  | 1.0  |

## Points clés
- EUR-GBP: Forte corrélation (0.8)
- EUR-GOLD: Corrélation modérée (0.7)
- EUR-JPY: Corrélation inverse (-0.6)

## Signaux
- EURUSD LONG + GBPUSD LONG = Position agrandie (corrélation)
- EURUSD LONG + USDJPY LONG = Hedging naturel (inverse)

## Recommandations
- Diversifier avec GOLD et US30
- Éviter positions opposées sur EUR-GBP
```

## Validation
- Corrélations doivent être mathematicalement correctes
- Interprétation doit être précise
- Recommandationsactionnables

## Example
```
Input: [EURUSD, GBPUSD, USDJPY, GOLD], H4, 100 barres
Output: Matrice corrélation + recommandations trading
```