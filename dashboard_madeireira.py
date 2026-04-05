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

# Filtro de período por ano
anos_disponiveis = sorted(df["data"].dt.year.unique())
ano_inicio, ano_fim = st.sidebar.select_slider(
    "Período (ano)",
    options=anos_disponiveis,
    value=(anos_disponiveis[0], anos_disponiveis[-1])
)

regiao_filtro = st.sidebar.multiselect("Região", options=df["regiao"].unique(), default=df["regiao"].unique())
produto_filtro = st.sidebar.multiselect("Produto", options=df["produto"].unique(), default=df["produto"].unique())

df_filtrado = df[
    (df["data"].dt.year >= ano_inicio) &
    (df["data"].dt.year <= ano_fim) &
    (df["regiao"].isin(regiao_filtro)) &
    (df["produto"].isin(produto_filtro))
]

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

# Métricas principais — corrigido: quantidade * preco_unitario por linha
st.header("Métricas Principais")
col1, col2, col3 = st.columns(3)

vendas = df_filtrado[df_filtrado['tipo_transacao'] == 'Venda']
compras = df_filtrado[df_filtrado['tipo_transacao'] == 'Compra']

total_vendas = (vendas['quantidade'] * vendas['preco_unitario']).sum()
total_compras = (compras['quantidade'] * compras['preco_unitario']).sum()
lucro_bruto = total_vendas - total_compras

col1.metric("Total de Vendas", f"R$ {total_vendas:,.2f}")
col2.metric("Total de Compras", f"R$ {total_compras:,.2f}")
col3.metric("Lucro Bruto", f"R$ {lucro_bruto:,.2f}")

# Gráficos
st.header("Visualizações")

# Vendas por produto
vendas_produto = vendas.groupby("produto")["quantidade"].sum().reset_index()
fig_vendas_produto = px.bar(vendas_produto, x="produto", y="quantidade", title="Vendas por Produto")

for i, row in vendas_produto.iterrows():
    fig_vendas_produto.add_annotation(
        x=row["produto"],
        y=row["quantidade"],
        text=str(row["quantidade"]),
        showarrow=False,
        yshift=10
    )

st.plotly_chart(fig_vendas_produto, width='stretch')

# Compras por fornecedor
compras_fornecedor = compras.groupby("cliente/fornecedor")["quantidade"].sum().reset_index()
fig_compras_fornecedor = px.bar(compras_fornecedor, x="cliente/fornecedor", y="quantidade", title="Compras por Fornecedor")
st.plotly_chart(fig_compras_fornecedor, width='stretch')

# Vendas por região
vendas_regiao = vendas.groupby("regiao")["quantidade"].sum().reset_index()
fig_vendas_regiao = px.pie(vendas_regiao, names="regiao", values="quantidade", title="Vendas por Região")
st.plotly_chart(fig_vendas_regiao, width='stretch')

# Evolução das vendas ao longo do tempo
vendas_tempo = vendas.groupby(pd.Grouper(key="data", freq="ME"))["quantidade"].sum().reset_index()
fig_vendas_tempo = px.line(vendas_tempo, x="data", y="quantidade", title="Evolução das Vendas ao Longo do Tempo")
st.plotly_chart(fig_vendas_tempo, width='stretch')
