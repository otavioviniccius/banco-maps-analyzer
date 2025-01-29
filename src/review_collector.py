import googlemaps
import json
import os
import sys
import time

# Adicionar o caminho do diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importando a chave da API do arquivo api_config.py
try:
    from src.api_config import API_KEY
except ImportError:
    print("Erro: O arquivo api_config.py não foi encontrado ou a variável API_KEY não está definida.")
    sys.exit(1)

# Configurando o cliente Google Maps
gmaps = googlemaps.Client(key=API_KEY)

# Caminho do arquivo de entrada com os dados das agências
input_file = os.path.join("data", "raw", "agencias_sao_paulo.json")
output_file = os.path.join("data", "raw", "avaliacoes_agencias.json")

# Verificar se o arquivo de entrada existe
if not os.path.exists(input_file):
    print(f"Erro: O arquivo {input_file} não foi encontrado. Execute primeiro data_collector.py")
    sys.exit(1)

# Carregar os dados das agências
with open(input_file, "r", encoding="utf-8") as f:
    agencias = json.load(f)

# Lista para armazenar as avaliações detalhadas
avaliacoes_agencias = []

# Percorrer as agências e buscar as avaliações detalhadas
for agencia in agencias:
    place_id = agencia.get("place_id")
    if not place_id:
        continue

    try:
        details = gmaps.place(place_id=place_id, fields=["name", "reviews"])
        
        if "result" in details and "reviews" in details["result"]:
            avaliacoes = details["result"]["reviews"]
            avaliacoes_agencias.append({
                "nome": agencia["name"],
                "endereco": agencia["vicinity"],
                "avaliacoes": avaliacoes
            })
        
        # Evitar excesso de requisições
        time.sleep(2)
        
    except Exception as e:
        print(f"Erro ao buscar avaliações para {agencia['name']}: {e}")

# Salvar as avaliações em um arquivo JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(avaliacoes_agencias, f, ensure_ascii=False, indent=4)

print(f"Avaliações detalhadas salvas em {output_file}")
