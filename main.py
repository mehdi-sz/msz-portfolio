from pathlib import Path

import streamlit as st
from PIL import Image


# ## Configuration du Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "styles.css"
resume_file = current_dir / "assets" / "profile-pic.png"

# ## Paramètre généraux du projet
PAGE_TITLE = "Mehdi Zayani | Ingénieur Logiciel"
PAGE_ICON = ":wave:"
NAME = "Mehdi Zayani"
DESCRIPTION = """
Développeur FullStack, Chef de projets, Java JEE React Android.
"""
EMAIL = "mehdi.zayani15@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Développement & Réfactoring  d'API - Concéption - dévelppement  & refactoring de plusieurs api pour projet SaaS": "https://youtube.com",
    "🏆 Création d'une soltion web et mobile pour la gestion de tri des déchet dans le batiment": "https://youtube.com",
    "🏆 Mise en place d'un ERP - Développement de modules complémentaire en PHP ": "https://youtube.com",
    "🏆 Fany - Une Application SaaS pour la location de services d'artistes en IDF": "https://youtube.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


st.title("Hello World !")