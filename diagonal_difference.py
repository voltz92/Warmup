# diagonal difference :::
# 2D array ::: 

def diagonalDifference(arr):
    # this is the reversed array. <<< to find the minor diag using the same array.
    flipped = list(reversed(arr))
    major, minor = 0, 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # when the row == col it adds the element to the major and minor diag variable
            if i == j:
                major += arr[i][j]
                minor += flipped[i][j]
    return abs(major-minor)


# taking the matrix size as input from user
n = int(input('Matrix Size > '))
arr = []
# _ = here we dont care about the index, just running the loop a specific number of times
for _ in range(n):
    arr.append(list(map(int,input().strip().split(' '))))  # taking the matrix as input from the user. The user enters each row with each element seperated by a space
    # the map() function calls the int() function on each input() as they are taken as strings.
    
print(diagonalDifference(arr))