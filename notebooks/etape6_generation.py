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
Réponds en français avec un ton poli, professionnel et concis, comme à un salarié.
Réponds directement à la question en utilisant UNIQUEMENT les extraits ci-dessous.
Ne recopie pas les extraits et n'écris pas le nom du document ni la page dans ta réponse ; l'application affiche les sources séparément.
Après chaque information, indique uniquement le numéro de l'extrait entre crochets, par exemple [1].
Pour une question générale, donne d'abord la règle générale. Mentionne les règles particulières séparément et seulement comme exceptions.
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
