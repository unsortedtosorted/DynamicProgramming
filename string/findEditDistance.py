def findEditDistance(word1,word2):

    def dp(i,j):

        if i >= len(word1):
            return len(word2)-j
        if j >= len(word2):
            return len(word1)-i

        #words are same
        if word1[i] == word2[j]:
            return dp(i+1,j+1)

        else:

        #insert
            return min(1+dp(i+1,j),1+dp(i,j+1),1+dp(i+1,j+1))

    return dp(0,0)

print (findEditDistance('bat','but'))
print (findEditDistance('abdca','cbda'))
print (findEditDistance('passpot','ppsspqrt'))



