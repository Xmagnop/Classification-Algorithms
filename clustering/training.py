import pandas as pd
import numpy as np
from skfuzzy.cluster import cmeans
from sklearn.preprocessing import StandardScaler
import pickle

# Leitura de dados a partir de um CSV de compras


def load_data(filepath):
  data = pd.read_csv(filepath)
  return data

# Treinamento do modelo Fuzzy C-means


def train_fuzzy_cmeans(data):
  scaler = StandardScaler()
  scaled_data = scaler.fit_transform(data)

  num_clusters = 5  # Definindo 5 clusters, por exemplo
  cntr, u, u0, d, jm, p, fpc = cmeans(
      scaled_data.T, num_clusters, 2, error=0.005, maxiter=1000)

  # Salvando o modelo e o scaler
  with open('clustering/fcm_model.pkl', 'wb') as f:
    pickle.dump((cntr, scaler), f)

  print("Modelo Fuzzy C-means treinado e salvo.")


if __name__ == '__main__':
  filepath = 'data/compras.csv'
  data = load_data(filepath)
  train_fuzzy_cmeans(data)
