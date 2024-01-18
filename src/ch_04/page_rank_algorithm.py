import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


my_web = nx.DiGraph()

# Changed to 6 since you had 5 pages from 1 to 5
my_pages = range(1, 6)

connections = [(1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 4), (4, 5), (5, 1), (5, 4), (4, 1)]

my_web.add_nodes_from(my_pages)

my_web.add_edges_from(connections)

pos = nx.shell_layout(my_web)

nx.draw(my_web, pos, arrows=True, with_labels=True)


def create_page_rank(a_graph):
    nodes_set = len(a_graph)
    M = nx.to_numpy_array(a_graph)

    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array([1.0 / count if count > 0 else 0.0 for count in outwards])

    G = np.asarray(np.multiply(M.T, prob_outwards))
    p = np.ones(nodes_set) / float(nodes_set)
    return G, p


if __name__ == '__main__':
    G, p = create_page_rank(my_web)
    print(G)
    plt.show()
