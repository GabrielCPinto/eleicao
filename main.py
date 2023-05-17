import networkx as nx
import matplotlib.pyplot as plt
import random
SIZE = 10


def start():
    G = nx.DiGraph()
    for i in range(1, SIZE+1):
        charge = round(random.random()*100, 2)
        G.add_nodes_from([i], id=i, battery=charge)

    return G


def elect_leader(G, leader):

    for i, node in enumerate(G.nodes.data()):

        if i + 1 != leader['id']:
            pass
            G.add_edge(node[1]['id'], leader['id'])


def choose_leader(G):
    lst = []
    for node in G.nodes.data():
        lst.append(node[1])

    leader = max(lst, key=lambda x: x['battery'])
    return leader


def main():
    G = start()

    elect_leader(G, choose_leader(G))
    nx.draw(G, with_labels=True)
    plt.show()


main()
