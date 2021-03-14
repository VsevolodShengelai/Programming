def create(length, init=0, step=0):
    
    array = []
    
    for i in range(length):
        array.append(init + ((i + 1) - 1) * step)
        
    return array;

def sort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i      
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor

    return arr

stoprec = print

def print(arr):
    stoprec(arr)

length = int(input())
init = int(input())
step = int(input())

arr = create(length, init, step)
arr = sort(arr)
print(arr)

