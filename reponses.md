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

### Q7

Un chunk trop petit risque de couper une information de son contexte et de rendre la recherche moins utile. Un chunk trop grand peut mélanger plusieurs sujets et rendre les passages trouvés moins précis. Le chevauchement conserve un peu de contexte entre deux morceaux, au prix d’un contenu répété. Pour la suite, je retiens une taille de 500 caractères et un chevauchement de 50 : les résultats donnent 69 chunks, contre 156 avec 200 caractères et 38 avec 1000.

## Exercice 1 - Étape 4 : embeddings et indexation

### Q8

Le modèle produit des vecteurs de 384 nombres. Avec 69 chunks et la taille retenue, il faut stocker 69 x 384 = 26 496 nombres.

### Q9

Les phrases 1 et 2 sont les plus proches, avec une similarité de 0,4888. Elles parlent toutes deux de demander un congé, même si les mots employés diffèrent. La phrase 3, sur un problème de VPN, a une similarité proche de zéro avec les deux autres.

### Q10

La base Chroma contient 69 chunks, comme les 69 chunks produits.

### Q11

Les trois chunks retrouvés pour chaque question, classés par distance croissante :

- Congé : `conges_absences.pdf` p. 2 (0,348), `conges_absences.pdf` p. 1 (0,403), `teletravail.pdf` p. 1 (0,429). La procédure de demande se trouve dans le deuxième résultat.
- Télétravail : `teletravail.pdf` p. 1 (0,233), `conges_absences.pdf` p. 1 (0,377), `teletravail.pdf` p. 1 (0,392).
- Mot de passe : `mot_de_passe.txt` p. 1 (0,322), `charte_informatique.pdf` p. 1 (0,363), `mot_de_passe.txt` p. 1 (0,434).

Une distance plus faible indique un résultat plus proche.

### Q12

En relançant l’indexation avec les mêmes chunks et les mêmes identifiants, le nombre ne double pas : il reste à 69. `upsert` crée un identifiant s’il n’existe pas et remplace son contenu s’il existe déjà. `add` ne remplace pas un identifiant existant. Si un document est modifié, il faut supprimer ses anciens chunks de la base puis réindexer sa nouvelle version.

### Q13

`base_vectorielle/` contient la base Chroma générée localement. Elle n’est pas envoyée sur GitHub pour éviter d’y stocker des fichiers générés et de devoir les versionner. Un collègue clone le code, installe les dépendances, récupère les documents autorisés, puis exécute les cellules du notebook jusqu’à l’indexation pour recréer la base.
