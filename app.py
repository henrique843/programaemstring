from flask import Flask, jsonify

app = Flask(__name__)

# Dados
dataset1 = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722}
    # Adicione os outros dias aqui, se necessário
]

@app.route('/dados/dataset1')
def get_dataset1():
    return jsonify(dataset1)

if __name__ == '__main__':
    app.run(debug=True)