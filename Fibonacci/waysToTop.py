

memo = {}
memo[1] = 1
memo[2] = 2
memo[3] = 4

#Top Down
def waysToTop(n,memo):

    if n in memo:
        return memo[n]

    steps = waysToTop(n-1,memo) + waysToTop(n-2,memo) + waysToTop(n-3,memo)
    memo[n] = steps
    return steps

#Bottom Up

def waysToTopBottomUp(n):

    prev1 = 2
    prev2 = 1
    prev3 = 1

    if n<=2:
        return n
    if n == 3 :
        return 4

    for x in range(3,n+1):

        temp = prev1 + prev2 + prev3

        prev3 = prev2
        prev2 = prev1
        prev1 = temp

    return temp


print (waysToTop(10,memo))
print (waysToTopBottomUp(10))
