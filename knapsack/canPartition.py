"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Example 
1, 2, 3, 4
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}


DP equation :

  dp(i,sum) = dp(i+1,sum+arr[i]) or dp(i+1,sum) } for all i in range(0, len(arr)
  base condition:
    if i == len(arr):
        if sum == sum(arr)/2 -- > True
        else False

"""

def canPartition(num):

    memo = {}

    def dp(ind,s):

        if (ind,s) in memo:
            return memo[(ind,s)]
        if ind == len(num):
            memo[(ind, s)] = s == sum(num)-s

        else:

            memo[(ind, s)] = dp(ind+1,s+num[ind]) or dp(ind+1,s)

        return memo[(ind, s)]

    return dp(0,0)


print (canPartition([1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4]))
print (canPartition([1, 1, 3, 4, 7]))
print (canPartition([2, 3, 4, 6]))
