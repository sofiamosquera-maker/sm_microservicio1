# app_a.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/all', methods=['GET'])
def call_app_b():
    try:
        
        response = requests.get('http://mi-servicio-backend-mservice.sofia-mosquera-dev.svc.cluster.local:4000/all')
        return f'{response.text}', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500

@app.route('/health', methods=['GET'])
def call_health():
    return 'OK', 200

@app.route('/startup', methods=['GET'])
def call_startup():
    return 'OK', 200
    
@app.route('/readiness', methods=['GET'])
def call_readiness():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
