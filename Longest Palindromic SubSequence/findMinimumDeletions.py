"""
Problem Statement
Given a string, find the minimum number of characters that we can remove to make it a palindrome.

Example 1:

"abdbca"
Input: "abdbca"
Output: 1
Explanation: By removing "c", we get a palindrome "abdba".


if st[i] ==  st[j]:
  return min (dp(i+1,j-1),1+dp(i,j-1),1+dp(i+1,j))
else:
  return min (1+dp(i,j-1),1+dp(i+1,j))

"""

import sys

def findMinimumDeletions(st):

    memo = {}
    def dp(i,j):

        if (i,j)  in memo:
            return memo[(i,j)]

        if i == j:
            out = 0

        elif i > j:
            out = sys.maxsize

        else:

            r = sys.maxsize
            if st[i] == st[j] :


                if i == j-1:
                    r = 0
                else:
                    r = min(r, dp(i + 1, j - 1))


            r = min(r,min(1+dp(i+1,j),1+dp(i,j-1)))

            out = r
            memo[(i,j)] = out
        return out


    return dp(0,len(st)-1)


print (findMinimumDeletions("abdbca"))
print (findMinimumDeletions("cddpd"))
print (findMinimumDeletions("Yes,thelengthoftheLongestPalindromicSubsequenceisthebestpalindromicsubsequencewecanhave.Let’stakeafewexamples:"))
