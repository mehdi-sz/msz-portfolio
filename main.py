from pathlib import Path

import streamlit as st
from PIL import Image


# ## Configuration du Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "styles.css"
profile_pic = current_dir / "assets" / "profile-pic.png"
resume_file = current_dir / "assets" / "msz.pdf"
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


# ## Charger le css, le cv en pdf & photo de profil 
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ## Section d'intro
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
