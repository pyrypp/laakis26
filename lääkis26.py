import streamlit as st
import pandas as pd
import re

st.title("Todistusvalinnan pisteytykset vuodesta 2026 - Lääkis")

st.subheader("Kaikilta pisteytettävät aineet")

matematiikka_value = st.radio(
    "Matematiikka, pitkä",
    ["L (37,9)", "E (34,1)"],
    key="matematiikka",
    horizontal=True
)

äidinkieli_value = st.radio(
    "Äidinkieli",
    ["L (36,1)", "E (32,5)"],
    key="äidinkieli",
    horizontal=True
)

biologia_value = st.radio(
    "Biologia",
    ["L (34,0)", "E (30,6)"],
    key="biologia",
    horizontal=True
)

kemia_value = st.radio(
    "Kemia",
    ["L (32,3)", "E (29,1)"],
    key="kemia",
    horizontal=True
)


st.subheader("Kaksi muuta ainetta (joista vähintään toinen on ainereaali)")
placeholder = st.empty()

pitkä_kieli_value = st.radio(
    "Pitkä kieli",
    ["L (28,3)", "E (25,5)", "0"],
    key="pitkä_kieli",
    horizontal=True
)

keskipitkä_kieli_value = st.radio(
    "Keskipitkä kieli",
    ["L (25,0)", "E (20,0)", "0"],
    key="keskipitkä_kieli",
    horizontal=True
)

fysiikka_value = st.radio(
    "Fysiikka",
    ["L (24,5)", "E (19,6)", "0"],
    key="fysiikka",
    horizontal=True
)

psykologia_value = st.radio(
    "Psykologia",
    ["L (24,5)", "E (19,6)", "0"],
    key="psykologia",
    horizontal=True
)

def label_to_float(input_string):
    # Use regular expression to keep only digits and commas
    cleaned_string = re.sub(r'[^0-9,]', '', input_string)
    cleaned_string = cleaned_string.replace(",", ".")
    output_float = float(cleaned_string)
    return output_float


matematiikka_value_num = label_to_float(matematiikka_value)
äidinkieli_value_num = label_to_float(äidinkieli_value)
biologia_value_num = label_to_float(biologia_value)
kemia_value_num = label_to_float(kemia_value)
pitkä_kieli_value_num = label_to_float(pitkä_kieli_value)
keskipitkä_kieli_value_num = label_to_float(keskipitkä_kieli_value)
fysiikka_value_num = label_to_float(fysiikka_value)
psykologia_value_num = label_to_float(psykologia_value)

# Sum up all the button values
total_sum = (matematiikka_value_num + äidinkieli_value_num + biologia_value_num + kemia_value_num +
             pitkä_kieli_value_num + keskipitkä_kieli_value_num + fysiikka_value_num + psykologia_value_num)

total_sum_str = str(total_sum).replace(".", ",")

st.subheader("Pisteet")
st.subheader(f"{total_sum_str}/193,1")

if total_sum > 193.1:
    st.error("Valitse vain kaksi muuta ainetta!!")
    with placeholder.container():
       st.error("Valitse vain kaksi muuta ainetta!!")     