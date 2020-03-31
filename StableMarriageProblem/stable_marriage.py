import sys
from collections import deque

p_list = deque([])

'''
Generates an inverted preferene list
'''
def invList(sub_list):
    new_list = [0] * len(sub_list)
    for num, i in enumerate(sub_list):
        new_list[i-1] = num
    return new_list

'''
Man in the Gale-Shapley algorithm
'''
class Man:

    def __init__(self,value,list):
        self.value = value
        self.pointer = 0
        self.pref_list = list

    def __str__(self):
        return 'value: {}, preference list: {}'.format(self.value, self.pref_list)

    def inc_pointer(self):
        self.pointer += 1

    def get_preferred(self):
        self.inc_pointer()
        return self.pref_list[self.pointer-1]

'''
Woman in the Gale-Shapley algorithm
'''
class Woman:

    def __init__(self,value,list):
        self.value = value
        self.partner = None
        self.pref_list = list

    def __str__(self):
        return 'value: {}, preference list: {}'.format(self.value, self.pref_list)

    def propose(self,new_partner):
        return self.pref_list[new_partner - 1] < self.pref_list[self.partner.value-1]

    def updatePartner(self,man):
        self.partner = man
'''
Data parser
'''
def parse_data():
    inp_file = sys.stdin
    lines = inp_file.read().strip().split('\n')
    exists = []
    N = int(lines[0])
    women = [0]*N
    men = [0]*N
    all_numbers = [int(i) for line in lines[1:] for i in line.split()]
    for i in range(2*N):
        data = all_numbers[i*(N+1):(1+i)*(N+1)]
        id = data[0]
        inv_list = invList(data[1:])
        if women[id-1] == 0:
            women[id-1] = Woman(id,inv_list)
        else:
            men[id-1] = Man(id,data[1:])
            p_list.appendleft(men[id-1])
    return women,men, N

'''
Gale-Shapley algorithm for stable marriages
'''
def stable_marriage():
    while len(p_list) > 0:
        man = p_list.pop()
        woman = women[man.get_preferred()-1]
        if woman.partner is None:
            woman.updatePartner(man)
        elif woman.propose(man.value):
            m_prime = woman.partner
            woman.updatePartner(man)
            p_list.append(m_prime)
        else:
            p_list.append(man)

    for woman in women:
        print(woman.partner.value)

women,men,N = parse_data()
stable_marriage()
