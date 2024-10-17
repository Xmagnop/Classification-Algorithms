from flask import Flask, render_template, request, jsonify
from clustering.predict import predict_segment
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segmentar', methods=['POST'])
def segmentar():
    produtos = request.json.get('produtos', [])
    segmento = predict_segment(produtos)
    return jsonify({'segmento': segmento})

if __name__ == '__main__':
    app.run(debug=True)
