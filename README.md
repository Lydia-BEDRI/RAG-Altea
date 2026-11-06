# RAG Altéa Services

Prototype d’assistant documentaire pour répondre aux questions des salariés à partir du corpus fictif d’Altéa Services. Les réponses sont générées à partir des extraits retrouvés et affichent leurs sources.

## Installation

Depuis le dossier `rag_altea` :

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Installer Ollama, puis télécharger et lancer le modèle local utilisé par le projet :

```bash
ollama run qwen3:0.6b
```

Garder Ollama actif pendant l’utilisation du notebook ou de l’application. Aucune clé OpenAI n’est nécessaire.

## Ordre de lancement

1. Ouvrir `notebooks/TP_RAG_Altea.ipynb` avec l’environnement `.venv` et exécuter les cellules dans l’ordre jusqu’à l’indexation pour créer `base_vectorielle/`.
2. Exécuter les étapes de recherche, génération et évaluation dans le même notebook.
3. Depuis `rag_altea/notebooks`, lancer l’interface :

```bash
streamlit run app.py
```

## Exemple de question

`Comment poser un jour de congé ?`

## Résultats de l’évaluation

Sur les dix questions de `notebooks/evaluation.csv`, le document attendu est retrouvé dans 80 % des cas avec `k=1`, 90 % avec `k=3` et 100 % avec `k=5`. La notation manuelle des réponses donne 20 % de réponses entièrement justes et 80 % de réponses correctement sourcées.

## Limites connues

- Le petit modèle local peut mal interpréter une règle ou ne pas répondre alors que la documentation contient l’information.
- Le prototype ne met pas en place de contrôle d’accès par salarié.
- Une modification des documents nécessite de reconstruire ou mettre à jour l’index.
- L’application dépend des ressources matérielles locales et du serveur Ollama.

## Auteurs

Lydia BEDRI.
