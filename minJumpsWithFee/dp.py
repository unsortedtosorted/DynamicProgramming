def dp(index,arr,memo):

    if index>=len(arr):
        return 0

    if index in memo:
        return memo[index]
    step1 = dp(index + 1,arr,memo) + arr[index]
    step2 = dp(index + 2,arr,memo) + arr[index]
    step3 = dp(index + 3,arr,memo) + arr[index]

    memo[index] = min(step1,step2,step3)
    return memo[index]

memo = {}
print (dp(0,[1,2,5,2,1,2],memo))

memo = {}
print (dp(0,[2,3,4,5,2,3,4,5,2,3,4,5,1,2,5,2,1,2,2,3,4,5,2,3,4,5,2,3,4,5,1,2,5,2,1,2,2,3,4,5,2,3,4,5,2,3,4,5,1,2,5,2,1,2,2,3,4,5,2,3,4,5,2,3,4,5,1,2,5,2,1,2,2,3,4,5,2,3,4,5,2,3,4,5,1,2,5,2,1,2,2,3,4,5,2,3,4,5,2,3,4,5,1,2,5,2,1,2],memo))
