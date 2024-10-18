from flask import Flask, render_template, request, jsonify
from clustering.predict import predict_segment

app = Flask(__name__)

# Página inicial com o carrinho de compras


@app.route('/')
def index():
  return render_template('index.html')

# Rota para segmentar o cliente baseado nos produtos comprados


@app.route('/segmentar', methods=['POST'])
def segmentar():
  produtos = request.json['produtos']
  segmento = predict_segment(produtos)
  return jsonify({'segmento': segmento})


if __name__ == '__main__':
  app.run(debug=True)
