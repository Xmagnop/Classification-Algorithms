# Classification-Algorithms

O intuito deste repositório é o projeto da matéria de Tópicos avançados em inteligências computacional, dessa maneira dentre os arquivos estão as apresentações e a nossa aplicação utilizando o algoritmo de Fuzzy C-Means para realizar a segmentação de clientes com base em suas compras de produtos específicos. A aplicação tem uma interface onde o cliente pode montar um carrinho de compras e, ao finalizar a compra, a aplicação gera uma segmentação com base nos produtos selecionados. O modelo de Fuzzy C-Means foi treinado previamente em dados fictícios e os pesos salvos desse modelo são utilizados para gerar os segmentos no frontend.

## Funcionamento

A aplicação consiste em duas partes principais:

- Treinamento e Armazenamento do Modelo: Um modelo de Fuzzy C-Means é treinado usando dados simulados de compras. Os centros dos clusters, que representam os pesos de cada produto em relação aos segmentos identificados, são salvos para uso posterior. Esses centros são fundamentais para identificar o segmento de um cliente a partir dos produtos em seu carrinho.

- Predição do Segmento no Frontend: A interface web permite que o usuário monte um carrinho com diversos produtos. Ao finalizar a compra, o backend utiliza os pesos salvos do modelo treinado para comparar o carrinho com os segmentos definidos. Essa comparação gera o segmento do cliente, que é então retornado e exibido para o usuário.

## Tecnologias Utilizadas

- Backend: Python com Flask
- Algoritmo de Segmentação: Fuzzy C-Means (utilizando scikit-fuzzy)
- Bibliotecas de Machine Learning: scikit-learn para escalonamento dos dados
- Frontend: HTML, CSS, JavaScript
- Serialização de Dados: pickle para salvar o modelo treinado

## Estrutura de Pastas

```
.
├── app.py                   # Arquivo principal da aplicação Flask
├── clustering
│   ├── training.py          # Script para treinar o modelo
│   ├── predict.py           # Script para prever o segmento do cliente
│   └── fcm_model.pkl        # Modelo treinado com Fuzzy C-Means
├── data
│   └── compras.csv          # Dados fictícios de compras para o treinamento
├── static
│   └── styles.css           # Estilos para o frontend
├── templates
│   └── index.html           # Interface principal do cliente
└── README.md                # Documentação do projeto
```

## Instalação de Dependências

```
pip install -r requirements.txt
```

## Subir Aplicação do Front

```
python app.py
```

## Uso Da Aplicação do Front

- Catálogo e Carrinho de Compras:
  - A interface exibe um catálogo com produtos como Mouse, Teclado, Cadeira, Monitor, etc.
  - O usuário pode adicionar produtos ao carrinho, ver os itens e suas quantidades, podendo adicionar quantidades adicionais de um mesmo produto.

- Finalizar Compra e Ver Segmento:
  - Ao finalizar a compra, o frontend envia os produtos do carrinho para o backend, onde o modelo Fuzzy C-Means realiza a segmentação.
  - O backend utiliza o modelo treinado para determinar a probabilidade de associação do cliente a cada segmento, considerando os produtos e suas respectivas quantidades.
