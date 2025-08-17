
import streamlit as st
import pandas as pd
from data.utils import t, guard

st.sidebar.title("Benew")
st.sidebar.page_link("app.py", label=t("menu_home"))
st.sidebar.page_link("pages/00_Login.py", label=t("menu_login"))
st.sidebar.page_link("pages/01_Persona.py", label=t("menu_persona"))
st.sidebar.page_link("pages/10_Banking.py", label=t("menu_banking"))
st.sidebar.page_link("pages/20_Insurance.py", label=t("menu_insurance"))
st.sidebar.page_link("pages/30_Healthcare.py", label=t("menu_healthcare"))
st.sidebar.page_link("pages/40_Taxation.py", label=t("menu_taxation"))
st.sidebar.page_link("pages/50_Housing.py", label=t("menu_housing"))
st.sidebar.page_link("pages/60_Transport.py", label=t("menu_transport"))
st.sidebar.page_link("pages/70_Work.py", label=t("menu_work"))
st.sidebar.page_link("pages/80_Life.py", label=t("menu_life"))
st.sidebar.page_link("pages/90_Tools.py", label=t("menu_tools"))
st.sidebar.page_link("pages/91_Glossary.py", label=t("menu_glossary"))
st.sidebar.page_link("pages/92_Plan30.py", label=t("menu_plan"))
st.sidebar.page_link("pages/93_Compare.py", label=t("menu_compare"))
st.sidebar.page_link("pages/94_Export.py", label=t("menu_export"))

guard()
st.title(t("compare_title"))

st.subheader("Banques (aperçu indicatif)")
banks = pd.DataFrame([
    {"Nom":"Boursorama","Type":"Banque en ligne","Forces":"Frais bas","International":"Moyen","Agences":"Non","Site":"https://www.boursorama.com/","Carte/mois":"0–5€"},
    {"Nom":"Hello bank!","Type":"En ligne (BNP)","Forces":"Écosystème BNP","International":"Moyen","Agences":"Oui (BNP)","Site":"https://www.hellobank.fr/","Carte/mois":"0–5€"},
    {"Nom":"BNP Paribas","Type":"Traditionnelle","Forces":"Réseau agences","International":"Bon","Agences":"Oui","Site":"https://mabanque.bnpparibas/","Carte/mois":"5–10€"},
    {"Nom":"Crédit Agricole","Type":"Traditionnelle","Forces":"Réseau local","International":"Bon","Agences":"Oui","Site":"https://www.credit-agricole.fr/","Carte/mois":"5–10€"},
    {"Nom":"Société Générale","Type":"Traditionnelle","Forces":"Réseau agences","International":"Bon","Agences":"Oui","Site":"https://particuliers.societegenerale.fr/","Carte/mois":"5–10€"},
    {"Nom":"N26","Type":"Fintech","Forces":"Ouverture rapide","International":"Très bon","Agences":"Non","Site":"https://n26.com/fr-fr","Carte/mois":"0–10€"},
    {"Nom":"Revolut","Type":"Fintech","Forces":"FX bas, multi‑devises","International":"Excellent","Agences":"Non","Site":"https://www.revolut.com/fr-FR/","Carte/mois":"0–10€"},
    {"Nom":"Wise","Type":"Fintech","Forces":"Virements internationaux","International":"Excellent","Agences":"Non","Site":"https://wise.com/fr/","Carte/mois":"0–10€"}
])
st.dataframe(banks)

st.subheader("Assureurs (aperçu indicatif)")
ins = pd.DataFrame([
    {"Nom":"MAIF","Forces":"Habitation/auto solides","Site":"https://www.maif.fr/"},
    {"Nom":"MACIF","Forces":"Rapport couverture/prix","Site":"https://www.macif.fr/"},
    {"Nom":"MAAF","Forces":"Auto/habitation","Site":"https://www.maaf.fr/"},
    {"Nom":"AXA","Forces":"Réseau, contrats variés","Site":"https://www.axa.fr/"},
    {"Nom":"Allianz","Forces":"International","Site":"https://www.allianz.fr/"}
])
st.dataframe(ins)

st.caption("Indications non contractuelles. Vérifiez les conditions actuelles sur les sites.")
