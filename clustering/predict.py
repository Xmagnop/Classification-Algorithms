import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Função para carregar o modelo treinado (centros dos clusters) e o scaler


def load_model():
  with open('clustering/fcm_model.pkl', 'rb') as f:
    cntr, scaler = pickle.load(f)
  return cntr, scaler

# Função de predição para identificar o segmento


def predict_segment(produtos):
  # Preencher com zeros para garantir que tenhamos 10 features
  produtos_completos = produtos + [0] * (10 - len(produtos))

  # Carregar o modelo treinado e o scaler
  cntr, scaler = load_model()

  # Escalar os dados de entrada
  scaled_data = scaler.transform([produtos_completos])

  # Calcular as distâncias entre o cliente e os centros dos clusters
  distancias = np.linalg.norm(scaled_data - cntr, axis=1)

  # Identificar o cluster mais próximo
  segmento = np.argmin(distancias)

  # Definindo os nomes dos clusters
  clusters = ['Gamer', 'Escritório', 'Desenvolvedor', 'Designer', 'Casual']

  return clusters[segmento]
