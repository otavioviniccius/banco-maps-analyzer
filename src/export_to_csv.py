import json
import os
import pandas as pd
from textblob import TextBlob
import nltk

# Baixar recursos do nltk
nltk.download('punkt')

# Caminho do arquivo de avaliações
data_file = os.path.join("data", "raw", "avaliacoes_agencias.json")
output_csv = os.path.join("data", "processed", "avaliacoes_sentimentos.csv")

# Verificar se o arquivo existe
if not os.path.exists(data_file):
    print(f"Erro: O arquivo {data_file} não foi encontrado.")
    exit(1)

# Carregar as avaliações
with open(data_file, "r", encoding="utf-8") as f:
    avaliacoes_agencias = json.load(f)

# Lista para armazenar os dados processados
dados = []

# Função para analisar sentimento
def analisar_sentimento(texto):
    if not texto:
        return "Neutro"
    analysis = TextBlob(texto)
    polaridade = analysis.sentiment.polarity
    if polaridade > 0:
        return "Positivo"
    elif polaridade < 0:
        return "Negativo"
    else:
        return "Neutro"

# Processar cada agência
for agencia in avaliacoes_agencias:
    nome = agencia["nome"]
    endereco = agencia["endereco"]
    avaliacoes = agencia.get("avaliacoes", [])
    
    for avaliacao in avaliacoes:
        texto = avaliacao.get("text", "")
        nota = avaliacao.get("rating", 0)
        sentimento = analisar_sentimento(texto)
        
        dados.append([nome, endereco, nota, texto, sentimento])

# Criar um DataFrame e salvar como CSV
df = pd.DataFrame(dados, columns=["Banco", "Endereço", "Nota", "Avaliação", "Sentimento"])
df.to_csv(output_csv, index=False, encoding="utf-8-sig")

print(f"Arquivo CSV gerado: {output_csv}")
