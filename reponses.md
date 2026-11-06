# Réponses aux questions du TP

## Exercice 1 — Étape 1 : collecte

### Q1

Le script suit le squelette du TP. `lire_pdf` utilise `PdfReader` pour extraire le texte de chaque page et enregistrer sa source et son numéro de page. `lire_txt` lit un fichier UTF-8 et le représente comme une page. `collecter` parcourt `docs/`, choisit la fonction selon l’extension et ajoute le service à chaque page.

### Q2

On conserve le nom du fichier et le numéro de page pour citer précisément la source dans une réponse et permettre au salarié de retrouver le passage. Le service permet de filtrer les résultats, par exemple pour chercher uniquement dans les documents RH, et de vérifier que la réponse vient du bon service.
