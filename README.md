# 🌲 Análise de Dados de uma Madeireira

Projeto de análise de dados de uma madeireira fictícia, desenvolvido em Python com o framework Streamlit. O projeto simula transações comerciais (vendas e compras) ao longo de 11 anos (2015–2025) e apresenta os resultados em um dashboard interativo com filtros dinâmicos.

---

## 📋 Funcionalidades

- Geração de base de dados simulada com 1.000 transações
- Preços de venda sempre superiores aos de compra, simulando margem de lucro real por produto
- Dashboard interativo com filtros por **ano**, **região** e **produto**
- Métricas financeiras: Total de Vendas, Total de Compras e Lucro Bruto
- Gráficos de barras, pizza e linha com Plotly
- Script de verificação de vendas por produto

---

## 🗂️ Estrutura do Projeto

```
madeireira/
├── base-de-dados-madeireira.py   # Gerador da base de dados CSV
├── dashboard_madeireira.py       # Dashboard interativo com Streamlit
├── teste.py                      # Script de verificação de vendas por produto
└── dados_madeireira.csv          # Base de dados gerada (criada ao rodar o gerador)
```

---

## ⚙️ Dependências

| Biblioteca | Versão recomendada | Descrição |
|---|---|---|
| Python | 3.8+ | Linguagem base do projeto |
| streamlit | >= 1.30 | Framework para o dashboard |
| pandas | >= 2.2 | Manipulação e análise de dados |
| plotly | >= 5.0 | Geração dos gráficos interativos |
| numpy | >= 1.24 | Geração dos dados simulados |

---

## 🚀 Como Rodar

**1. Clone o repositório**
```bash
git clone https://github.com/bluesky2019/analise-de-dados-de-uma-madeireira
cd analise-de-dados-de-uma-madeireira
```

**2. Crie e ative um ambiente virtual (recomendado)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install streamlit pandas plotly numpy
```

**4. Gere a base de dados**
```bash
python base-de-dados-madeireira.py
```

**5. Rode o dashboard**
```bash
python -m streamlit run dashboard_madeireira.py
```

Acesse no navegador: `http://localhost:8501`

---

## 📊 Sobre os Dados

As transações são geradas aleatoriamente com seed fixo (`numpy.random.seed(42)`), garantindo reprodutibilidade. Cada produto possui faixas de preço de compra e margens de lucro próprias:

| Produto | Preço de Compra | Margem de Lucro |
|---|---|---|
| Pinus | R$ 50 – R$ 200 | 20% a 40% |
| Eucalipto | R$ 60 – R$ 220 | 20% a 40% |
| MDF | R$ 80 – R$ 250 | 25% a 50% |
| Compensado | R$ 70 – R$ 230 | 25% a 45% |
| Cedro | R$ 100 – R$ 300 | 30% a 50% |

---

## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://medium.com/@gilnei809/gilnei-azambuja-borges-analista-de-dados-e-administrador-de-banco-de-dados-8774175b0e46)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gilnei-azambuja-borges-1a83432b)
[![HUGGING FACE](https://img.shields.io/badge/HuggingFace-e5f21d?style=for-the-badge&logo=HuggingFace&logoColor=yellow)](https://huggingface.co/bluesky2019)
[![KAGGLE](https://img.shields.io/badge/Kaggle-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.kaggle.com/gilneiborges)

---

Se você gostou do projeto e gostaria de contribuir com uma doação, eu agradeceria!
[�donate via PayPal](https://www.paypal.com/donate/?hosted_button_id=FW4VNKJWXLTCJ)
