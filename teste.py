import pandas as pd

# Carregar os dados
data = pd.read_csv('dados_madeireira.csv')

# Filtrar as transações de venda para o produto Pinus
vendas_pinus = data[(data['tipo_transacao'] == 'Venda') & (data['produto'] == 'Pinus')]

# Contar a quantidade total de vendas de Pinus
quantidade_vendas_pinus = vendas_pinus['quantidade'].sum()

print(f"Quantidade de vendas de Pinus: {quantidade_vendas_pinus}")

# Filtrar as transações de venda para o produto Cedro
vendas_cedro = data[(data['tipo_transacao'] == 'Venda') & (data['produto'] == 'Cedro')]

# Contar a quantidade total de vendas de Cedro
quantidade_vendas_cedro = vendas_cedro['quantidade'].sum()

print(f"Quantidade de vendas de Cedro: {quantidade_vendas_cedro}")

# filtrar as transações de venda para  o produto Compensado
vendas_compensado = data[(data['tipo_transacao'] == 'Venda') & (data['produto'] == 'Compensado')]

# Contar a quantidade total de vendas de Compensado
quantidade_vendas_compensado = vendas_compensado['quantidade'].sum()

print(f"Quantidade de vendas de Compensado: {quantidade_vendas_compensado}")

# Filtrar as transações de venda para o produto Eucalipto
vendas_eucalipto = data[(data['tipo_transacao'] == 'Venda') & (data['produto'] == 'Eucalipto')]

# Contar a quantidade total de vendas de Eucalipto
quantidade_vendas_eucalipto = vendas_eucalipto['quantidade'].sum()

print(f"Quantidade de vendas de Eucalipto: {quantidade_vendas_eucalipto}")

# Filtrar as transações de venda para o produto MDF
vendas_mdf = data[(data['tipo_transacao'] == 'Venda') & (data['produto'] == 'mdf')]

# Contar a quantidade total de vendas de MDF
quantidade_vendas_mdf = vendas_mdf['quantidade'].sum()

print(f"Quantidade de vendas de MDF: {quantidade_vendas_mdf}")


