import sys
from collections import defaultdict as Map

def parse_data():
    inp_file = sys.stdin
    result = inp_file.read().strip().split('\n')
    first_line = [int(x) for x in result[0].split()]
    (N,Q) = (first_line[0],first_line[1])
    N_list = result[1:N]
    Q_list = result[N+1:N+1+Q]
    return N,Q,N_list,Q_list

def setup_graph(words):
    copy = words.copy()
    graph = Map()
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

N,Q,words,queries = parse_data()
graph = setup_graph(words)
#print(str(N),str(Q) + '\n',str(words) + '\n', str(queries) + '\n')
