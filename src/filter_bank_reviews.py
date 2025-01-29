import pandas as pd
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Inicializar o analisador de sentimentos
analyzer = SentimentIntensityAnalyzer()

# Caminho do arquivo CSV
input_csv = os.path.join("data", "processed", "avaliacoes_sentimentos.csv")
output_csv = os.path.join("data", "processed", "avaliacoes_sentimentos_vader.csv")

# Verificar se o arquivo existe
if not os.path.exists(input_csv):
    print(f"Erro: O arquivo {input_csv} não foi encontrado.")
    exit(1)

# Carregar os dados
df = pd.read_csv(input_csv)

# Função para analisar sentimentos com VADER
def analisar_sentimento_vader(texto):
    if not isinstance(texto, str) or texto.strip() == "":
        return "Neutro"
    
    score = analyzer.polarity_scores(texto)
    
    if score['compound'] >= 0.05:
        return "Positivo"
    elif score['compound'] <= -0.05:
        return "Negativo"
    else:
        return "Neutro"

# Aplicar análise de sentimentos
df["Sentimento"] = df["Avaliação"].apply(analisar_sentimento_vader)

# Salvar o novo CSV
df.to_csv(output_csv, index=False, encoding="utf-8-sig")

print(f"Arquivo CSV atualizado com VADER gerado: {output_csv}")
