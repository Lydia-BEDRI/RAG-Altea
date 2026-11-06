from pathlib import Path

import chromadb
import streamlit as st
from etape4_indexation import creer_modele
from etape6_generation import repondre


@st.cache_resource
def charger_ressources():
    modele = creer_modele()
    chemin_base = Path(__file__).resolve().parent.parent / "base_vectorielle"
    client = chromadb.PersistentClient(path=str(chemin_base))
    collection = client.get_collection("altea")
    return modele, collection


modele, collection = charger_ressources()
st.title("Assistant documentaire Altéa")
question = st.text_input("Votre question")

if question:
    with st.spinner("Recherche dans la documentation..."):
        reponse, extraits = repondre(question, modele, collection)
    st.write(reponse)
    st.subheader("Sources")
    for i, extrait in enumerate(extraits, start=1):
        with st.expander(f"[{i}] {extrait['source']}, page {extrait['page']}"):
            st.write(extrait["texte"])
