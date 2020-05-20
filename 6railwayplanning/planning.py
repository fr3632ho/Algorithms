#!/usr/bin/env python3
import sys,copy
from math import pow
from collections import defaultdict,deque

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
    G[u][v] = G[v][u] = 0

'''
Adds an edge to an undirected graph
'''
def add_edge(G,u,v,flow):
    G[u][v] = G[v][u] = flow

def zero_flows(G, edges, paths,x):
    for i in range(len(paths[:x])):
        u,v = edges[paths[i]]
        zero_flow(G,u,v)
'''
Finds a flow in the graph recursively which satisfies the needed flow C
'''
def binary_search_flow(G, l, r):
    global N, C, source, sink, edge_ord, paths
    if r >= l:
        mid = l + (r-l)//2
        Gr = copy.deepcopy(G)
        zero_flows(Gr, edge_ord, paths, mid)
        # Current flow in Residual graph with edges unitl paths[:mid] removed
        flow = max_flow(Gr, source, sink, N)
        if flow >= C:
            binary_search_flow(G, mid + 1, r)
        else:
            binary_search_flow(G, l, mid-1)
    else:
        zero_flows(G, edge_ord, paths, r)
        print(len(paths[:r]), max_flow(G,source, sink, N))

'''
# N = number of nodes (cities)
# M = number of edges (connections between cities)
# C = number of students (to transport between cities)
# P = number of routes
'''
if __name__ == "__main__":
    global G, N, C, P, source, sink, paths, edge_ord
    data = [[int(i) for i in line.strip('\n').split()] for line in sys.stdin]
    N, M, C, P = data[0]
    source, sink = 0, N-1
    G, edge_ord = defaultdict(dict), []

    for i in data[1:M+1]:
        add_edge(G,i[0],i[1],i[2])
        edge_ord.append((i[0],i[1]))

    paths = [i[0] for i in data[M+1:]]
    binary_search_flow(G,0,len(paths)-1)
