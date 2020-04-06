# Algorithms & Datastructures

### Stable Marriage Problem
One O(n<sup>2</sup>) solution to the stable marriage problem, with the Gale-Shapley algorithm as a foundation
* The script says that every test passed. After doing some runs with the largest test set it avreages a total run time of about 5-6 seconds and performs the algorithm in around 1/20th of a second. Preprocessing the data seems to take the most amount of time in this case and the algorithm itself is pretty fast. All measurements were done using the time module with the time.perf_counter_ns() method.
* We implemented the soultion using the Gale-Shapley algorithm for stable marriages, as instructed, with a worst time complexity of O(n<sup>2</sup>). When implementing we tried to limit the amount of traversals that had to be done as much as possible, so using pythons double ended queue (deque) we got fast access to the defiend p_list. Other than the deque, we only used lists. The worst case can be explained, because when the algorithm terminates (implying that all men are paired with a woman) the men got paired with their least preffered woman. Since there are n men looking to be paired and each has a preference list of length n, we get a worst case of O(n<sup>2</sup>).
* The algorithm terminates due to the fact that it is a greedy algorithm for the women (always striving for a local optimum, in other words choosing the best mate for themselves). The men will propose to the women in their preference list and make pairs, however, the women always have the possibility to trade up if there is another proposal that is better suited for themselves. Which means that the proposer is higher up on their preference list. If a marriage is broken, the men will go down their preference list until there is nobody to propose to. At that point the algorithm terminates, since all men will then have a partner and no man can propose to another woman.
* The algorithm reaches a stable solution, this can be shown with a proof of contradicition. Assume there is a dissatisfied pair (m<sub>1</sub>,w<sub>1</sub>) where m<sub>1</sub> is paired with w<sub>2</sub> and w<sub>2</sub> is paired with m<sub>2</sub> when the algorithm terminates, implying that m1 prefers w<sub>1</sub> to w<sub>2</sub>. If this is the case then m<sub>1</sub> must have proposed to w<sub>1</sub> already and been rejected or been dumped since w<sub>1</sub> must have preferred m<sub>2</sub> to m<sub>1</sub>. Our assumption is then false and there can't be a dissatisfied pair (m<sub>1</sub>,w<sub>1</sub>) when the algorithm terminates. Hence the solution is stable.
* <p>Assume we have a male-optimal matching A and if for any male m we have a stable solution C, A(m) &ge; C(m). Assume we also have a matching B which is male-pessimal and if for any male m we have a stable solution C, C(m) &ge; B(m). Now assume A = B, which implies that A(m) &ge; C(m) &ge; B(m) = A(m). Then A = C and the solution is unique.</p>

### Word Ladders
<p>Graphing problem. Find the length of the shortest path between any nodes a,b &isin; G. Implemented soultion is done with the help of the BFS algorithm. </p>

* The graph is represented as a dicitionary with words as keys and their connecting nodes as their values.
* If one were to perform backtracking, how would that be done? For instance, each and every node could keep track of a path leading back to the starting node, and then simply return that path if the end point is found. However, this would take up a lot of memory since for the case were a path can't be found in a large data set, that would imply that a lot of lists will have to be instansiated and thus taking up space.
* Say for the graph that we have the vertex set V and edge set E the time complexity for BFS would be O(V+E). Let's assume that <p>  |E|&ge;|V|, which it would be for most graphs. This implies that |V|+|E|&le;|E|+|E|=2 *|E|. With our assumption we now see that |E|&ge;|V| and thus O(V+E) is the same as O(E) for large sets. However, if |V|&g;|E|, then |V|+|E|&le;|V|+|V|=2*|V|, then O(V+E) is the same as O(V)! By putting both cases together we get O(V+E).  </p>

### DFS example
Added a DFS example
