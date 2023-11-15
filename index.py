import streamlit as st

def calcular_emissao_carbono(consumo):
    densidade_da_gasolina = 0.75 #Valor da densidade da gasolina. Fonte: https://esalqlastrop.com.br/capa.asp?pi=calculadora_emissoes#:~:text=Desta%20forma%20o%20c%C3%A1lculo%20fica,kg%20CO2%20emitido%20por%20litro.
    fator_de_transformacao = 3.7 #Valor do fator de transformação de gasolina em CO2. Fonte: https://esalqlastrop.com.br/capa.asp?pi=calculadora_emissoes#:~:text=Desta%20forma%20o%20c%C3%A1lculo%20fica,kg%20CO2%20emitido%20por%20litro.
    volume_etanol = 0.82 #Valor do desconto de volume de etanol que temos na gasolina. Obtendo 82% de gasolina pura. Fonte: https://esalqlastrop.com.br/capa.asp?pi=calculadora_emissoes#:~:text=Desta%20forma%20o%20c%C3%A1lculo%20fica,kg%20CO2%20emitido%20por%20litro.
    return round(float(consumo) * densidade_da_gasolina * fator_de_transformacao * volume_etanol, 2)

def calcular_compensacao_carbono(emissao):
    credito_carbono = 1000 #Valor da tonelada de de carbono. Uma tonelada de carbono vale um credito de carbono. Fonte: https://brasilescola.uol.com.br/geografia/creditos-carbono.htm#:~:text=O%20cr%C3%A9dito%20de%20carbono%20como,carbono%2C%20um%20dos%20principais%20GEE.
    return round(emissao / credito_carbono, 2)

def calcular_credito_carbono(credito):
    valor_credito = float(24.33) #Valor da conversão de 5 dólares americanos para real. Fonte: https://g.co/kgs/poQqXM
    return round(credito * valor_credito, 2)

st.title("Calculadora de Carbono")
consumo = st.number_input(label="Insira o consumo semanal de gasolina em Km/litro:", min_value= 0) 
emissao = calcular_emissao_carbono(consumo)
compensacao = calcular_compensacao_carbono(emissao)
st.write("Sua emissão de carbono é: ")
st.write(emissao, "Kg de CO2")
st.write("Você deve comprar esta quantidade de créditos para compensar sua emissão: ")
st.write("R$", compensacao)
st.write("Você pode lucrar essa quantidade com futuras vendas de crédito: ")
st.write("R$",calcular_credito_carbono(compensacao))
