# etape1_collecte.py
from pathlib import Path

from pypdf import PdfReader


def lire_pdf(chemin):
    lecteur = PdfReader(chemin)
    pages = []
    for numero, page in enumerate(lecteur.pages, start=1):
        texte = page.extract_text() or ""
        pages.append({"source": chemin.name, "page": numero, "texte": texte})
    return pages


def lire_txt(chemin):
    texte = chemin.read_text(encoding="utf-8")
    return [{"source": chemin.name, "page": 1, "texte": texte}]


def collecter(dossier="docs"):
    dossier = Path(dossier)
    if not dossier.is_absolute():
        dossier = Path(__file__).resolve().parent.parent / dossier
    pages = []
    for chemin in sorted(dossier.rglob("*")):
        if not chemin.is_file():
            continue
        if chemin.suffix.lower() == ".pdf":
            pages_fichier = lire_pdf(chemin)
        elif chemin.suffix.lower() == ".txt":
            pages_fichier = lire_txt(chemin)
        else:
            continue

        service = chemin.parent.name  # RH, IT ou General
        for page in pages_fichier:
            page["service"] = service
        pages.extend(pages_fichier)
    return pages

if __name__ == "__main__":
    pages = collecter()
    print(len(pages), "pages lues")
