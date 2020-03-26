import sys



def parse_data():
    inp_file = sys.stdin
    result = inp_file.read().strip().split('\n')
    first_line = [int(x) for x in result[0].split()]
    (N,Q) = (first_line[0],first_line[1])
    N_list = result[1:N]
    Q_list = result[N+1:N+1+Q]

parse_data()
