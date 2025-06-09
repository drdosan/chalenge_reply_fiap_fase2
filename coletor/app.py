from flask import Flask, request
from flasgger import Swagger
import csv
from datetime import datetime

app = Flask(__name__)
swagger = Swagger(app)

CSV_FILE = "leituras_siap.csv"

# Garante o cabeçalho se o CSV ainda não existe
with open(CSV_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "temperatura", "umidade", "vibracao"])

@app.route("/coletar", methods=["POST"])
def coletar():
    """
    Coletar dados do ESP32
    ---
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - temperatura
            - umidade
            - vibracao
          properties:
            temperatura:
              type: number
              example: 24.5
            umidade:
              type: number
              example: 55.0
            vibracao:
              type: integer
              example: 2345
    responses:
      200:
        description: Dados salvos com sucesso
    """
    dados = request.get_json()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            dados.get("temperatura"),
            dados.get("umidade"),
            dados.get("vibracao")
        ])

    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
