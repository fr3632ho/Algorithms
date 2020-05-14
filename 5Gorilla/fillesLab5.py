import sys

alphabet = 0
alignment_costs = 0
queries = 0
cost_matrix = 0
word_matrix = 0
delta = -4

def parse_data(data):
    rows = data.split("\n")
    alphabet = rows[0].split()
    alphabet = {i: alphabet.index(i) for i in alphabet}
    cost_matrix_str = rows[1: len(alphabet) + 1]
    nbr_queries = int(rows[len(alphabet) + 1])
    queries = rows[len(alphabet) + 2:]
    queries = [query.split() for query in queries]
    queries.remove(queries[len(queries) - 1])
    alignment_costs = []

    for row in range(len(cost_matrix_str)):
        alignment_costs.append(cost_matrix_str[row].split())

    alignment_costs = [[int(element) for element in row] for row in alignment_costs]

    return alphabet, alignment_costs, nbr_queries, queries

def get_data():
    return sys.stdin.read()


def get_alignment_cost(word1, word2, index1, index2):
    cost_index2 = alphabet[word2[index2-1]]
    cost_index1 = alphabet[word1[index1-1]]
    return alignment_costs[cost_index1][cost_index2]

def build_matrix_iterative(word1, word2):     #För att iterativ lösning ska fungera måste vi fylla ut cost_matrix med nollor så att den blir kvadratisk.
    cost_matrix = [[-5000 for j in range(len(word1) + len(word2) + 1)] for i in range(len(word1) + len(word2) + 1)]
    for i in range(len(word1) + len(word2) + 1):
        cost_matrix[i][0] = delta * i
        cost_matrix[0][i] = delta * i

    for index1 in range(1, len(word1) + 1):
        for index2 in range(1, len(word2) + 1):
            alpha = get_alignment_cost(word1, word2, index1, index2)
            #matrix[index1][index2] = alpha
            cost_matrix[index1][index2] = max(alpha + cost_matrix[index1-1][index2-1],
                                          delta + cost_matrix[index1][index2-1],
                                          delta + cost_matrix[index1-1][index2])

    return cost_matrix


def dec(value, *args):
    for i in args:
        yield i - value

def backtrack_iterative(word1, word2):
    n,m = len(word1),len(word2)
    l = n+m
    new_word1, new_word2 = [0]*(l+1), [0]*(l+1)
    xpos = ypos = l
    i,j = n,m

    while not (i == 0 or j == 0):
        if cost_matrix[i-1][j-1] + get_alignment_cost(word1,word2,i,j) == cost_matrix[i][j]:
            new_word1[xpos] = word1[i-1]
            new_word2[ypos] = word2[j-1]
            i,j,xpos,ypos = dec(1, i, j, xpos, ypos)
        elif cost_matrix[i-1][j] + delta == cost_matrix[i][j]:
            new_word1[xpos] = word1[i-1]
            new_word2[ypos] = '*'
            i,xpos,ypos = dec(1,i,xpos,ypos)
        else:
            new_word1[xpos] = '*'
            new_word2[ypos] = word2[j-1]
            j,xpos,ypos = dec(1,j,xpos,ypos)

    while xpos > 0:
        if i > 0:
            new_word1[xpos] = word1[i-1]
            i -= 1
        else:
            new_word1[xpos] = '*'
        xpos -= 1

    while ypos > 0:
        if j > 0:
            new_word2[ypos] = word2[j-1]
            j -= 1
        else:
            new_word2[ypos] = '*'
        ypos -= 1

    id = 1
    for i in range(l,0,-1):
        if new_word1[i-1] == '*' and new_word2[i-1] == '*':
            id = i
            break

    print("".join(new_word1[id:]),"".join(new_word2[id:]))


def optimize():
    global cost_matrix, word_matrix
    for query in queries:
        cost_matrix = build_matrix_iterative(query[0], query[1])
        backtrack_iterative(query[0],query[1])


def main():
    global alphabet, alignment_costs, queries
    data = get_data()
    alphabet, alignment_costs, nbr_queries, queries = parse_data(data)
    optimize()


if __name__ == '__main__':
    main()
