import requests
import json

# Datos a enviar al servidor PHP
data = {
    'message': 'Hola desde Python!'
}

# URL del servidor PHP
url = 'http://localhost:8000/server.php'

# Enviar solicitud POST al servidor PHP con los datos
response = requests.post(url, data=json.dumps(data))

# Imprimir la respuesta del servidor PHP
print(response.text)
