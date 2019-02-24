

memo ={}
memo[0] = 0
memo[1] = 1
memo[3] = 2
memo[4] = 4

def numOfWays(n):


    if n in memo:
        return memo[n]

    w1,w2,w3 = 0,0,0

    if n-1>=0:
        w1 = numOfWays(n-1)
    if n-3>=0:
        w2 = numOfWays(n-3)

    if n-4>=0:
        w3 = numOfWays(n-4)

    memo[n] = w1+w2+w3


    return memo[n]

print (numOfWays(8))
print (numOfWays(9))
print (numOfWays(10))
