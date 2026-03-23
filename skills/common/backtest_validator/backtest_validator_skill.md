# Backtest Validator Skill

## Purpose
Valider le comportement d'un indicateur de trading avec des données historiques réelles, vérifier la justesse des calculs, et générer un rapport de validation avec métriques.

## Trigger
Ce skill est invoqué après `code_optimizer` pour valider le code avec des données réelles.

## Inputs
- Code source de l'indicateur
- `RULES_SPEC.md`: Spécification technique
- `TEST_CASES.md`: Cas de test
- Données historiques (optionnel, peut utiliser données simulées)

## Outputs
- `BACKTEST_VALIDATION_REPORT.md`: Rapport de validation contenant:
  - Résultats des tests sur données réelles
  - Métriques de performance
  - Anomalies détectées
  - Score de validation

## Process

### 1. Préparation des données de test
Générer ou charger:
- Dataset de prix (OHLCV)
- Différentes conditions de marché (trend, range, volatile)
- Périodes diverses

### 2. Exécution des tests
Pour chaque TEST_CASE:
- Exécuter le code sur les données
- Capturer les valeurs de sortie
- Comparer avec les valeurs attendues
- Enregistrer les métriques

### 3. Analyse des résultats
- Calculer le taux de succès
- Identifier les échecs
- Mesurer les performances
- Détecter les anomalies

### 4. Métriques calculées
- **Précision**: % de tests réussis
- **Latence**: Temps moyen par calcul
- **Mémoire**: Utilisation mémoire
- **Stabilité**: Variance des résultats

### 5. Génération BACKTEST_VALIDATION_REPORT
```markdown
# Backtest Validation Report - [INDICATEUR]

## Résumé
- Statut: [PASS/FAIL]
- Score: 92/100
- Tests réussis: 45/50
- Temps d'exécution: 2.3s

## Tests fonctionnels
| Test | Résultat | Valeur attendue | Valeur obtenue |
|------|----------|-----------------|----------------|
| RSI period=14 | PASS | 65.2 | 65.2 |
| RSI period=7 | PASS | 58.1 | 58.1 |

## Métriques de performance
- Latence moyenne: 0.5ms/bar
- Mémoire: 128KB
- Stabilité: 100%

## Anomalies détectées
### A-001: [Description]
- Sévérité: [LOW/MEDIUM/HIGH]
- Recommandation: [correction]

## Conditions de marché testées
- Trend haussier: ✓
- Trend baissier: ✓
- Marché latéral: ✓
- Haute volatilité: ✓

## Recommandations
- [Recommandation 1]
```

## Validation
- Au moins 80% des tests doivent passer
- Les échecs doivent être documentés
- Les performances doivent être acceptables

## Example
```
Input: Code RSI + données EURUSD H1
Output:
- Tests: 50/50 exécutés
- Réussis: 48/50
- Échecs: 2 (border cases)
- Score: 94/100
- Latence: 0.3ms/bar
```