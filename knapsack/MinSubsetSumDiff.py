"""
Given a set of positive numbers, 
partition the set into two subsets 
with a minimum difference between their subset sums

"""

def canPartition(nums):


    def dp(i,s):

        if i == len(nums)-1:
            s2 = sum(nums)-s
            return abs(s2-s)
        else:


            # i included in set
            p1 = dp(i+1,s+nums[i])

            #i not included in set
            p2 = dp(i+1,s)

            return min(p1,p2)

    return dp(0,0)

print (canPartition([1,2,3,9]))
print (canPartition([1,2,7,1,5]))
print (canPartition([1,3,100,4]))
