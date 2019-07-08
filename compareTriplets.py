# comparing 2 triplets containing scores and returning the points gained by each member


def compareTriplets(a, b):
    alice = 0
    bob = 0
    #working solution
    for i in range(len(a)):
        if a[i] > b[i]:
            alice+=1
        elif a[i] < b[i] :
            bob+=1
    return [alice, bob]
    
    # # map method 
    # points = list(map(lambda x, y: 1 if max(x,y)==x else -1, a,b))
    # for i n range()
    

    
alice = [5, 6, 7]
bob = [3, 6, 10]
print(compareTriplets(alice,bob))