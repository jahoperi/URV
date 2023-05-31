from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('datos.csv')

AgGrid(df)
