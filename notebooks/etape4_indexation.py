# etape4_indexation.py
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


NOM_MODELE = "paraphrase-multilingual-MiniLM-L12-v2"


def creer_modele():
    return SentenceTransformer(NOM_MODELE)


def indexer_chunks(chunks, modele):
    chemin_base = Path(__file__).resolve().parent.parent / "base_vectorielle"
    client = chromadb.PersistentClient(path=str(chemin_base))
    collection = client.get_or_create_collection(
        name="altea",
        metadata={"hnsw:space": "cosine"},
    )
    textes = [chunk["texte"] for chunk in chunks]
    vecteurs = modele.encode(textes, show_progress_bar=True).tolist()
    collection.upsert(
        ids=[chunk["id"] for chunk in chunks],
        documents=textes,
        embeddings=vecteurs,
        metadatas=[
            {
                "source": chunk["source"],
                "page": chunk["page"],
                "service": chunk["service"],
            }
            for chunk in chunks
        ],
    )
    return collection


def rechercher(collection, modele, question, k=3):
    vecteur_question = modele.encode([question]).tolist()
    return collection.query(
        query_embeddings=vecteur_question,
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )
