import json
import os
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Baixar stopwords se necessário
nltk.download('stopwords')
nltk.download('punkt')

# Definir idioma das stopwords
stop_words = set(stopwords.words('portuguese'))

# Caminho do arquivo de avaliações
data_file = os.path.join("data", "raw", "avaliacoes_agencias.json")

# Verificar se o arquivo existe
if not os.path.exists(data_file):
    print(f"Erro: O arquivo {data_file} não foi encontrado.")
    exit(1)

# Carregar as avaliações
with open(data_file, "r", encoding="utf-8") as f:
    avaliacoes_agencias = json.load(f)

# Lista para armazenar todas as palavras das avaliações
todas_palavras = []
ranking_agencias = []

# Processar cada agência
for agencia in avaliacoes_agencias:
    nome = agencia["nome"]
    endereco = agencia["endereco"]
    avaliacoes = agencia.get("avaliacoes", [])
    
    notas = []
    texto_avaliacoes = []
    
    for avaliacao in avaliacoes:
        texto = avaliacao.get("text", "")
        nota = avaliacao.get("rating", 0)
        
        # Processar texto
        palavras = re.findall(r'\b\w{3,}\b', texto.lower())  # Remover pontuação e pegar palavras com mais de 3 letras
        palavras_filtradas = [p for p in palavras if p not in stop_words]
        todas_palavras.extend(palavras_filtradas)
        texto_avaliacoes.append(texto)
        
        # Coletar notas
        notas.append(nota)
    
    # Calcular a média da agência
    media_nota = sum(notas) / len(notas) if notas else 0
    
    ranking_agencias.append({
        "nome": nome,
        "endereco": endereco,
        "media_nota": media_nota,
        "avaliacoes": texto_avaliacoes
    })

# Identificar palavras mais frequentes
palavras_mais_comuns = Counter(todas_palavras).most_common(20)

# Ordenar agências pelo ranking
ranking_agencias.sort(key=lambda x: x["media_nota"], reverse=True)

# Top 5 melhores e piores agências
top_melhores = ranking_agencias[:5]
top_piores = ranking_agencias[-5:]

# Exibir resultados
print("🔹 Palavras mais frequentes nas avaliações:")
for palavra, freq in palavras_mais_comuns:
    print(f"{palavra}: {freq}")

print("\n🏆 Top 5 Melhores Agências:")
for agencia in top_melhores:
    print(f"{agencia['nome']} - Média: {agencia['media_nota']:.2f}")

print("\n⚠️ Top 5 Piores Agências:")
for agencia in top_piores:
    print(f"{agencia['nome']} - Média: {agencia['media_nota']:.2f}")
