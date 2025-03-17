import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dados_madeireira(num_transacoes=1000):
    np.random.seed(42)  # Para resultados reproduzíveis

    produtos = ["Pinus", "Eucalipto", "MDF", "Compensado", "Cedro"]
    clientes_fornecedores = ["Cliente A", "Cliente B", "Fornecedor X", "Fornecedor Y", "Cliente C", "Fornecedor Z"]
    vendedores = ["João", "Maria", "Carlos", "Ana"]
    regioes = ["Sul", "Sudeste", "Centro-Oeste", "Nordeste"]

    dados = []
    data_inicio = datetime(2020, 1, 1)
    data_fim = datetime(2023, 12, 31)

    for _ in range(num_transacoes):
        data = data_inicio + timedelta(days=np.random.randint(0, (data_fim - data_inicio).days))
        tipo_transacao = np.random.choice(["Venda", "Compra"])
        produto = np.random.choice(produtos)
        quantidade = np.random.randint(1, 100)
        preco_unitario = np.random.uniform(50, 500)
        cliente_fornecedor = np.random.choice(clientes_fornecedores)
        vendedor = np.random.choice(vendedores) if tipo_transacao == "Venda" else None
        regiao = np.random.choice(regioes)
        custo_frete = np.random.uniform(10, 100) if np.random.rand() < 0.3 else 0  # 30% das transações têm frete

        dados.append([data, tipo_transacao, produto, quantidade, preco_unitario, cliente_fornecedor, vendedor, regiao, custo_frete])

    df = pd.DataFrame(dados, columns=["data", "tipo_transacao", "produto", "quantidade", "preco_unitario", "cliente/fornecedor", "vendedor", "regiao", "custo_frete"])
    df.to_csv("dados_madeireira.csv", index=False)
    return df

df_madeireira = gerar_dados_madeireira()
print("Base de dados gerada com sucesso!")