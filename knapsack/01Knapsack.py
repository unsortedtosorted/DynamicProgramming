"""
Given two integer arrays to represent weights and profits of ‘N’
items, we need to find a subset of these items which will give us maximum
profit such that their cumulative weight is not more than a given number ‘C’.
Each item can only be selected once,
which means either we put an item in the knapsack or we skip it.

"""
import sys

def Knapsack(W,P,C):



    memo = {}
    def dp(ind,remain):

        if (ind,remain) in memo:
            return memo[(ind,remain)]

        if ind == len(W):
            memo[(ind, remain)] = 0
            return 0
        if remain == 0:
            memo[(ind, remain)] = 0
            return 0
        else:

            #put item at index i

            if W[ind] <= remain:
                p1 = dp(ind+1,remain-W[ind])+P[ind]
            else:
                p1 = -sys.maxsize-1

            #dont put item at ind i
            p2 = dp(ind+1,remain)
            memo[(ind, remain)] = max(p1,p2)
            return max(p1,p2)


    return dp(0,C)


profits = [1, 6, 1, 1,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1,1,1, 6, 1,1,1, 6, 1, 1,2,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1,1,1, 6, 1,1,1, 6, 1, 1,2,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1,1,1, 6, 1,1,1, 6, 1, 1,2,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1, 1,1, 6, 1,1,1, 6, 1,1,1, 6, 1, 1,2]
weights = [1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1,2, 3,5,1,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1,2, 3,5,1,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1,2, 3,5,1,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1, 2, 3, 5,1,2, 3,5,1]

print (Knapsack(weights,profits,18))

print (Knapsack(weights,profits,62))
