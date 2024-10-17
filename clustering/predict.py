import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carregar o modelo treinado
modelo = np.load('modelo_fuzzy_cmeans.npz')
centros = modelo['cntr']

# Nome dos produtos e seus segmentos correspondentes
produtos = [
    'Mouse', 'Teclado', 'Cadeira', 'Monitor', 'Placa de Vídeo',
    'Headset', 'Microfone', 'Mesa Gamer', 'Cabo HDMI', 'Webcam'
]

def predict_segment(produtos_compra):
    data = np.zeros((1, len(produtos)))
    
    for produto in produtos_compra:
        if produto in produtos:
            idx = produtos.index(produto)
            data[0, idx] = 1
            
    scaled_data = StandardScaler().fit_transform(data)

    # Previsão
    distances = np.linalg.norm(centros[:, None] - scaled_data.T, axis=0)
    cluster = np.argmin(distances)
    
    segmentos = ['Gamer', 'Profissional', 'Estudante', 'Ocasional', 'Tecnológico']
    
    return segmentos[cluster]
