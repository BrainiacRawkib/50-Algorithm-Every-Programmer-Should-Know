import networkx as nx
import matplotlib.pyplot as plt


vertices = range(1, 10)

edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

graph = nx.Graph()

graph.add_nodes_from(vertices)

graph.add_edges_from(edges)


if __name__ == '__main__':
    # nx.draw(graph, with_labels=True, node_color='y', node_size=800)
    # plt.show()
    print('Degree Centrality:', nx.degree_centrality(graph))
    print('Betweenness Centrality:', nx.betweenness_centrality(graph))
    print('Closeness Centrality:', nx.closeness_centrality(graph))
    eigenvector_centrality = nx.eigenvector_centrality(graph)
    print('Eigenvector Centrality:', eigenvector_centrality)
    sorted_centrality = sorted((vertex, '{:0.2f}'.format(centrality_val)) for vertex, centrality_val in eigenvector_centrality.items())
    print(f'sorted_centrality ==> {sorted_centrality}')
