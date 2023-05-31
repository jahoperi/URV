import pandas as pd
import streamlit as st

st.text("hola lllllllllllllll")
a = "sreeram"
st.text("ffffffffffffffffffffffffffffffffffffffffff{}.format()")

st.header("fttttttttttttttttttttttttttttttttttttttttttttttttttttt")
st.subheader("333333333333333333333333333333333333333333333333333")
st.title("datos públicos de URV")
st.markdown("wwwwwwwwwwwwwwwwwwwwww")



df = pd.read_csv("datos.csv")

st.dataframe(df)
