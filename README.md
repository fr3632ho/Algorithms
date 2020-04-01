# Algorithms & Datastructures

### Stable Marriage Problem
One O(n<sup>2</sup>) solution to the stable marriage problem, with the Gale-Shapley algorithm as a foundation
* The script says that every test passed. After doing some runs with the largest test set it avreages a total run time of about 5-6 seconds and performs the algorithm in around 1/20th of a second. Preprocessing the data seems to take the most amount of time in this case and the algorithm itself is pretty fast. All measurements were done using the time module with the time.perf_counter_ns() method.
* We implemented the soultion using the Gale-Shapley algorithm for stable marriages, as instructed, with a worst time complexity of O(n<sup>2</sup>). When implementing we tried to limit the amount of traversals that had to be done as much as possible, so using pythons double ended queue (deque) we got fast access to the defiend p_list. Other than the deque, we only used lists. The worst case can be explained, because when the algorithm terminates (implying that all men are paired with a woman) the men got paired with their least preffered woman. Since there are n men looking to be paired and each has a preference list of length n, we get a worst case of O(n^2).
* The algorithm terminates due to the fact that it is a greedy algorithm for the women (always striving for a local optimum, in other words choosing the best mate for themselves). The men will propose to the women in their preference list and make pairs, however, the women always have the possibility to trade up if there is another proposal that is better suited for themselves. Which means that the proposer is higher up on their preference list. If a marriage is broken, the men will go down their preference list until there is nobody to propose to. At that point the algorithm terminates, since all men will then have a partner and no man can propose to another woman.
* The algorithm reaches a stable solution, this can be shown with a proof of contradicition. Assume there is a dissatisfied pair (m1,w1) where m1 is paired with w2 and w2 is paired with m2 when the algorithm terminates, implying that m1 prefers w1 to w2. If this is the case then m1 must have proposed to w1 already and been rejected or been dumped since w1 must have preferred m2 to m1. Our assumption is then false and there can't be a dissatisfied pair (m1,w1) when the algorithm terminates. Hence the solution is stable.

### Word Ladders
Graphing problem which is yet not solved. Finding the shortest path with the help of the BFS-algorithm

### DFS example
Added a DFS example
