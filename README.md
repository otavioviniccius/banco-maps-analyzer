# Banco Maps Analyzer

## 📌 Sobre o Projeto

Este projeto coleta dados de agências bancárias usando a API do Google Maps, analisa suas avaliações e identifica problemas recorrentes. Os dados são organizados e exportados para visualização em Power BI e Excel.

## 🚀 Funcionalidades

- Busca automática de agências bancárias.
- Coleta de avaliações detalhadas e notas.
- Análise de sentimentos (positivo, neutro ou negativo) nas avaliações.
- Exportação de dados para CSV.
- Dashboard interativo no Power BI e Excel.
- Filtro para visualizar avaliações de um banco específico.

## 🛠️ Tecnologias Utilizadas

- **Python** (pandas, googlemaps, vaderSentiment)
- **Google Maps API** (coleta de dados)
- **Power BI / Excel** (visualização de dados)

## 📦 Estrutura do Projeto

```
banco-maps-analyzer/
├── data/
│   ├── raw/              # Dados brutos coletados da API
│   ├── processed/        # Dados processados
├── notebooks/            # Notebooks Jupyter para análises
├── src/                  # Código-fonte do projeto
│   ├── main.py           # Script principal
│   ├── api_config.py     # Configuração da API
│   ├── data_collector.py # Coleta de dados
│   ├── analyzer.py       # Processamento e análise de dados
│   ├── export_to_csv.py  # Exportação para CSV
│   ├── filter_bank_reviews.py  # Filtro para bancos específicos
├── tests/                # Testes unitários
├── .gitignore            # Arquivo para ignorar arquivos no Git
├── README.md             # Documentação do projeto
├── requirements.txt      # Dependências
└── LICENSE
```

## 🔧 Como Configurar e Executar

### 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar a API do Google Maps

- Criar um arquivo **api\_config.py** na pasta **src/**.
- Inserir sua chave da API:
  ```python
  API_KEY = "SUA_CHAVE_AQUI"
  ```

### 3️⃣ Coletar Dados das Agências Bancárias

```bash
python src/data_collector.py
```

### 4️⃣ Analisar Sentimentos e Exportar CSV

```bash
python src/export_to_csv.py
```

### 5️⃣ Filtrar Avaliações de um Banco Específico

```bash
python src/filter_bank_reviews.py
```

## 📊 Visualização no Power BI / Excel

- **Importe o CSV** gerado em `data/processed/avaliacoes_sentimentos_vader.csv`.
- **Crie gráficos interativos** (notas médias, sentimentos, palavras mais citadas).

## 📝 Licença

Este projeto está sob a licença MIT.

