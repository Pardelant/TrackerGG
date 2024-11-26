import requests
import json

# Tu API Key
API_KEY = "5e5ae59d-ee0d-4abf-9c1d-71464cbad25f"

# Nombre de usuario (recuerda codificar caracteres especiales como %)
username = "RvS0 #THARD"
platform = "steam"
platformUserIdentifier = "https://steamcommunity.com/id/rvs0/"

# Función para obtener datos del jugador
def get_player_data(username):
    url = f"https://public-api.tracker.gg/v2/csgo/standard/profile/{platform}/{platformUserIdentifier}"
    headers = {"TRN-Api-Key": API_KEY}
    
    # Realiza la solicitud
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Procesa y muestra los datos en caso de éxito
        data = response.json()
        print("Datos del usuario:")
        print(json.dumps(data, indent=4))  # Imprime el JSON con formato
    else:
        # Manejo de errores
        print(f"Error al obtener datos: {response.status_code}")
        print("Mensaje:", response.text)

# Llamada a la función
get_player_data(username)
