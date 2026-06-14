import streamlit as st
import pandas as pd
st.set_page_config(page_title="Dashboard - Defesa Social", layout="wide")
st.title("🛡️ Painel de Monitoramento - Integração Comunitária")
st.markdown("Projeto desenvolvido para a Avaliação de Python do melhor aluno que existe(eu).")
st.divider()
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('dados_defesa_social.csv')
    return tabela

df = carregar_dados()

st.subheader("Resumo Operacional")
coluna1, coluna2, coluna3 = st.columns(3)

coluna1.metric("Total de Ocorrências", len(df))
coluna2.metric("Bairros Monitorados", df['Bairro'].nunique())
coluna3.metric("Ocorrências Pendentes", len(df[df['Status'] == 'Pendente']))

st.divider()

col_grafico1, col_grafico2 = st.columns(2)

with col_grafico1:
    st.subheader("Ocorrências por Bairro")
    contagem_bairros = df['Bairro'].value_counts()
    st.bar_chart(contagem_bairros)

with col_grafico2:
    st.subheader("Status dos Atendimentos")
    # Usando o Pandas para contar o status
    contagem_status = df['Status'].value_counts()
    st.bar_chart(contagem_status)

st.divider()
st.subheader("Base de Dados Completa")
with st.expander("Clique aqui para visualizar e filtrar a tabela de dados"):
    st.dataframe(df, use_container_width=True)