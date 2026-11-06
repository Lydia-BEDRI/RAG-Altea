# Réponses aux questions du TP

## Exercice 1 - Étape 1 : collecte

### Q1

Le script suit le squelette du TP. `lire_pdf` utilise `PdfReader` pour extraire le texte de chaque page et enregistrer sa source et son numéro de page. `lire_txt` lit un fichier UTF-8 et le représente comme une page. `collecter` parcourt `docs/`, choisit la fonction selon l’extension et ajoute le service à chaque page.

### Q2

On conserve le nom du fichier et le numéro de page pour citer précisément la source dans une réponse et permettre au salarié de retrouver le passage. Le service permet de filtrer les résultats, par exemple pour chercher uniquement dans les documents RH, et de vérifier que la réponse vient du bon service.

## Exercice 1 - Étape 2 : nettoyage

### Q3

`nettoyer_pages` applique `nettoyer` au texte de chaque page et écarte celles dont le texte devient vide. Sur le corpus, 23 pages/documents sont conservés sur 23 ; aucune page n’est devenue vide.

### Q4

La page 1 de `livret_accueil.pdf` est affichée avant et après nettoyage. Elle ne contient pas d’espaces répétés à corriger ; la différence visible avec `repr` est le retour à la ligne final, supprimé par `strip`. L’en-tête de diffusion restreinte et le numéro de page restent présents. Une règle supplémentaire pourrait supprimer l’en-tête exact et les lignes ne contenant qu’un numéro.


## Exercice 1 - Étape 3 : découpage

### Q5

Avec une taille de 4 et un chevauchement de 1, le pas est de 3 caractères. Les morceaux commencent aux positions 0, 3 et 6 : `abcd`, `defg`, `ghij`. Le dernier caractère de chaque morceau est repris au début du suivant.

### Q6

| Taille (caractères) | Chevauchement | Nombre de morceaux | Longueur moyenne |
|---:|---:|---:|---:|
| 200 | 20 | 156 | 189,26 |
| 500 | 50 | 69 | 422,68 |
| 1000 | 100 | 38 | 746,45 |
