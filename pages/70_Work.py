
import streamlit as st
from data.utils import render_section, t, guard

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
render_section("work")
st.subheader(t("quiz"))
st.info("Questionnaire détaillé bientôt ici pour ce parcours.")
