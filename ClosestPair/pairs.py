import sys
from math import sqrt,pow

def distance(i,j):
    return sqrt(pow(i[0] - j[0],2) + pow(i[1]-j[1],2))

def closest_points():
    data = sys.stdin.read().rstrip('\n').split('\n')
    p = [[int(x) for x in line.split(' ')] for line in data[1:]]
    px,py = sorted(p,key=lambda x:x[0]),sorted(p,key=lambda x:x[1])
    print(format(closest(px,py,len(p)),'.6f'))

def closest(px,py,n):
    if n <= 3:
        delta = sys.maxsize
        for i in px:
            for j in px:
                dist = distance(i,j)
                if dist < delta and dist != 0:
                    delta = dist
        return delta
    else:
        mid = n//2
        Lx,Rx = px[:mid],px[mid:]
        Ly,Ry = py[:mid],py[mid:]
        delta = min( closest(Lx,Ly,len(Lx)), closest(Rx,Ry,len(Rx)) )

        S = set()
        r,l = py[mid][1] + delta,py[mid][1] - delta
        for i in py[mid:]:
            if i[1] > r:
                break
            S.add((i[0],i[1]))

        for i in py[mid::-1]:
            if i[1] < l:
                break
            S.add((i[0],i[1]))

        S = sorted(S,key=lambda x:x[1])
        for i in range(0,len(S)):
            for j in range(i+1,i+7):
                if len(S) == j:
                    break
                dist = distance(S[i],S[j])
                if dist < delta:
                    delta = dist
        return delta

closest_points()
