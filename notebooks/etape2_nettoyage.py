# etape2_nettoyage.py
import re



def nettoyer(texte):
    texte = re.sub(r"[ \t]+", " ", texte)  # plusieurs espaces -> un seul
    texte = re.sub(r"\n{3,}", "\n\n", texte)  # au plus une ligne vide
    texte = re.sub(r"-\n(\w)", r"\1", texte)  # recoller les mots coupés
    return texte.strip()


def nettoyer_pages(pages):
    pages_nettoyees = []
    for page in pages:
        texte = nettoyer(page["texte"])
        if texte:  # ignorer les pages vides après nettoyage
            page_nettoyee = page.copy()
            page_nettoyee["texte"] = texte
            pages_nettoyees.append(page_nettoyee)
    return pages_nettoyees
