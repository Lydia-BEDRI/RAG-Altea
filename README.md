# RAG Altéa Services

Prototype d'assistant RAG documentaire réalisé étape par étape à partir du TP.

## Environnement

L'environnement virtuel du projet est isolé dans `.venv/`.

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Le corpus fourni est rangé dans le dossier `docs/`.

## Structure

- `docs/RH/`, `docs/IT/`, `docs/General/` : documents du corpus.
- `notebooks/etape1_collecte.py` à `notebooks/etape7_evaluation.py` : scripts à construire au fil du TP.
- `base_vectorielle/` : index local généré par l'étape 4, ignoré par Git.
- `notebooks/app.py` : interface Streamlit prévue à l'étape 8.
- `reponses.md` : réponses écrites aux questions du TP.


## Lancer la collecte

Depuis la racine du projet, avec l’environnement activé :

```bash
python notebooks/etape1_collecte.py
```
