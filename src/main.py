from src.data_collector import buscar_agencias_bancarias

if __name__ == "__main__":
    localizacao = "São Paulo, Brasil"
    raio = 5000  # Raio de busca em metros
    agencias = buscar_agencias_bancarias(localizacao, raio)

    for agencia in agencias:
        print(f"Nome: {agencia['name']}, Endereço: {agencia.get('vicinity', 'Não disponível')}")
