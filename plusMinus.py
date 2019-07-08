# this function calculates the percentage of positive negative and zero values in a list
def plusMinus(arr):
    size = len(arr)
    plus, minus = 0,0
    for i in arr: 
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
    # formatting to print upto 6 decimal places
    print('{0:.6f}'.format(plus/size))
    print('{0:.6f}'.format(minus/size)) 
    print('{0:.6f}'.format((size - (plus+minus))/size))

arr = [-4,3, -9, 0, 4, 1]

