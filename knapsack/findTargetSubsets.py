"""

Given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. 
We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

Example 1:
1, 1, 2, 3
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}



dp(i,s) = dp(i+1,-arr[i]+s)+ dp(i+1,arr[i]+s)

base condition:
    if i == len(arr):
      if s == target --> 1
      else --> '0'
"""

def findTargetSubsets(nums,target):

    def dp(i,s):
        
        if i == len(nums):
            if s == target:
                return 1
            else:
                return 0

        else:

            return dp(i+1,-nums[i]+s) + dp(i+1,nums[i]+s)

    return dp(0,0)


print (findTargetSubsets([1, 1, 2, 3],1))

print (findTargetSubsets([1, 2, 7, 1],9))
