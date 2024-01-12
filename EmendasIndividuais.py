import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
pd.set_option('display.float_format', "R$ {:20,.2f}".format)
import locale

df = pd.read_csv("emendas_individuais.csv", sep=";", encoding='utf8')
df["Valor empenhado"] = df["Valor empenhado"].str.replace('- ','-')
df["Valor empenhado"] = df["Valor empenhado"].str.replace('.','')
df["Valor empenhado"] = df["Valor empenhado"].str.replace(',','.')
df["Valor empenhado"] = df["Valor empenhado"].astype(float)
df_pe = df[df["Localidade do gasto (Regionalização)"] == "PERNAMBUCO (UF)"]
df_pe.sample(5)
df_top10 = df_pe.groupby("Autor da emenda")["Valor empenhado"].sum().sort_values(ascending=False).reset_index().head(5)
fig = px.bar(df_top10, x='Autor da emenda', y="Valor empenhado", title="TOP 5 - Valores Liberados em Emendas Individuais",  orientation='v')
fig.show()
df_funcao = df_pe.groupby("Função")["Valor empenhado"].sum().sort_values(ascending=False).reset_index().head(5)
df_funcao
fig = px.pie(df_funcao, values="Valor empenhado", names="Função", title="TOP 5 - Emendas Liberadas por Área")
fig.show()
pd.set_option('display.max_rows', None)
df_pe.groupby(["Autor da emenda","Função","Subfunção"])["Valor empenhado"].sum().sort_values(ascending=False)