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
    pages = []
    for chemin in sorted(Path(dossier).rglob("*")):
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

    documents = sorted({(page["service"], page["source"]) for page in pages})
    for service, source in documents:
        nombre = sum(
            1 for page in pages
            if page["service"] == service and page["source"] == source
        )
        print(f"{service}/{source} : {nombre} page(s) lue(s)")

    print(len(pages), "pages lues")
