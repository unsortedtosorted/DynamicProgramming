"""
Problem Statement
Given a string, find the total number of palindromic substrings in it. 
Please note we need to find the total number of substrings and not subsequences.

Example 1:

abdbca
Input: "abdbca"
Output: 7
Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".

 
if dp(i,j) is palindrome , count+=1,return True
if s[i] == s[j] and dp(i+1,j-1) is palindrome, count+=1, return True
if s[i] == s[j] and i == j-1 is palindrome, count+=1, return True

else:
  return False
"""


def findCPS(st):


    memo = {}
    count = [0]

    def dp(i,j):

        if (i,j) in memo:
            return memo[(i,j)]
        if i == j:

            count[0]+=1
            memo[(i,j)] = True
            return memo[(i,j)]

        elif i > j:
            memo[(i, j)] = False
            return memo[(i,j)]
        else:
            r = False


            if st[i] == st[j]:
                if dp(i + 1, j - 1) or i + 1 == j:
                    count[0]+=1
                    r = True


            dp(i, j - 1)
            dp(i + 1, j)



            memo[(i, j)] = r

            return r

    dp(0,len(st)-1)

    return count[0]


print (findCPS("abdbca"))
print (findCPS("cdpdd"))
print (findCPS("pqr"))
print (findCPS("UsersdhruvbhardwajPycharmProjectsDynamicProgrammingvenvbin"))
