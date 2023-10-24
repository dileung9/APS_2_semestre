import streamlit as st

def calcular_emissao_carbono(consumo):
    densidade_da_gasolina = 0.75
    fator_de_transformacao = 3.7
    volume_etanol = 0.82
    return float(consumo) * densidade_da_gasolina * fator_de_transformacao * volume_etanol

def calcular_compensacao_carbono(emissao):
    credito = 1000
    return emissao / credito

def calcular_credito_carbono(emissao_de_carbono):
    valor_credito = 26
    return emissao_de_carbono / 1000 * valor_credito

st.title("Calculadora de Carbono")
consumo = st.number_input(label="Consumo semanal de gasolina em Km/litro:", min_value= 0) 
emissao = calcular_emissao_carbono(consumo)
compensacao = calcular_compensacao_carbono(emissao)
st.write("Sua emissão de carbono é: ")
st.write(emissao, "Kg de CO2")
st.write("Você deve comprar esta quantidade de créditos para compensar sua emissão: ")
st.write("R$", compensacao)
st.write("Você pode lucrar essa quantidade com futuras vendas de crédito: ")
st.write("R$",calcular_credito_carbono(emissao))