from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY
from prometheus_client.exposition import basic_auth_handler
import random
import time

# Создание Flask-приложения
app = Flask(__name__)

# Метрики Prometheus
REQUESTS = Counter('app_requests_total', 'Total number of requests')
REQUEST_LATENCY = Histogram('app_request_duration_seconds', 'Request duration in seconds')

# Эндпоинт для получения метрик
@app.route('/metrics')
def metrics():
    # Генерация метрик в формате, понятном Prometheus
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; version=0.0.4'}

# Эндпоинт для обработки GET и POST запросов
@app.route('/data', methods=['GET', 'POST'])
@REQUEST_LATENCY.time()  # Засекаем время обработки
def data():
    # Увеличиваем счётчик запросов
    REQUESTS.inc()

    if request.method == 'GET':
        # Обработка GET запроса
        name = request.args.get('name', 'World')
        return jsonify({"message": f"Hello, {name}!"})

    elif request.method == 'POST':
        # Обработка POST запроса
        data = request.get_json()
        if data:
            name = data.get('name', 'Unknown')
            lastname = data.get('lastname', 'Unknown')
            return jsonify({"message": f"Welcome, {name} {lastname}!"})
        else:
            return jsonify({"error": "Invalid JSON data"}), 400

    else:
        return jsonify({"error": "Method not allowed"}), 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
