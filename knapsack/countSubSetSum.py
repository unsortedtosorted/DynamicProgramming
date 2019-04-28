"""

Given a set of positive numbers, 
find the total number of subsets 
whose sum is equal to a given number ‘S’.

Example 1:
1, 1, 2, 3
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.

dp(i,sum) = dp(i+1,sum+arr[i]) + dp(i+1,sum)

"""

def countSubsets(nums, target):


    def dp(i,sum):

        if i == len(nums):
            if sum == target:
                return 1
            else:
                return 0

        if sum == target:
            return 1

        return dp(i+1,sum+nums[i])+ dp(i+1,sum)


    return dp(0,0)

print (countSubsets([0,3,1],4))

print (countSubsets([0, 2, 7],9))
