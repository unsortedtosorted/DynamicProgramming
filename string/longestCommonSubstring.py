m = [0]
j1 = [0]
def dp(i,j,count):


    j1[0]+=1
    m[0] = max(count,m[0])

    if i >= len(str1) or j>= len(str2):
        return


    if str1[i] == str2[j]:

        return dp(i+1,j+1,count+1)
    else:

        return dp(i,j+1,0)


str1 = "passport"
str2 = "ppsspt"
for i in range(0,len(str1)):
    (dp(i,0,0))
print (m)

str1 = "GeeksforGeeks"
str2 = "GeeksQuiz"
for i in range(0,len(str1)):
    (dp(i,0,0))
print (m)

str1 = "zxabcdezy"
str2 = "yzabcdezx"
for i in range(0,len(str1)):
    (dp(i,0,0))
print (m)
