from openai import OpenAI

from etape5_recherche import rechercher

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODELE = "qwen3:0.6b"
REPLI = "Je ne trouve pas cette information dans la documentation."


def construire_prompt(question, extraits):
    contexte = ""
    for i, extrait in enumerate(extraits, start=1):
        contexte += (
            f"[{i}] ({extrait['source']}, page {extrait['page']})\n"
            f"{extrait['texte']}\n\n"
        )
    return f"""Tu es l'assistant interne d'Altéa Services.
Réponds à la question en utilisant UNIQUEMENT les extraits ci-dessous.
Après chaque information, indique le numéro de l'extrait entre crochets, par exemple [1].
Si les extraits présentent une règle générale et un cas particulier, distingue-les explicitement.
Si les extraits ne contiennent pas la réponse, réponds exactement : "{REPLI}"

Extraits :
{contexte}
Question : {question}
Réponse :"""


def repondre(question, modele, collection, k=3):
    extraits = rechercher(question, modele, collection, k=k)
    prompt = construire_prompt(question, extraits)
    reponse = client.chat.completions.create(
        model=MODELE,
        temperature=0,
        reasoning_effort="none",
        messages=[{"role": "user", "content": prompt}],
    )
    return reponse.choices[0].message.content, extraits
