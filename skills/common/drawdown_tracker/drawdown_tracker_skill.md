# Drawdown Tracker Skill

## Purpose
Suivre et analyser les drawdowns d'un compte de trading, calculant les métriques de risque (Max DD, Current DD, Recovery Time) et générant des alertes.

## Trigger
Ce skill est invoqué quand l'utilisateur veut suivre les performances de risque de son compte et éviter les drawdowns excessifs.

## Inputs
- Historique des trades ou equity curve
- Seuil d'alerte de drawdown
- Paramètres de calcul

## Outputs
- `DRAWDOWN_REPORT.md`: Rapport contenant:
  - Current drawdown
  - Maximum drawdown
  - Recovery time estimé
  - Alertes

## Process

### 1. Métriques calculées
- **Current DD**: (Peak - Current) / Peak
- **Max DD**: Plus grand drawdown historiquement
- **Drawdown Duration**: Temps pour revenir au peak
- **Recovery Factor**: Profit total / Max DD

### 2. Alertes
- Warning à X% de drawdown
- Critical à Y% de drawdown
- Recovery estimé

### 3. Statistiques
- Avg drawdown duration
- Avg recovery time
- Ratio profit/drawdown

## Output Example
```markdown
# Drawdown Report

## Métriques Actuelles
- Equity Peak: $10,000
- Equity Current: $9,200
- Current DD: 8.0%
- Status: WARNING

## Maximum Drawdown
- Max DD: 15.2%
- Date: 2024-02-15
- Recovery: EN COURS
- Recovery Time: 23 jours

## Historique DD
| Période | DD | Durée | Recovery |
|---------|-----|------|----------|
| Jan 2024 | 12% | 15j | 12j |
| Fev 2024 | 15% | 30j | 23j |

## Alertes
⚠️ WARNING: Drawdown à 8% (seuil: 5%)
🔴 CRITICAL: Max DD à 15% (seuil: 20%)

## Recommandations
- Réduire taille de position de 30%
- Arrêter si DD atteint 12%
- Attendre recovery avant nouvel ajout
```

## Validation
- Calculations doivent correspondre à la définition standard
- Alertes doivent être en temps réel
- Recovery time doit être réaliste

## Example
```
Input: Equity history, alert at 5%
Output: DD tracker avec alertes et recommandations
```