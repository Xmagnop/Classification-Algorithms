import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from skfuzzy import cmeans

# Nome dos produtos e seus segmentos correspondentes
produtos = [
    'Mouse', 'Teclado', 'Cadeira', 'Monitor', 'Placa de Vídeo',
    'Headset', 'Microfone', 'Mesa Gamer', 'Cabo HDMI', 'Webcam'
]

# Simulação de dados de treinamento com segmentos associados
dados = {
    'Mouse': [1, 0, 0, 0, 0],
    'Teclado': [1, 0, 0, 0, 0],
    'Cadeira': [1, 1, 0, 0, 0],
    'Monitor': [1, 1, 1, 0, 0],
    'Placa de Vídeo': [0, 1, 0, 1, 0],
    'Headset': [0, 1, 1, 1, 0],
    'Microfone': [0, 0, 1, 1, 1],
    'Mesa Gamer': [0, 0, 1, 1, 1],
    'Cabo HDMI': [0, 0, 0, 0, 1],
    'Webcam': [0, 0, 0, 0, 1],
}

data = pd.DataFrame.from_dict(dados, orient='index')
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

num_clusters = 5
cntr, u, u0, d, jm, p, fpc = cmeans(scaled_data.T, num_clusters, 2, error=0.005, maxiter=1000)

# Salvar o modelo treinado
np.savez('modelo_fuzzy_cmeans.npz', cntr=cntr)

print("Modelo treinado e salvo com sucesso!")
