"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a 
knapsack which has a capacity ‘C’. 
The goal is to get the maximum profit from the items in the knapsack. 

"""


import sys

def solveKnapsack(profits, weights, capacity) :
    memo = {}
    def dp(W,P):

        if (W,P) in memo:
            return memo[(W,P)]
        if W == capacity:
            memo[(W, P)] = P
            return P
        else:

            p = -sys.maxsize-1

            for i,x in enumerate(profits):
                if W+weights[i] <= capacity:
                    p = max(p,dp(W+weights[i],P+profits[i]))
            memo[(W, P)] = p
            return p


    return dp(0,0)

print (solveKnapsack([15, 20, 50],[1, 2, 3],50))
print (solveKnapsack([15, 50, 60, 90],[1, 3, 4, 5],80))
