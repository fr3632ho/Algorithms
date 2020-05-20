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

'''
Ford Fulkerson for max flow in a graph
'''
def max_flow(G, s, t, N):
    flow_tot = 0
    parents = [-1]*N
    # terminates before max flow is found for the graph
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
Fins a flow in the graph recursively which satisfies the needed flow C
'''
def binary_search_flow(G, l, r):
    global N, C, source, sink, edge_ord, paths
    if r >= l:
        mid = l + (r-l)//2
        Gr = copy.deepcopy(G)

        for i in range(0,len(paths[:mid])):
            u,v = edge_ord[paths[i]]
            zero_flow(Gr,u,v)
        # Current flow in Residual graph with edges unitl paths[:mid] removed
        flow = max_flow(Gr, source, sink, N)
        if flow >= C:
            binary_search_flow(G, mid + 1, r)
        else:
            binary_search_flow(G, l, mid-1)
    else:
        for i in range(0, len(paths[:r])):
            u,v = edge_ord[paths[i]]
            zero_flow(G,u,v)
        print(len(paths[:l])-1, max_flow(G,source, sink, N))

'''
1. Calculate flow through original graph
2. Create residual Graph Gr with deepcopy and remove next edge and calculate flow
3. Check if flow through Gr meets the conditions
4. Repeat 2 and 3 till the conditions are broken
'''
if __name__ == "__main__":
    global G, N, C, P, source, sink
    global paths, edge_ord
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
    binary_search_flow(G,0,len(paths)-1)
