# Análise de Avaliações de Agências Bancárias

Este projeto coleta e analisa as avaliações de agências bancárias usando a API do Google Maps. A análise inclui a identificação de palavras-chave, classificação das melhores e piores agências, além de um dashboard no Power BI e Excel para visualização. Também foi implementada uma análise de sentimentos para determinar se as avaliações são positivas, neutras ou negativas.

## Funcionalidades

- Coleta de dados de agências bancárias através da API do Google Maps.
- Análise das avaliações, identificando palavras-chave.
- Geração de rankings das melhores e piores agências.
- Implementação de filtro para visualizar avaliações de um banco específico.
- Análise de sentimentos (positiva, neutra ou negativa) nas avaliações.

## Tecnologias Usadas

- Python
  - Bibliotecas: `requests`, `pandas`, `json`, `nltk`, `textblob`, etc.
- Power BI
- Excel
- API do Google Maps
- API de Análise de Sentimentos (opcional)

## Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/otavioviniccius/banco-maps-analyzer.git
2. Rodar no terminal:
   ```bash
   python src/filter_bank_reviews.py
