#!/usr/bin/env python3
import sys
from math import pow
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
def BFS(G, s, t, p, i):
    discovered = {}
    q = deque([(s, sys.maxsize)])
    print(i)
    C_i = sum([G[s][x] for x in G[s]]) // pow(2,i)
    #print(C_i)

    while q:
        cur, flow = q.pop()

        for n in G[cur].keys():
            if p[n] == -1 and G[cur][n] >= C_i:
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
    i = 1
    while (new_flow := BFS(G, s, t, parents, i)) or not i > 1:
        flow_tot += new_flow
        cur = t
        while cur != s and new_flow:
            prev = parents[cur]
            #print(prev,cur)

            G[prev][cur] -= new_flow
            G[cur][prev] += new_flow
            cur = prev

        parents = [-1]*N
        i += 1

    return flow_tot

'''
Set zero flow to the given edge relation
'''
def zero_flow(G,u,v):
    G[u][v] = 0
    G[v][u] = 0

'''
Adds an edge to an undirected graph
'''
def add_edge(G,u,v,flow):
    G[u][v] = flow
    G[v][u] = flow

'''

'''
def calc_flow(G,edge_order,paths,N,C,P,source,sink):
    Gr = copy.deepcopy(G)

    i = 0
    flow = sys.maxsize
    prev_flow = flow
    while flow >= C and P > i:
        u,v = edge_order[paths[i]]
        zero_flow(Gr,u,v)
        G = copy.deepcopy(Gr)

        prev_flow = flow
        flow = max_flow(G,source,sink,N)

        i += 1

    print(i-1,prev_flow)

'''
1. Calculate flow through original graph
2. Create residual Graph Gr with deepcopy and remove next edge and calculate flow
3. Check if flow through Gr meets the conditions
4. Repeat 2 and 3 till the conditions are broken
'''
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

    calc_flow(G,edge_ord, paths, N, C, P, source, sink)
