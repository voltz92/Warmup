# min max sum

def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:len(arr)-1]), sum(arr[1:len(arr)]))

a = [1,23,3,34,11]
miniMaxSum(a)