import pandas as pd
import plotly.express as px
import streamlit as st

df_vehicles = pd.read_csv('vehicles_us.csv')# lendo os dados

st.header('estoque de veículos')# titulo do dashboard

hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
            # escrever uma mensagem
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
            fig = px.histogram(df_vehicles, x="odometer")
        
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)
            
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão do preço em relação à quilometragem')
    fig = px.scatter(df_vehicles, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_hist = st.checkbox('Criar um histograma')

if build_hist: # se a caixa de seleção for selecionada
            st.write('Criando um histograma para a coluna odometer')
            fig_3 = px.histogram(df_vehicles, x='odometer')
            st.plotly_chart(fig_3, key='histogram', use_container_width=True)