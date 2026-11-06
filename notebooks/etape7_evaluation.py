import csv
from pathlib import Path

from etape5_recherche import rechercher

FICHIER_EVALUATION = Path(__file__).with_name("evaluation.csv")


def taux_reussite(modele, collection, fichier=FICHIER_EVALUATION, k=3):
    with open(fichier, encoding="utf-8") as f:
        lignes = list(csv.DictReader(f))
    trouves = 0
    for ligne in lignes:
        resultats = rechercher(ligne["question"], modele, collection, k=k)
        sources = [resultat["source"] for resultat in resultats]
        if ligne["document_attendu"] in sources:
            trouves += 1
    return trouves / len(lignes)
