"""

Given an infinite supply of ‘n’ coin denominations and a total money amount, 
we are asked to find the minimum number of coins needed to make up that amount.

"""

import sys
def minCoin(coins, total):


    def dp(total):

        if total == 0:
            return 0
        else:

            temp = sys.maxsize

            for x in coins:
                if total-x >=0 :
                    temp = min(temp,1+dp(total-x))



            return temp
    return dp(total)

print (minCoin([1, 2, 3],5))
print (minCoin([1, 2, 3],11))
print (minCoin([1, 2, 3],7))

print (minCoin([3,5],7))
