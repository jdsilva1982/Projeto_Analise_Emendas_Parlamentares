#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
pd.set_option('display.float_format', "R$ {:20,.2f}".format)
import locale


# In[2]:


#Criando DataFrame
df = pd.read_csv("emendas_individuais.csv", sep=";", encoding='utf8')


# In[3]:


#Tratamento dos Numeros Negativos:
df["Valor empenhado"] = df["Valor empenhado"].str.replace('- ','-')


# In[4]:


#Substituindo "." por vazio:
df["Valor empenhado"] = df["Valor empenhado"].str.replace('.','')


# In[5]:


#Substituindo "," por ".":
df["Valor empenhado"] = df["Valor empenhado"].str.replace(',','.')


# In[6]:


df["Valor empenhado"] = df["Valor empenhado"].astype(float)


# In[7]:


#Criando um novo DF com os dados de "PERNAMBUCO (UF)"
df_pe = df[df["Localidade do gasto (Regionalização)"] == "PERNAMBUCO (UF)"]


# In[8]:


df_pe.sample(5)


# In[21]:


df_top10 = df_pe.groupby("Autor da emenda")["Valor empenhado"].sum().sort_values(ascending=False).reset_index().head(5)


# In[26]:


fig = px.bar(df_top10, x='Autor da emenda', y="Valor empenhado", title="TOP 5 - Valores Liberados em Emendas Individuais",  orientation='v')
fig.show()


# In[11]:


df_funcao = df_pe.groupby("Função")["Valor empenhado"].sum().sort_values(ascending=False).reset_index().head(5)


# In[12]:


df_funcao


# In[16]:


fig = px.pie(df_funcao, values="Valor empenhado", names="Função", title="TOP 5 - Emendas Liberadas por Área")
fig.show()


# In[ ]:


pd.set_option('display.max_rows', None)
df_pe.groupby(["Autor da emenda","Função","Subfunção"])["Valor empenhado"].sum().sort_values(ascending=False)

