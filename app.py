# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st


st.title('CONSAR DATOS URV ACTUALIZADO MATO 2023')

df = pd.read_excel(r'datos.xlsx', sheet_name='URV')
st.table(df)