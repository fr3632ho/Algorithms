import sys
from math import sqrt,pow

def parse_data():
    data = sys.stdin.read().rstrip('\n').split('\n')
    N = int(data[0])
    pairs = [[int(x) for x in line.split(' ')] for line in data[1:]]
    return pairs

def mergeSortPairs(arr,idx):

    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        mergeSortPairs(left,idx)
        mergeSortPairs(right,idx)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][idx] < right[j][idx]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            arr[k] = left[i]
            k+=1
            i+=1

        while j < len(right):
            arr[k] = right[j]
            k+=1
            j+=1

def take_second(x):
    return x[1]

def distance(i,j):
    return sqrt(pow(i[0] - j[0],2) + pow(i[1]-j[1],2))

def closest_points(p):
    px,py = p,p
    mergeSortPairs(px,0)
    mergeSortPairs(py,1)
    print(format(closest(px,py,len(p)),'.6f'))

def closest(px,py,n):
    if n <= 3:
        delta = sys.maxsize
        for i in px:
            for j in px:
                dist = distance(i,j)
                if dist <= delta and dist != 0:
                    delta = dist
        return delta
    else:
        mid = n//2
        Lx,Rx = px[:mid],px[mid:]
        Ly,Ry = py[:mid],py[mid:]

        min_left = closest(Lx,Ly,len(Lx))
        min_right = closest(Rx,Ry,len(Rx))
        delta = min(min_left,min_right)

        S = set()

        dist = py[mid][1] + delta
        for i in py[mid:]:
            if i[1] > dist:
                break
            S.add((i[0],i[1]))

        dist = py[mid][1] - delta
        for i in py[mid::-1]:
            if i[1] < dist:
                break
            S.add((i[0],i[1]))

        S = sorted(S,key=take_second)
        for i in range(0,len(S)):
            for j in range(i,i+7):
                if len(S) == j:
                    break
                if i != j:
                    dist = distance(S[i],S[j])
                    if dist < delta:
                        delta = dist
        return delta


def run():
    pairs = parse_data()
    closest_points(pairs)


run()

# END
