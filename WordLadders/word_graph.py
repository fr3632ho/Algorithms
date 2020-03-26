import sys
from collections import defaultdict as Map

def parse_data():
    inp_file = sys.stdin
    result = inp_file.read().strip().split('\n')
    first_line = [int(x) for x in result[0].split()]
    (N,Q) = (first_line[0],first_line[1])
    N_list = result[1:N]
    Q_list = result[N+1:N+1+Q]
    return (N,Q,N_list,Q_list)



(N,Q,words,queries) = parse_data()
print(N,Q,words,Queries)
