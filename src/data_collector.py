import googlemaps
import json
import os
import sys  # Adicionando a importação do sys

# Adicionar o caminho do diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Sua chave de API do Google Maps
gmaps = googlemaps.Client(key='AIzaSyDUpEaANRt3H8GD_pz_wUQn43LmfBPFoXY')

location = '-23.550520, -46.633308'  # Coordenadas de São Paulo, SP
place_type = 'bank'  # Tipo de lugar, por exemplo, 'bank' para agências bancárias

# Realize a busca
places_result = gmaps.places_nearby(location=location, radius=5000, type=place_type)

# Verifique se a chave 'results' existe na resposta
if 'results' in places_result:
        # Criar diretório de saída, se não existir
        output_dir = os.path.join("data", "raw")
        os.makedirs(output_dir, exist_ok=True)
    
        # Caminho do arquivo JSON de saída
        output_file = os.path.join(output_dir, "agencias_sao_paulo.json")

        # Salvar os resultados em um arquivo JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(places_result['results'], f, ensure_ascii=False, indent=4)
        print(f"Dados salvos em: {output_file}")
        # Exiba os resultados
        for place in places_result['results']:
            print(f"Nome: {place['name']}")
            print(f"Endereço: {place['vicinity']}")
            print(f"Rating: {place.get('rating', 'N/A')}")
            print('-' * 40)
else:
    print("Nenhum resultado encontrado ou erro na resposta da API.")