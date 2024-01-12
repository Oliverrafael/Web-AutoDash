import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo os dados
car_data = pd.read_csv('../vehicles.csv')

# Botão para criar histograma
hist_button = st.button('Criar histograma')

if hist_button:
    # Mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # Criar histograma
    fig = px.histogram(car_data, x="odometer")

    # Exibir gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar gráfico de dispersão
disp_button = st.button('Criar gráfico de dispersão')

if disp_button:
    # Mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # Criar gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # Exibir gráfico interativo
    st.plotly_chart(fig, use_container_width=True)
