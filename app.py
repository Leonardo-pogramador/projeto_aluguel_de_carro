# import streamlit as st


# #title = titulo
# st.title('olá mundo :D')

# #pede uma data
# date = st.date_input("Selecione uma data")

# #pede um arquivo
# file = st.file_uploader("Selecione um arquivo topzera")

#python -m streamlit run app.py


# #python -m streamlit run app.py

import streamlit as st
import pandas as pd

# ---------------------------------------------- Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('leo cars')

carros = ['Kwid', 'Strada', 'Corsa', 'Jaguar', 'Corolla', 'Porsche', 'Toro', 'Fusca']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

# ---------------------------------------------- Principal

st.title('Leo Cars - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'Kwid':
    diaria = 180

elif opcao == 'Strada':
    diaria = 850

elif opcao == 'Corsa':
    diaria = 160

elif opcao == 'Jaguar':
    diaria = 1600

elif opcao == 'Corolla':
    diaria = 200

elif opcao == 'Porsche':
    diaria = 3500

elif opcao == 'Toro':
    diaria = 1500

elif opcao == 'Fusca':
    diaria = 1200


if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')