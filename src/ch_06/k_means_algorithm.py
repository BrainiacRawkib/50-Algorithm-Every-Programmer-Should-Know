"""
k-means algorithm
"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import cluster


dataset = pd.DataFrame({
    'x': [11, 21, 28, 17, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61,
          62, 70, 72, 10],
    'y': [39, 36, 30, 52, 53, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8,
18, 7, 24, 10]
})

kmeans = cluster.KMeans(n_clusters=2)

kmeans.fit(dataset)

labels = kmeans.labels_

centers = kmeans.cluster_centers_


if __name__ == '__main__':
    print(labels)
    print(centers)
    plt.scatter(dataset['x'], dataset['y'], c=labels)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
    plt.show()
