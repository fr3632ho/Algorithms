#!/bin/python3

import sys
from collections import deque

def parse_data():
    inp_file = sys.stdin
    result = inp_file.read().strip().split('\n')
    first_line = [int(x) for x in result[0].split()]
    (N,Q) = (first_line[0],first_line[1])
    N_list = result[1:N+1]
    Q_list = result[N+1:N+1+Q]
    return N,Q,N_list,Q_list

def setup_graph(words):
    copy = words.copy()
    graph = dict()
    for key in words:
        graph.setdefault(key,[])

    for i in range(len(copy)):
        for j in range(len(copy)):
            if j != i:
                count = 0
                word1 = list(copy[i])
                word2 = list(copy[j])
                for w1 in word1[1:]:
                    prev_count = count
                    for w2 in word2:
                        if prev_count != count:
                            continue
                        elif w1 == w2:
                            word2[word2.index(w2)] = -1
                            count += 1
                    string_word1 = "".join(word1)
                    if count >= 4:
                        graph[string_word1].append(copy[j])
    return graph

N, Q, words, queries = parse_data()
graph = setup_graph(words)
#print(f'# of words: {N}, # of queries: {Q}\nWords: {words}\nQueries: {queries}\n')
#print(f'Current graph: {graph} \n')

# discovered = []
# 'where' : ['there', 'shere']
# 'where' --> queue.
# discovered.append('where')
# look_at_verices('where') --> ['there', 'shere']
#
# visit_vertices -- > 'there' --> goal --> end
#     otherwise:

def BFS(G, start, end):
    #discovered = [False] * len(G.keys())
    if start == end:
        return 0
    discovered = []
    queue = []
    discovered.append(start)
    queue.append([start,0])
    while queue:
        v = queue.pop()
        if v[0] == end:
            return v[1]
        for edge in graph[v[0]]:
            if edge not in discovered:
                discovered.append(edge)
                queue.append([edge,v[1] + 1])

    return "Impossible"

q_list = [ i.split(" ") for i in queries]

for query in q_list:
    print(BFS(graph,query[0],query[1]))


#END
