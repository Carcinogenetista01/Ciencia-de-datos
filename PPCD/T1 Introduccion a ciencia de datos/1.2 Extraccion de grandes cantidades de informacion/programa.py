# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc

# Cargar y preprocesar los datos
url = 'https://bit.ly/2COHM14'
data = pd.read_csv(url)
data_scaled = normalize(data)
data_scaled = pd.DataFrame(data_scaled, columns=data.columns)


# Función para crear dendrogramas
def plot_dendrogram(data, linkage_method):
    plt.figure(figsize=(16, 9))
    plt.title(f'Dendrograma ({linkage_method})')
    dend = shc.dendrogram(shc.linkage(data, method=linkage_method))
    plt.show()


# Función para realizar clustering y visualizar resultados
def perform_clustering(data, n_clusters, metric, linkage):
    ac = AgglomerativeClustering(n_clusters=n_clusters, metric=metric, linkage=linkage)
    y_hat = ac.fit_predict(data)

    plt.figure(figsize=(10, 7))
    plt.scatter(data.Milk, data.Grocery, c=y_hat, s=50, cmap='viridis')
    plt.title(f'Clustering (metric: {metric}, linkage: {linkage})')
    plt.show()


# Distancia Euclidiana (original)
plot_dendrogram(data_scaled, 'ward')
perform_clustering(data_scaled, 2, 'euclidean', 'ward')

# Distancia Manhattan
plot_dendrogram(data_scaled, 'single')
perform_clustering(data_scaled, 2, 'manhattan', 'single')

# Distancia Coseno
plot_dendrogram(data_scaled, 'complete')
perform_clustering(data_scaled, 2, 'cosine', 'complete')

# Enlazamiento promedio (average)
plot_dendrogram(data_scaled, 'average')
perform_clustering(data_scaled, 2, 'euclidean', 'average')