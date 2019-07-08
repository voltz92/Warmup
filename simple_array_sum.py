# Given an array of integers, find the sum of its elements.

# For example, if the array , , so return .

# Function Description

# Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

# simpleArraySum has the following parameter(s):

# ar: an array of integers
# Input Format

# The first line contains an integer, , denoting the size of the array. 
# The second line contains  space-separated integers representing the array's elements.

# Constraints

# Output Format

# Print the sum of the array's elements as a single integer.

# Sample Input
# 6
# 1 2 3 4 10 11

# Sample Output
# 31


# solution

#!/bin/python3

import os
import sys
import functools

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    return functools.reduce((lambda a,b: a+b),ar)
    
    # alternate solutions:
    #> 1
    # return sum(ar)

    #> 2
    # total = 0
    # for number in ar:
    #    total += number
    # return total

if __name__ == '__main__':                              ### the following code is run when the python file is run in place as in not imported
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
