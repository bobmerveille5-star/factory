# Test Design Skill

## Purpose
Concevoir une suite de tests exhaustive qui valide le comportement correct d'un indicateur de trading sur chaque plateforme.

## Trigger
Ce skill doit être invoqué après `rules_formalizer_skill` et avant `architecture_skill`. Il produit le TEST_CASES.md qui guide la génération et la validation du code.

## Inputs
- `RULES_SPEC.md`: Spécification technique détaillée
- `PRODUCT_SPEC.md`: Spécification fonctionnelle

## Outputs
- `TEST_CASES.md`: Documentation des cas de test contenant:
  - Cas nominaux (fonctionnement normal)
  - Cas limites (border cases)
  - Cas d'erreur (entrées invalides)
  - Cas de performance (données volumineuses)
  - Critères d'acceptation pour chaque test

## Process

### 1. Identification des axes de test
Pour chaque composant de l'indicateur:
- Axe mathématique: Les calculs sont-ils justes?
- Axe visuel: L'affichage correspond-il aux spécifications?
- Axe comportemental: Les signaux sont-ils générés correctement?
- Axe performance: Les calculs sont-ils assez rapides?

### 2. Conception des cas nominaux
Pour chaque fonctionnalité:
- Test avec données standards (prixnormaux)
- Test avec paramètres par défaut
- Test avec variations de paramètres
- Test multi-timeframe

### 3. Conception des cas limites
Identifier et tester:
- Premières barres (données insuffisantes)
- Données manquantes (gaps dans les prix)
- Valeurs extrêmes (prix très hauts/très bas)
- Périodes minimales/maximales
- Changement de session/jour

### 4. Conception des cas d'erreur
Tester le comportement avec:
- Paramètres hors plage
- Données d'entrée invalides
- Division par zéro
- Overflows numériques
- Conditions de course (race conditions)

### 5. Conception des cas de performance
Tester avec:
- Grand nombre de barres (10k+)
- Multiples instances
- Changement de paramètre en temps réel
- Contexte backtest vs live

### 6. Définition des critères d'acceptation
Pour chaque test:
- Condition de succès explicite
- Marge de tolérance (pour les tests numériques)
- Mode de validation (automatique ou manuel)

### 7. Génération TEST_CASES.md
Structurer selon le template:
```
# Cas de test - [INDICATEUR]

## Tests fonctionnels
### TF-001: [Nom du test]
- Description: [Ce qui est testé]
- Données: [Dataset utilisé]
- Attendu: [Résultat attendu]
- Critère: [Comment valider]

### TF-002: ...

## Tests limites
### TL-001: [Nom du test]
- Description: ...
- Données: ...
- Attendu: ...
- Critère: ...

## Tests d'erreur
### TE-001: ...

## Tests de performance
### TP-001: ...

## Matrice de couverture
| Test | Règle couverte | Critère |
|------|----------------|---------|
| TF-001 | Règle 1 | Automatique |
```

## Validation
- Chaque règle dans RULES_SPEC doit avoir au moins un test
- Chaque border case identifié doit être testé
- Les critères doivent être mesurables

## Example
```
Input: RULES_SPEC pour swing highs avec swingPeriod=14
Output: TEST_CASES avec:
- TF-001: swingPeriod=14 sur données normales → pics détectés
- TL-001: swingPeriod > barres disponibles → comportement handle
- TL-002: Données constantes → pas de swing
- TE-001: swingPeriod ≤ 0 → erreur paramètre
- TP-001: 10000 barres → temps < 100ms
```