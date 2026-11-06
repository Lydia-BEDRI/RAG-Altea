# etape3_decoupage.py

def decouper(texte, taille=500, chevauchement=50):
    assert chevauchement < taille, "le chevauchement doit être plus petit que la taille"
    morceaux = []
    debut = 0
    while debut < len(texte):
        fin = min(debut + taille, len(texte))
        morceaux.append(texte[debut:fin])
        if fin >= len(texte):
            break
        debut = fin - chevauchement
    return morceaux


def decouper_pages(pages, taille=500, chevauchement=50):
    chunks = []
    for page in pages:
        for i, morceau in enumerate(decouper(page["texte"], taille, chevauchement)):
            chunks.append({
                "id": f"{page['source']}-p{page['page']}-{i}",
                "texte": morceau,
                "source": page["source"],
                "page": page["page"],
                "service": page["service"],
            })
    return chunks
