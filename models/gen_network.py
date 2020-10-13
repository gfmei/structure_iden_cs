#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/13/2020 8:38 PM
# @Author  : Guofeng Mei
# @Email   : Guofeng.Mei@student.uts.edu.au
# @File    : gen_network.py
# @Software: PyCharm
import networkx as nx
import numpy as np


def get_network(nodes, neighs, prob, net_type='ws'):
    if net_type == 'ws':
        ws = nx.watts_strogatz_graph(nodes, neighs, prob)
        adj_mat = np.array(nx.adjacency_matrix(ws).todense())
        return adj_mat
    else:
        return None


if __name__ == '__main__':
    ws_net = get_network(10, 2, 0.2, 'ws')
    print(ws_net)
