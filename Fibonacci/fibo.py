memo = {}
memo[0] = 1
memo[1] = 1

def fibo(n,memo):

    if n in memo:
        return memo[n]

    if n == 0 or n==1:
        return 1

    else:
        x = fibo(n-1,memo)
        y = fibo(n-2,memo)

        memo[n] = x+y
        return x+y


def fiboBottomUp(n):

    if n <2:
        return 1

    prev1 = 1
    prev2 = 1


    for i in range(2,n+1):
        temp = prev1 + prev2
        prev2 = prev1
        prev1 = temp


    return temp


print (fibo(800,memo))
print (fiboBottomUp(800))
