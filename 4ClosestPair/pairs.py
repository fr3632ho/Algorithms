import sys
from math import sqrt,pow

def distance(i,j):
    return sqrt(pow(i[0] - j[0],2) + pow(i[1]-j[1],2))
'''
Processes data and calls on the closest method producing the result
'''
def closest_points():
    p = []
    n = int(input())
    for i in range(n):
        temp = input().split()
        x,y = int(temp[0]),int(temp[1])
        p.append((x,y))
    px,py = sorted(p,key=lambda x:x[0]),sorted(p,key=lambda x:x[1])
    print(format(closest(px,py,len(p)),'.6f'))

'''
Finds the closest pair in a 2D plane given two sorted lists, one sorted by x and the other by y.
Returns the distance between the closest pair!
'''
def closest(px,py,n):
    if n == 3:
        return min(distance(px[0],px[1]),distance(px[0],px[2]),distance(px[1],px[2]))
    elif n == 2:
        return distance(px[0],px[1])
    else:
        mid = n//2
        Lx,Rx = px[:mid],px[mid:]
        Ly,Ry = py[:mid],py[mid:]
        delta = min( closest(Lx,Ly,len(Lx)), closest(Rx,Ry,len(Rx)) )
        S = []
        l,r = py[mid][1] - delta,py[mid][1] + delta
        for y in py:
            if l <= y[1] <= r:
                S.append(y)

        for i in range(0,len(S)):
            for j in range(i+1,i+7):
                if len(S) == j:
                    break
                if S[i] != S[j]:
                    delta = min(delta,distance(S[i],S[j]))
        return delta

closest_points()
