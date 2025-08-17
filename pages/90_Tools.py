
import streamlit as st
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
st.title(t("tools"))
st.header(t("budget_tool"))
c1, c2, c3 = st.columns(3)
with c1:
    inc = st.number_input("Revenu mensuel (€)", min_value=0, value=1200, step=50)
with c2:
    rent = st.number_input("Loyer (€)", min_value=0, value=700, step=50)
    tr = st.number_input("Transport (€)", min_value=0, value=50, step=10)
with c3:
    food = st.number_input("Alimentation (€)", min_value=0, value=250, step=10)
    tel = st.number_input("Télécoms (€)", min_value=0, value=20, step=5)
ins = st.number_input("Assurances (€)", min_value=0, value=15, step=5)
out = rent + tr + food + tel + ins
bal = inc - out
st.metric("Total dépenses (€)", out, delta=None)
st.metric("Solde (€)", bal, delta=None)
st.header(t("credit_tool"))
A = st.number_input("Montant (€)", min_value=0, value=2000, step=100)
R = st.number_input("Taux annuel (%)", min_value=0.0, value=8.5, step=0.1)
M = st.number_input("Durée (mois)", min_value=1, value=24, step=1)
def monthly(a,rpct,m):
    r = (rpct/100)/12
    if m <= 0: return 0.0
    if r == 0: return a/m
    return (a*r)/(1 - (1+r)**(-m))
p = monthly(A,R,M)
st.metric("Mensualité (€)", round(p,2))
st.write(f"Total remboursé : **{round(p*M,2)} €**")
