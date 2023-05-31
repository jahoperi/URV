import pandas as pd
import streamlit as st
df = pd.read_csv("datos.csv")

st.dataframe(df)
