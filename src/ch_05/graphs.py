import networkx as nx


graph = nx.Graph()

graph.add_node('Mike')

graph.add_nodes_from(['Amine', 'Wassim', 'Nick'])

graph.add_edge('Mike', 'Amine')

graph.add_edge('Amine', 'Imran')


if __name__ == '__main__':
    print(graph.nodes)
    print(graph.edges)
