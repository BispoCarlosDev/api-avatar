import requests

# URL para a requisição
url = "https://last-airbender-api.fly.dev/api/v1/characters"

try:
    # Executa a requisição GET
    response = requests.get(url)

    # Verifica o código de status da resposta
    if response.status_code == 200:
        # Processa o conteúdo da resposta
        data = response.json()  # Converte o JSON da resposta em um objeto Python
        print("Dados recebidos:")
        print(data)
    else:
        print(f"Erro na requisição. Código de status: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")
