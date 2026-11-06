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

## Exercice 2 - Étape 5 : recherche

### Q1

Les trois résultats par question, classés par score décroissant :

- Congé : `conges_absences.pdf` p. 2 (0,652), `conges_absences.pdf` p. 1 (0,597), `teletravail.pdf` p. 1 (0,571). La procédure pour poser un congé apparaît dans le deuxième résultat.
- Télétravail : `teletravail.pdf` p. 1 (0,767), `conges_absences.pdf` p. 1 (0,623), `teletravail.pdf` p. 1 (0,608).
- Mot de passe : `mot_de_passe.txt` p. 1 (0,678), `charte_informatique.pdf` p. 1 (0,637), `mot_de_passe.txt` p. 1 (0,566).

Un score plus élevé indique un chunk plus proche de la question.

### Q2

Avec `k = 1`, on obtient le meilleur résultat seulement, avec peu de contexte. `k = 3` donne davantage d’éléments utiles. `k = 10` élargit les résultats, mais ajoute aussi des passages moins pertinents, comme `securite_emails.txt` pour une question sur le télétravail.

### Q3

Le filtre `RH` retourne des documents RH pertinents sur le télétravail. Le filtre `IT` retourne des documents IT, mais ils ne répondent pas à cette question. Le filtre limite la recherche, mais ne suffit pas à garantir la confidentialité : l’application doit vérifier les droits du salarié et imposer le filtre côté serveur.


## Exercice 2 - Étape 6 : génération

### Q5

| Question | Réponse juste ? | Sources citées ? | Phrase de repli quand il le fallait ? |
|---|---|---|---|
| Comment poser un jour de congé ? | Oui, la procédure principale est donnée. | Oui, le document et la page sont corrects. | Non, la documentation contient la réponse. |
| Combien de jours de télétravail par semaine sont autorisés ? | Non, la réponse donne le cas des alternants au lieu de la règle générale de 2 jours. | Oui, mais l’extrait est mal interprété. | Non, la documentation contient la réponse. |
| Comment réinitialiser mon mot de passe ? | Non, le modèle utilise le repli alors que la procédure est dans le document. | Oui, mais la source pertinente n’est pas exploitée. | Non, le repli n’était pas nécessaire. |
| Quel temps fera-t-il demain ? | Oui, le modèle indique qu’il ne trouve pas l’information. | Non, aucune source n’est citée. | Oui. |
| Quel est le chiffre d’affaires d’Altéa Services en 2025 ? | Oui, le modèle indique qu’il ne trouve pas l’information. | Non, aucune source ne répond à la question. | Oui. |

### Q6

Sans extraits, le LLM affirme que le télétravail est autorisé jusqu’à 5 jours par semaine : cette information est fausse et constitue une hallucination. Le RAG retrouve le document, mais répond 1 jour, qui ne concerne que les alternants et les stagiaires. La règle générale du document est jusqu’à 2 jours par semaine pour les salariés éligibles. Le RAG réduit les hallucinations en fournissant des extraits et en demandant de s’y limiter, mais une mauvaise interprétation reste possible.

### Q7

Une température de 0 réduit les variations aléatoires et rend les réponses documentaires plus cohérentes d’une exécution à l’autre. Elle ne garantit pas que la réponse soit vraie.

## Exercice 2 - Étape 7 : évaluation

### Q8

`evaluation.csv` contient dix questions associées au document attendu. Le document VPN est `vpn.txt`, conformément au nom présent dans le corpus.

### Q9

Après correction du nom du document VPN, les résultats sont :

| k | Questions avec le bon document retrouvé |
|---:|---:|
| 1 | 80 % |
| 3 | 90 % |
| 5 | 100 % |

Les taux initiaux étaient inférieurs de 10 points, car le CSV indiquait `vpn.pdf` alors que le document retrouvé s’appelle `vpn.txt`.

### Q10

| Question | Réponse | Source exacte ? |
|---|---|---|
| Télétravail | Fausse : la réponse donne le cas des alternants comme règle générale. | Oui, mais le passage est mal interprété. |
| Mot de passe | Partielle : la procédure est commencée, mais le texte s’arrête avant la fin. | Oui. |
| Congé | Partielle : les étapes et la validation sont décrites, mais le portail MonEspace n’est pas mentionné. | Oui. |
| Note de frais | Juste. | Oui, la page citée correspond à l’extrait retrouvé. |
| Mutuelle | Fausse : le modèle utilise le repli malgré la présence du document attendu parmi les résultats. | Non, il cite la charte informatique. |
| VPN | Fausse : le modèle ne donne pas la procédure et ne fait qu’énumérer les sources. | Oui, le fichier et la page correspondent au document attendu. |
| Matériel informatique | Fausse : le modèle ne donne pas de réponse et n’affiche que des citations. | Oui, les citations pointent vers le document attendu. |
| E-mail suspect | Fausse : le modèle n’indique pas la marche à suivre et termine par le repli malgré les extraits pertinents. | Oui, les extraits cités viennent du document attendu. |
| Horaires | Fausse : le modèle utilise le repli, car le document attendu n’a pas été retrouvé. | Non. |
| Accès au siège | Juste. | Oui. |

Les réponses entièrement justes représentent 2 sur 10, soit 20 %. Les réponses correctement sourcées représentent 8 sur 10, soit 80 %.

### Q11

La réponse sur le télétravail est fausse alors que `teletravail.pdf` a été retrouvé à l’étape 5 : l’erreur vient donc de la génération. J’ai ajouté au prompt une consigne demandant de distinguer la règle générale des cas particuliers. Après test, le modèle répond encore « 1 jour par semaine » et ne corrige pas l’erreur.
