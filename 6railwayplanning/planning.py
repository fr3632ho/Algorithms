#!/usr/bin/env python3

import sys
import networkx
from collections import defaultdict,deque
import copy

# N = number of nodes (cities)
# M = number of edges (connections between cities)
# C = number of students (to transport between cities)
# P = number of routes

'''
Finds the path from the sink to the parent of the parents
'''
def findPath(node, parents):
    path = deque([node])
    root = node
    while parents[root] != -1:
        root = parents[root]
        path.appendleft(root)
    return path

'''
Shortest path BFS for now, this will be needed for the lab
'''

def BFS(G, s, t, p):
    discovered = {}
    q = deque([(s, sys.maxsize)])
    while q:
        cur, flow = q.pop()

        for n in G[cur].keys():
            if p[n] == -1 and G[cur][n] > 0:
                p[n] = cur
                new_flow = min(G[cur][n], flow)
                if n == t:
                    return new_flow

                q.appendleft((n, new_flow))

    return 0

def max_flow(G, s, t, N):
    flow_tot = 0
    parents = [-1] * N
    new_flow = 0

    while new_flow := BFS(G, s, t, parents):
        flow_tot += new_flow
        cur = t
        while cur != s:
            prev = parents[cur]

            G[prev][cur] -= new_flow
            G[cur][prev] += new_flow
            cur = prev

        parents = [-1]*N

    return flow_tot

def zero_flow(G,u,v):
    G[u][v] = 0
    G[v][u] = 0


'''
Adds an edge to an undirected graph
'''
def add_edge(G,u,v,flow):
    G[u][v] = flow
    G[v][u] = flow

if __name__ == "__main__":

    # Parsing of data
    data = [[int(i) for i in line.strip('\n').split()] for line in sys.stdin]
    N, M, C, P = data[0]
    source = sink = 0
    
    G = defaultdict(dict)
    source,sink = 0, N-1
    edge_ord = []

    for i in data[1:M+1]:
        add_edge(G,i[0],i[1],i[2])
        edge_ord.append((i[0],i[1]))

    paths = [i[0] for i in data[M+1:]]


    Gr = copy.deepcopy(G)
    flow = 20
    new_flow = flow
    i = 0
    while new_flow >= C and P > i:
        Gr = copy.deepcopy(G)
                
        flow = new_flow
        u,v = edge_ord[paths[i]]
        
        zero_flow(Gr,u,v)
        G = copy.deepcopy(Gr)
        new_flow = max_flow(Gr,source,sink,N)
        
        i+=1


    print(i-1,flow)
