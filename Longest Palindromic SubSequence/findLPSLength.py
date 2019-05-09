"""

Problem Statement
Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). 
In a palindromic subsequence, elements read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by 
deleting some or no elements without changing the order of the remaining elements.

Example 1:

 "abdbca"
Input: "abdbca"
Output: 5
Explanation: LPS is "abdba".



Begin with one pointer at the start and other at the end:
  if i == j:
      return 1+dp(i,j)
  else:
    if st[i] == st[j]:
        return 2 + dp(i+1,j-1)
    else:
      return max (dp(i+1,j),dp(i.j-1)

"""


def findLPSLength(st):


    memo = {}
    def dp(i,j):

        if (i,j) in memo:
            return memo[(i,j)]
        if i > j:
            return 0
        else:


            if i == j:
                memo[(i,j)] = 1+dp(i+1,j-1)

            else:


                c1 = st[i]
                c2 = st[j]

                if c1 == c2:

                    memo[(i, j)] = 2+dp(i+1,j-1)

                else:

                    memo[(i, j)] = max(dp(i+1,j),dp(i,j-1))
            return memo[(i,j)]

    return dp(0,len(st)-1)


print (findLPSLength("Since we want to try all the subsequences of the given sequence, we can use a two-dimensional array to store our results"))
print (findLPSLength("cddpd"))
print (findLPSLength("pqr"))
