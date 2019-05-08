"""
Given a rod of length ‘n’, we are asked to cut the rod and sell t
he pieces in a way that will maximize the profit. 
We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

Example:

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5

dp(i) = max (i+dp(l-i)) for i in range(0,n)
"""

import sys


def solveRodCutting(lengths, prices,n):



    memo = {}
    def dp(l):

        if l in memo:
            return memo[l]
        if l == 0:
            memo[l] = 0
            return memo[l]
        else:
            m = -sys.maxsize-1

            for i,x in enumerate(lengths):
                if l-x >=0:
                    if l-x not in memo:
                        memo[l-x] = dp(l-x)
                    m = max(m,prices[i]+memo[l-x])

            return m

    return dp(n)



print (solveRodCutting([1, 2, 3, 4, 5],[2, 6, 7, 10, 13],50))

