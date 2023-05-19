import networkx as nx
import matplotlib.pyplot as plt
import random
from multiprocessing import Process
import threading
import os
import time
import zmq
import sys
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
            G.add_edge(node[1]['id'], leader['id'])


def choose_leader(G):
    lst = []
    for node in G.nodes.data():
        lst.append(node[1])

    leader = max(lst, key=lambda x: x['battery'])
    return leader


def receive_election_message(G, leader, sender):
    msg = str(sender['id'])
    if sender['battery'] > leader['battery']:
        print(f'Node {msg} sends OK')


def main():
    G = start()
    leader = choose_leader(G)
    print(G.nodes.data()[1])
    receive_election_message(G, leader, G.nodes.data()[1])
    if leader['battery'] <= 0:
        leader = choose_leader(G)
    elect_leader(G, leader)
    nx.draw(G, with_labels=True)
    plt.show()


main()
