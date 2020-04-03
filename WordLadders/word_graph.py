import sys
import time
from collections import deque

'''
# Description: Parses the given file and seperates the input into two lists; A word
  list and a queries list.
# Returns: Word-list and Queries-list
'''
def parse_data():
    inp_file = sys.stdin
    result = inp_file.read().strip().split('\n')
    first_line = [int(x) for x in result[0].split()]
    (N,Q) = (first_line[0],first_line[1])
    N_list = result[1:N+1]
    Q_list = result[N+1:N+1+Q]
    return N_list,Q_list

'''
# Description: Parses the words according to the given rules for which a vertex is connected to another
  or not!
# Returns: The graph containing all vertices and their outgoing edges.
'''
def setup_graph(words):
    copy = words.copy()
    graph = dict()
    for key in words:
        graph.setdefault(key,[])

    for i in range(len(copy)):
        for j in range(len(copy)):
            if j != i:
                count = 0
                word1,word2 = list(copy[i]),list(copy[j])
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

'''
# Description: The BFS algorithm
# Datastructures: Set, deque and dict
# Returns: Returns the shortest amount of steps needed to get from 'start' to 'end'
  or 'Impossible' if a path could not be found.
'''
def BFS(G, start, end):
    if start == end:
        return 0
    discovered,queue = {start},deque([])
    queue.append([start,0])
    while queue:
        v = queue.pop()
        if v[0] == end:
            return v[1]
        for vertex in G[v[0]]:
            if vertex not in discovered:
                discovered.update([vertex])
                queue.appendleft([vertex,v[1] + 1])
    return "Impossible"

def run():
    W, Q = parse_data()
    start = time.perf_counter_ns()
    graph = setup_graph(W)
    queries = [ i.split(" ") for i in Q]
    for query in queries:
        print(BFS(graph,query[0],query[1]))
    print(f'TOTAL RUN TIME: {(time.perf_counter_ns() - start)/10**9 }')

run()
