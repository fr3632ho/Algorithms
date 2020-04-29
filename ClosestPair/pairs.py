import sys

def parse_data():
    data = sys.stdin.read().rstrip('\n').split('\n')
    N = int(data[0])
    pairs = [[int(x) for x in line.split(' ')] for line in data[1:]]

    print(f'N: {N}\nPairs: {pairs}')

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


def closest_points(p):
    px,py = p,p.copy(
    mergeSortPairs(px,0)
    mergeSortPairs(py,1)
    closest(px,py,len(p))

def closest(px,py,n):
    if n <= 3:
        delta = sys.maxsize
        for i in px:
            for j in py:
                dist = ((i[0] - j[0])**2 + (i[1]-j[1])**2)**0.5
                if dist <= delta:
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


def run():
    pairs = parse_data()
    closest_points(pairs)


run()

# END
