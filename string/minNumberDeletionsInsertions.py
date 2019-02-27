


def dp(i,j):


    if i == len(str1):
        return 0
    if j == len(str2):
        return 0


    if str1[i]==str2[j]:
        return 1+dp(i+1,j+1)


    c1 = dp(i+1,j)
    c2 = dp(i,j+1)

    return max(c1,c2)



str1 = "abc"
str2 = "fbc"
x = (dp(0,0))
print ("deletions : "+ str(abs(x-len(str1))))
print ("insertions : "+ str(abs(x-len(str2))))

str1 = "abdca"
str2 = "cbda"
x = (dp(0,0))
print ("deletions : "+ str(abs(x-len(str1))))
print ("insertions : "+ str(abs(x-len(str2))))

str1 = "passport"
str2 = "ppsspt"
x = (dp(0,0))
print ("deletions : "+ str(abs(x-len(str1))))
print ("insertions : "+ str(abs(x-len(str2))))
