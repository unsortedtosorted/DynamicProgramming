"""
Problem Statement
Given a set of positive numbers, determine if there exists a subset
whose sum is equal to a given number ‘S’.

Example 1:
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}

dp (i,remain) = dp(i+1,remain-arr[i])  or dp(i+1,remain) } for all i in range(0, len(Arr))

base condition:
  if i == len(arr):
      return remain == 0

"""


def canPartition(arr,S):


    memo = {}

    def dp(ind,remain):

        if (ind,remain) in memo:
            return memo[(ind,remain)]

        if ind == len(arr):
            memo[(ind, remain)] = (remain == 0)

        else:
            memo[(ind, remain)] =  dp(ind+1,remain-arr[ind]) or dp(ind+1,remain)

        return memo[(ind, remain)]

    return dp(0,S)

print (canPartition([1,30,30,7],60))
print (canPartition([1,2,7,1,5],10))
print (canPartition([1,3,4,8],6))
