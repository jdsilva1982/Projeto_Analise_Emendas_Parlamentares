#importando as bibliotecas
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
pd.set_option('display.float_format', "R$ {:20,.2f}".format)
import locale

st.set_page_config(
         page_title="Minha primeira Web APP", #1
         page_icon="🧊", #2
         layout="centered", #3
         initial_sidebar_state="expanded", #4
)

#título
with st.container():
    #st.image("datasage.png", width=100),
    st.title('🧊DashBoard: ',)
    st.subheader('Análise das liberações de Emendas Parlamentares: ')
    st.caption('Na política brasileira, entende-se por emendas parlamentares, os recursos do orçamento público legalmente indicados pelos membros do Congresso Nacional e das Assembleias Legislativas estaduais para finalidades públicas, geralmente relacionada ao interesse temático e eleitoral de cada parlamentar.  - Wikipédia')
    st.caption("---")

@st.cache_data
def carrega_dados():
    df = pd.read_csv("emendasPE.csv", sep=",", encoding='utf8')
    df['ano'] = df['ano'].apply(str)
    return df
df = carrega_dados()
## Adicionar uma select box para escolher o tipo de gráfico
tipo_grafico = st.selectbox('Escolha o de gráfico que deseja exibir',
                             ["Valores Liberados em Emendas por Ano",
                             "Quantidade de Emendas Liberadas por ano para PE",
                             "Valores Liberados por tipo de Emenda em PE",
                             "TOP 5 - Áreas de função das Emendas em 2023 - PE",
                             "TOP 5 - Valores Liberados em Emendas Individuais em 2023"])

if tipo_grafico == "Valores Liberados em Emendas por Ano":
    df_ValorAno = df.groupby('ano')['valorEmpenhado'].sum().reset_index()
    fig = px.line(df_ValorAno, x='ano', y='valorEmpenhado', labels={'ano': 'Ano', 'valorEmpenhado': 'Valor Empenhado'},
                  title="Valores Liberados em Emendas por Ano", markers=True)
    fig.update_traces(textposition="bottom right")
    fig.update_traces(mode="markers+lines")
    st.plotly_chart(fig)

elif tipo_grafico == "Quantidade de Emendas Liberadas por ano para PE":
    df_QtdAno = df.groupby('ano')['ano'].value_counts().reset_index()
    fig = px.bar(df_QtdAno, x='ano', y='count', labels={'ano': '', 'count': ''},title="Quantidade de Emendas Liberadas por ano para PE", text='count')
    st.plotly_chart(fig)

elif tipo_grafico == "Valores Liberados por tipo de Emenda em PE":
    df_tipoEmenda = df.groupby('tipoEmenda')['valorEmpenhado'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(df_tipoEmenda, x='tipoEmenda', y='valorEmpenhado', labels={'valorEmpenhado': 'Valor Empenhado', 'tipoEmenda': ''}, text_auto='.2s', title="Valores Liberados por tipo de Emenda em PE", text='valorEmpenhado')
    st.plotly_chart(fig)

elif tipo_grafico == "TOP 5 - Áreas de função das Emendas em 2023 - PE":
    df_funcao2023 = df[df["ano"] == "2023"].groupby("funcao")["valorEmpenhado"].sum().sort_values(ascending=False).reset_index().head(5)
    fig = px.pie(df_funcao2023, values="valorEmpenhado", names="funcao",title="TOP 5 - Áreas de função das Emendas em 2023 - PE")
    st.plotly_chart(fig)

elif tipo_grafico == "TOP 5 - Valores Liberados em Emendas Individuais em 2023":
    df_top10 = df[(df.tipoEmenda == 'Emenda Individual') & (df.ano == "2023")].groupby('nomeAutor')['valorEmpenhado'].sum().sort_values(ascending=False).reset_index().head(5)
    fig = px.bar(df_top10, x='nomeAutor', y='valorEmpenhado', text_auto='.5s', labels={'valorEmpenhado': 'Valor Empenhado', 'nomeAutor': 'Autor da Emenda'},                 title="TOP 5 - Valores Liberados em Emendas Individuais em 2023", text='valorEmpenhado')
    st.plotly_chart(fig)
