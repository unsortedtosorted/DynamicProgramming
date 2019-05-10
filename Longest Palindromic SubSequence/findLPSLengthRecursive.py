"""

Problem Statement
Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.

Example 1:

Input: "abdbca"
Output: 3
Explanation: LPS is "bdb".


Solution :

if i==j:
  return 1
else:

  if s[i] equal to s[j]:
    remain length = j-i-1
    if dp(i+1,j-1) == remain length:
        l = 2+remain length
  also check for i+1,j and i,j-1 case
    return max (dp(i+1,j),dp(i,j-1),dp(i+1,j-1)
        
"""

def findLPSLengthRecursive(s):


    ma = [0]
    memo = {}
    def dp(i,j):

        if (i,j) in memo:
            return memo[(i,j)]

        if i > j:
            memo[(i, j)] = 0
            return 0

        if i == j:
            memo[(i, j)] = 1
            return 1
        else:

            l = 0

            if s[i] == s[j]:

                remain = j-i-1
                out = dp(i+1,j-1)
                if out == remain:
                    l = 2+out

            ma[0] = max(ma[0], l)

            l = max(l,max(dp(i+1,j),dp(i,j-1)))

            ma[0] = max(ma[0],l)

            memo[(i, j)] = l
            return l

    return dp(0,len(s)-1)


print (findLPSLengthRecursive('abdbca'))
print (findLPSLengthRecursive('cddpd'))
print (findLPSLengthRecursive('PycharmProjectsabcdcbarogrammingvenvbinpython'))
