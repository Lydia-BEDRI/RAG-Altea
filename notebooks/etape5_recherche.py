def rechercher(question, modele, collection, k=3, service=None):
    vecteur = modele.encode([question]).tolist()
    filtre = {"service": service} if service else None
    resultat = collection.query(
        query_embeddings=vecteur,
        n_results=k,
        where=filtre,
    )
    resultats = []
    for texte, metadonnees, distance in zip(
        resultat["documents"][0],
        resultat["metadatas"][0],
        resultat["distances"][0],
    ):
        resultats.append({
            "texte": texte,
            "source": metadonnees["source"],
            "page": metadonnees["page"],
            "service": metadonnees["service"],
            "score": 1 - distance,
        })
    return resultats
