import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados_madeireira.csv")
df["data"] = pd.to_datetime(df["data"])

# Configuração da página
st.set_page_config(page_title="Dashboard Madeireira", layout="wide")

# Título do dashboard
st.title("Análise de Dados da Madeireira")

# Filtros
st.sidebar.header("Filtros")
regiao_filtro = st.sidebar.multiselect("Região", options=df["regiao"].unique(), default=df["regiao"].unique())
produto_filtro = st.sidebar.multiselect("Produto", options=df["produto"].unique(), default=df["produto"].unique())
df_filtrado = df[(df["regiao"].isin(regiao_filtro)) & (df["produto"].isin(produto_filtro))]
st.subheader("Dados Filtrados")
st.dataframe(df_filtrado)
# Verificação adicional das vendas por produto
st.subheader("Verificação de Vendas por Produto")
for produto in df_filtrado["produto"].unique():
    if "Venda" in df_filtrado["tipo_transacao"].unique():
        vendas_produto_verificacao = df_filtrado[(df_filtrado["tipo_transacao"] == "Venda") & (df_filtrado["produto"] == produto)]["quantidade"].sum()
        st.write(f"Vendas de {produto}: {vendas_produto_verificacao}")
    else:
        st.write(f"Não existe vendas para os filtros selecionados")
# Métricas principais
st.header("Métricas Principais")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas", f"R$ {df_filtrado[df_filtrado['tipo_transacao'] == 'Venda']['quantidade'].sum() * df_filtrado[df_filtrado['tipo_transacao'] == 'Venda']['preco_unitario'].mean():.2f}")
col2.metric("Total de Compras", f"R$ {df_filtrado[df_filtrado['tipo_transacao'] == 'Compra']['quantidade'].sum() * df_filtrado[df_filtrado['tipo_transacao'] == 'Compra']['preco_unitario'].mean():.2f}")
col3.metric("Lucro Bruto", f"R$ {(df_filtrado[df_filtrado['tipo_transacao'] == 'Venda']['quantidade'].sum() * df_filtrado[df_filtrado['tipo_transacao'] == 'Venda']['preco_unitario'].mean()) - (df_filtrado[df_filtrado['tipo_transacao'] == 'Compra']['quantidade'].sum() * df_filtrado[df_filtrado['tipo_transacao'] == 'Compra']['preco_unitario'].mean()):.2f}")

# Gráficos
st.header("Visualizações")

# Vendas por produto
vendas_produto = df_filtrado[df_filtrado["tipo_transacao"] == "Venda"].groupby("produto")["quantidade"].sum().reset_index()
fig_vendas_produto = px.bar(vendas_produto, x="produto", y="quantidade", title="Vendas por Produto")

# Adicionar anotações com os valores exatos
for i, row in vendas_produto.iterrows():
    fig_vendas_produto.add_annotation(
        x=row["produto"],
        y=row["quantidade"],
        text=str(row["quantidade"]),
        showarrow=False,
        yshift=10
    )

st.plotly_chart(fig_vendas_produto, use_container_width=True)# Compras por fornecedor
compras_fornecedor = df_filtrado[df_filtrado["tipo_transacao"] == "Compra"].groupby("cliente/fornecedor")["quantidade"].sum().reset_index()
fig_compras_fornecedor = px.bar(compras_fornecedor, x="cliente/fornecedor", y="quantidade", title="Compras por Fornecedor")
st.plotly_chart(fig_compras_fornecedor, use_container_width=True)

# Vendas por região
vendas_regiao = df_filtrado[df_filtrado["tipo_transacao"] == "Venda"].groupby("regiao")["quantidade"].sum().reset_index()
fig_vendas_regiao = px.pie(vendas_regiao, names="regiao", values="quantidade", title="Vendas por Região")
st.plotly_chart(fig_vendas_regiao, use_container_width=True)

# Evolução das vendas ao longo do tempo
vendas_tempo = df_filtrado[df_filtrado["tipo_transacao"] == "Venda"].groupby(pd.Grouper(key="data", freq="M"))["quantidade"].sum().reset_index()
fig_vendas_tempo = px.line(vendas_tempo, x="data", y="quantidade", title="Evolução das Vendas ao Longo do Tempo")
st.plotly_chart(fig_vendas_tempo, use_container_width=True)