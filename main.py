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
Expert Full-Stack aguerri, je mets en œuvre ma créativité technique pour des solutions innovantes.
"""
EMAIL = "mehdi.zayani15@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Master 2, Manager de projets informatique": "https://youtube.com",
    "🏆 Diplôme d'ingénierie en sciences appliquées": "https://youtube.com",
    "🏆 Certification Google - Digital Marketing fundamentals ": "https://youtube.com",
    "🏆 Certification Cisco - CCNA 1,2,3,4 ": "https://youtube.com",
    "🏆 Toeic | Score  860 " :"",
    "🏆 Certification FreeCodeCamp - WebDesign" : "",
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
    st.write("📮", EMAIL)

# ## Liens vers les résaux sociaux
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ## QUALIFICATIONS  
st.write('\n')
st.subheader("Compétences")
st.write(
    """
- ✅  Développement Full-Stack: Expertise dans JavaScript, Node.js, React/Angular, avec une capacité avérée à concevoir des architectures robustes.
- ✅  Gestion de Projet Agile: Chef de projet expérimenté, adeptes des méthodologies Agile/Scrum, assurant une livraison efficace et dans les délais.
- ✅  Communication Avancée: Excellentes compétences de communication pour collaborer efficacement avec les équipes et les parties prenantes, traduisant les besoins commerciaux en solutions techniques.
- ✅  Résolution Créative des Problèmes: Aptitude démontrée à résoudre des défis complexes de manière innovante, avec un engagement continu envers l'apprentissage des nouvelles technologies.
"""
)

# ## Compétences
st.write('\n')
st.subheader("Compétences Téchniques")
st.write(
    """
- 👩‍💻 Programmation: Python,JAVA, Javascript, TS, JSX,React, Spring, Angular, Android, SQL, VBA
- 📊 Visulisation de données: PowerBi, MS Excel,GraphQL, Plotly
- 📲 App Dev: Android, React Native Flask Ionic
- 🗄️ Bases de données: Postgres, MongoDB, MySQL, Oracle, SQL Server
"""
)
# ## Expérience Professionnelle
st.write('\n')
st.subheader("Expérience Professionnelle")
st.write("---")

# ## Experience La Sacem
st.write("🚧", "**Ingénieur d'études et développement | La Sacem**")
st.write("007-2017 - 08-2018")
st.write(
    """
- ► Conception et mise en œuvre d'applications robustes avec Java JEE, utilisant Oracle comme base de données.
- ► Développement d'interfaces utilisateur interactives avec JavaScript et React pour une expérience utilisateur optimale.
- ► Gestion complète du cycle de vie du développement, de la conception à la mise en production, pour des projets novateurs et réussis.
"""
)

# --- Diplomes & certification---
st.write('\n')
st.subheader("Diplômes & Certificats")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")