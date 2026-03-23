# MT4 Indicator Codegen Skill

## Purpose
Générer du code MQL4 optimisé et conforme aux spécifications pour un indicateur de trading.

## Trigger
Ce skill doit être invoqué après `mt4_doc_guard_skill` et avant `mt4_review_skill`. Il utilise RULES_SPEC.md, ARCHITECTURE.md et MT4_DOCS_CHECKED.md pour produire le code source.

## Inputs
- `RULES_SPEC.md`: Spécification technique détaillée
- `ARCHITECTURE.md`: Architecture de l'indicateur
- `MT4_DOCS_CHECKED.md`: Validation des APIs MQL4
- `TEST_CASES.md`: Cas de test à valider

## Outputs
- Fichier source `...mq4` dans le dossier `projects/[nom]/mt4/src/`
- Code conforme aux standards MQL4
- Code compatible avec MT4 Build 600+

## Process

### 1. Préparation de l'environnement
- Créer la structure de fichier standard MQL4
- Définir les includes nécessaires (indicators.mq4)
- Configurer les propriétés du programme

### 2. Différences MQL4 vs MQL5 à gérer
- Pas de classes CTrade, utiliser OrderSend()
- Pas de ArraySetAsSeries, order manuel
- IndicatorCounted() fonctionne différemment
- Limites sur le nombre de buffers (max 8)

### 3. Définition des paramètres
Pour chaque paramètre de RULES_SPEC:
- Créer les variables `input`
- Types primitifs uniquement (MQL4 n'a pas de types avancés)
- Valeurs par défaut compatibles MQL4

### 4. Implémentation des buffers
- Créer les buffers avec `IndicatorBuffers()`
- Limite: maximum 8 buffers
- Configurer les styles de plot

### 5. Implémentation de init()
- Initialiser les indicateurs avec les fonctions iMA, iRSI
- Pas de handle d'indicateur (MQL4 n'a pas d'handle)
- Calcul direct des valeurs

### 6. Implémentation de start()
- Utiliser IndicatorCounted() pour optimiser
- Accéder aux prix avec iOpen, iHigh, iLow, iClose
- Calcul sur les barres manquantes

### 7. Standards de codage MQL4
- Conventions: `extern` pour paramètres, `double` pour prix
- Commentaires pour chaque fonction
- Gestion manuelle des arrays
- Compatibilité MT4 Build 600+ (classes partielle)

## Validation
- Le code compile sans erreur dans MetaEditor
- Toutes les fonctions INVALID de MT4_DOCS_CHECKED évitées
- Code respecte les limites MQL4 (8 buffers, etc.)
- Compatible MT4 Build 600+

## Example
```
Input: RULES_SPEC swingPeriod=14
Output: SwingHighLow.mq4:
- extern int SwingPeriod = 14;
- #property indicator_buffers 2
- double swingHighBuffer[];
- int init(): IndicatorBuffers(2), SetIndexBuffer(0, swingHighBuffer)
- int start(): calculate swing highs using iHigh
```