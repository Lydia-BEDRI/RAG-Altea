# RAG Altéa Services

Prototype d'assistant RAG documentaire réalisé étape par étape à partir du TP.

## Environnement

L'environnement virtuel du projet est isolé dans `.venv/`.

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Les dépendances sont déclarées, mais ne sont pas encore installées. Le corpus fourni
se trouve pour le moment dans `~/Téléchargements/corpus_altea/docs/`.

## Structure

- `docs/RH/`, `docs/IT/`, `docs/General/` : documents du corpus à intégrer.
- `etape1_collecte.py` à `etape7_evaluation.py` : scripts à construire au fil du TP.
- `base_vectorielle/` : index local généré par l'étape 4, ignoré par Git.
- `app.py` : interface Streamlit prévue à l'étape 8.
- `reponses.md` : réponses écrites aux questions du TP.

