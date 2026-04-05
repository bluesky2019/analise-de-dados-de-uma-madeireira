import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dados_madeireira(num_transacoes=1000):
    np.random.seed(42)  # Para resultados reproduzíveis

    produtos = ["Pinus", "Eucalipto", "MDF", "Compensado", "Cedro"]
    clientes_fornecedores = ["Cliente A", "Cliente B", "Fornecedor X", "Fornecedor Y", "Cliente C", "Fornecedor Z"]
    vendedores = ["João", "Maria", "Carlos", "Ana"]
    regioes = ["Sul", "Sudeste", "Centro-Oeste", "Nordeste"]

    # Preço base de compra por produto (custo de aquisição)
    preco_compra_base = {
        "Pinus":      {"min": 50,  "max": 200},
        "Eucalipto":  {"min": 60,  "max": 220},
        "MDF":        {"min": 80,  "max": 250},
        "Compensado": {"min": 70,  "max": 230},
        "Cedro":      {"min": 100, "max": 300},
    }

    # Margem de lucro por produto (entre 20% e 50% acima do preço de compra)
    margem_lucro = {
        "Pinus":      {"min": 0.20, "max": 0.40},
        "Eucalipto":  {"min": 0.20, "max": 0.40},
        "MDF":        {"min": 0.25, "max": 0.50},
        "Compensado": {"min": 0.25, "max": 0.45},
        "Cedro":      {"min": 0.30, "max": 0.50},
    }

    dados = []
    data_inicio = datetime(2015, 1, 1)
    data_fim = datetime(2025, 12, 31)

    for _ in range(num_transacoes):
        data = data_inicio + timedelta(days=np.random.randint(0, (data_fim - data_inicio).days))
        tipo_transacao = np.random.choice(["Venda", "Compra"])
        produto = np.random.choice(produtos)
        quantidade = np.random.randint(1, 100)
        cliente_fornecedor = np.random.choice(clientes_fornecedores)
        vendedor = np.random.choice(vendedores) if tipo_transacao == "Venda" else None
        regiao = np.random.choice(regioes)
        custo_frete = np.random.uniform(10, 100) if np.random.rand() < 0.3 else 0

        # Preço de compra baseado no produto
        preco_compra = np.random.uniform(
            preco_compra_base[produto]["min"],
            preco_compra_base[produto]["max"]
        )

        # Preço de venda = preço de compra + margem de lucro
        margem = np.random.uniform(
            margem_lucro[produto]["min"],
            margem_lucro[produto]["max"]
        )
        preco_venda = preco_compra * (1 + margem)

        # Atribui o preço correto conforme o tipo da transação
        preco_unitario = preco_venda if tipo_transacao == "Venda" else preco_compra

        dados.append([data, tipo_transacao, produto, quantidade, round(preco_unitario, 2),
                       cliente_fornecedor, vendedor, regiao, round(custo_frete, 2)])

    df = pd.DataFrame(dados, columns=["data", "tipo_transacao", "produto", "quantidade",
                                       "preco_unitario", "cliente/fornecedor", "vendedor",
                                       "regiao", "custo_frete"])
    df.to_csv("dados_madeireira.csv", index=False)
    return df

df_madeireira = gerar_dados_madeireira()
print("Base de dados gerada com sucesso!")

# Resumo financeiro para conferência
import pandas as pd
df = pd.read_csv("dados_madeireira.csv")
vendas = df[df['tipo_transacao'] == 'Venda']
compras = df[df['tipo_transacao'] == 'Compra']
total_vendas = (vendas['quantidade'] * vendas['preco_unitario']).sum()
total_compras = (compras['quantidade'] * compras['preco_unitario']).sum()
print(f"Total de Vendas:  R$ {total_vendas:,.2f}")
print(f"Total de Compras: R$ {total_compras:,.2f}")
print(f"Lucro Bruto:      R$ {(total_vendas - total_compras):,.2f}")
