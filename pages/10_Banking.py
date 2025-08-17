
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
render_section("banking")

st.subheader("Assistant de démarrage bancaire")
with st.form("bank_plan"):
    inc = st.number_input(t("income"), min_value=0, value=1200, step=50)
    c1,c2,c3 = st.columns(3)
    with c1:
        rent = st.number_input(t("rent"), min_value=0, value=700, step=25)
        util = st.number_input(t("utilities"), min_value=0, value=80, step=10)
    with c2:
        tr = st.number_input(t("transport_s"), min_value=0, value=50, step=10)
        tel = st.number_input(t("telecom"), min_value=0, value=20, step=5)
    with c3:
        food = st.number_input(t("groceries"), min_value=0, value=220, step=10)
        other = st.number_input(t("other_fixed"), min_value=0, value=30, step=5)
    submitted = st.form_submit_button(t("calc_plan"))
if submitted:
    fixed = rent + util + tr + tel + food + other
    leftover = max(0, inc - fixed)
    # Rule: base 10% of income; if leftover is small, save 5%; if big, up to 20% but not above 50% of leftover
    base_pct = 0.10
    if leftover < inc * 0.10:
        base_pct = 0.05
    elif leftover > inc * 0.30:
        base_pct = 0.20
    monthly_save = int(round(inc * base_pct))
    buffer = int(round(fixed * 3))
    lines = [
        "- " + t("open_individual"),
        "- " + t("open_savings"),
        "- " + t("save_percent").format(pct=int(base_pct*100), amt=monthly_save),
        "- " + t("build_buffer").format(buf=buffer)
    ]
    st.success("\n".join(lines))
    st.info(t("int_transfers_hint"))
    st.info(t("branch_hint"))

st.subheader(t("quiz"))
with st.form("bank_quiz"):
    profile = st.selectbox(t("profile"), [t("student"),t("worker"),t("family"),t("entrepreneur"),t("retiree")])
    papers = st.radio(t("papers"), [t("yes"),t("no")], horizontal=True)
    fx = st.radio(t("fx"), [t("yes"),t("no")], horizontal=True)
    branch = st.radio(t("branch"), [t("yes"),t("no")], horizontal=True)
    submitted2 = st.form_submit_button(t("see_rec"))
if submitted2:
    rec = []
    if papers == t("no"):
        rec.append("N26 / Revolut / Wise — ouverture rapide, justificatifs allégés.")
    if profile == t("entrepreneur"):
        rec.append("Qonto / Shine / BNP Pro — comptes pro adaptés.")
    if fx == t("yes"):
        rec.append("Revolut / Wise — frais FX bas et cartes multi-devises.")
    if branch == t("yes"):
        rec.append("BNP / Crédit Agricole / Société Générale — réseau d'agences.")
    if not rec:
        rec.append("Boursorama / Hello bank! — frais bas en ligne.")
    st.success(" • ".join(rec))
