"""
Give three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ 
has been formed by interleaving ‘m’ and ‘n’. ‘p’ would be considered 
interleaving ‘m’ and ‘n’ if it contains all the letters from ‘m’ and ‘n’ 
and the order of letters is preserved too.

"""


def isInterleaving(w1,w2,p):



    def isSubSeq(w,i,j):

        if i == len(w):
            return True

        if j >= len(p) or i >=len(w):
            return False

        if w[i] == p[j]:
            return isSubSeq(w,i+1,j+1)

        else:
            return isSubSeq(w,i,j+1)


    return (isSubSeq(w1,0,0)) and (isSubSeq(w2,0,0))


print (isInterleaving("abd","cef", "abcdef"))
print (isInterleaving("abd","cef", "adcbef"))
print (isInterleaving("abd","def", "abdccf"))
print (isInterleaving("abcdef","mnop", "mnaobcdepf"))










