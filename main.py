import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregar os dados
df = pd.read_csv("area-preco.csv")

# Criar o modelo de regressão linear
modelo = LinearRegression()
X = df[["Area"]]
y = df["Preco"]

# Treinar o modelo
modelo.fit(X, y)

# Configuração do título e layout
st.title("Previsão de Preço de Imóvel")
st.write("Utilize o modelo de regressão linear para prever o preço de um imóvel com base na sua área.")

# Divisor
st.divider()

# Entrada do usuário
area = st.number_input("Digite a área do imóvel (em metros quadrados): ", min_value=0.0)

# Previsão e exibição do resultado
if area > 0:
    preco_previsto = modelo.predict([[area]])[0]
    st.write(f"O preço previsto para um imóvel com área de {area:.2f} m² é: R$ {preco_previsto:.2f}")
else:
    st.write("Por favor, insira uma área válida.")
