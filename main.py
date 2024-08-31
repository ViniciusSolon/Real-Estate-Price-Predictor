import streamlit as st
import pandas as pd
from sklearn import linear_model

df = pd.read_csv("area-preco.csv")


modelo = linear_model.LinearRegression()
x = df[["Area"]]
y = df[["Preco"]]

modelo.fit(x, y)

st.title("Prevendo o preço por área de imóvel: ")
st.divider()

area = st.number_input("Digite a área do imóvel para obter uma previsão de preço: ")

if area:
    preco_previsto = modelo.predict([[area]])[0][0]
    st.write(f"O preço da área previsto é: R$ {preco_previsto:.2f}")