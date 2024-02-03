"""
Density-based spatial clustering of applications with noise (DBSCAN)
"""
from matplotlib import pyplot
from pandas import DataFrame
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons


dataset = pd.DataFrame({
    'x': [11, 11, 20, 12, 16, 33, 24, 14, 45, 52, 51, 52, 55, 53,
          55, 61, 62, 70, 72, 10],
    'y': [39, 36, 30, 52, 53, 46, 55, 59, 12, 15, 16, 18, 11, 23,
          14, 8, 18, 7, 24, 70]
})


dbscan = DBSCAN(eps=0.05, min_samples=5)

dbscan.fit(dataset)

# generate 2D classification dataset

X, y = make_moons(n_samples=1000, noise=0.05)

# scatter plot, dots colored by class value

df = DataFrame (dict (x=X[:,0], y=X[:,1], label=y))

colors = {0: 'red', 1: 'blue'}

fig, ax = pyplot.subplots()

grouped = df.groupby('label')

for key, group in grouped:
    print(f'type of key ====> {type(key)}')
    print(f'type of group ====> {type(group)}')
    group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])


if __name__ == '__main__':
    pyplot.show()
