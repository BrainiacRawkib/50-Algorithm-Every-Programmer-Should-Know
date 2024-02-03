import numpy as np
import pandas as pd

from sklearn.cluster import AgglomerativeClustering


dataset = pd.DataFrame({
    'x': [11, 11, 20, 12, 16, 33, 24, 14, 45, 52, 51, 52, 55, 53,
          55, 61, 62, 70, 72, 10],
    'y': [39, 36, 30, 52, 53, 46, 55, 59, 12, 15, 16, 18, 11, 23,
          14, 8, 18, 7, 24, 70]
})

cluster = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')

cluster.fit_predict(dataset)


if __name__ == '__main__':
    print(cluster.labels_)
