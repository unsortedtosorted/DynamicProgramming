

def dp(i,j):


    if (i,j) in m:

        return m[(i,j)]

    if len(str1) == i or len(str2) == j:

        return 0



    if str1[i] == str2[j]:

        x =  (1+dp(i+1,j+1))
        return x


    c1 = dp(i+1,j)
    c2 = dp(i,j+1)

    m[(i,j)] = max(c1,c2)
    return  m[(i,j)]



m = {}

str1 = "HIEROGLYPHOLOGY"
str2 = "MICHAELANGELO"

print (dp(0,0))
