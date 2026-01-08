import streamlit as st
from clamp_calc import calculate_clamp

st.title("CSS clamp() Calculator")

st.write("Adjust the values below to generate a responsive CSS clamp().")

min_size = st.number_input("Minimum font size (rem)", min_value=0.1, value=1.0, step=0.005)

max_size = st.number_input("Maximum font size (rem)", min_value=0.1, value=2.0, step=0.005)

vw_min = st.number_input("Minimum viewport width (px)", min_value=1, value=300, step=1)

vw_max = st.number_input("Maximum viewport width (px)", min_value=1, value=768, step=1)

precision = st.slider("Decimal precision", min_value=0, max_value=6, value=3)

try:
    result = calculate_clamp(min_size, max_size, vw_min, vw_max, precision=precision)
    st.code(result["css"], language="css")
except ValueError as e:
    st.error(str(e))