"""
Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). 
In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

Example 1:

4,2,3,6,10,1,12
Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LIS is {2,3,6,10,12}.



dp(i,j) =   
           1 + dp(j,j+1) ==> if num[j] > num[i]
           max(dp(i,j+1),dp(j,j+1)) ==> num[j] <= num[i]
           
           base : return 1 if i >= len(nums) or j >= len(nums)
"""





def findLISLength(nums):

    def dp(i,j):

        if i >= len(nums) or j >= len(nums):
            return 1

        else:

            if nums[j] > nums[i]:

                return 1 + dp(j,j+1)
            else:

                return max(dp(i,j+1),dp(j,j+1))
    if len(nums) == 0:
        return 0
    return dp(0,0)


print (findLISLength([1,3,5,4,7]))
print (findLISLength([4,3,2,1]))
print (findLISLength([4,2,3,6,10,1,12]))
print (findLISLength([10,9,2,5,3,7,101,18]))


