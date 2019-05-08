"""
We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. 
Now we need to cut the ribbon into the maximum number of pieces that 
comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

Example 1:

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.

"""

import sys

def countRibbonPieces(ribbonLengths,total):

    memo = {}
    def dp(total):
        if total in memo:
            return memo[total]
        if total == 0:
            memo[total] = 0
            return 0
        else:

            v = -sys.maxsize-1

            for l in ribbonLengths:
                if total - l >=0:
                    v = max(v,1+dp(total-l))

            memo[total] = v
            return v

    return dp(total)
