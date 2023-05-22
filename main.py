import networkx as nx
import matplotlib.pyplot as plt
import random
SIZE = 10


def start():
    G = nx.DiGraph()
    for i in range(1, SIZE+1):
        charge = round(random.random()*100, 2)
        G.add_nodes_from([i], id=i, battery=charge, alive='yes')
    return G


def link_leader(G, leader):
    for i, node in enumerate(G.nodes.data()):
        if i + 1 != leader['id'] and node[1]['alive'] == 'yes':
            G.add_edge(node[1]['id'], leader['id'])


def choose_leader(G):
    lst = []
    for node in G.nodes.data():
        lst.append(node[1])
    leader = max(lst, key=lambda x: x['battery'])
    return leader


def func(x):
    return x['battery']


def send_message(G, sender):
    lst = []
    for node in G.nodes.data():
        if float(sender['battery']) < float(node[1]['battery']):
            if node[1]['alive'] == 'yes':
                lst.append(node[1])

    lst.sort(key=lambda x: x['battery'])
    if len(lst) > 1:
        return send_message(G, lst[0])
    else:
        return lst[0]


def main():
    G = start()
    leader = choose_leader(G)
    leader['alive'] = 'no'
    #print(G.nodes.data())
    x = int(random.randint(1,SIZE))
    new_leader = send_message(G, G.nodes.data()[x])
    #link_leader(G, new_leader)
    if leader['battery'] <= 0:
        leader = choose_leader(G)
    link_leader(G, new_leader)

    nx.draw(G, with_labels=True)
    plt.show()


main()
