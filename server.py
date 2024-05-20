from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json
    # Procesa los datos recibidos
    # Realiza alguna acción con los datos
    print("Datos recibidos:", data)
    return jsonify({'message': 'Datos recibidos correctamente desde mi lap'})

if __name__ == '__main__':
    app.run(host='10.182.1.177', port=5000)
