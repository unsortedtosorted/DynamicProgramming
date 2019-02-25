import sys

arr = [1,1,3,6,9,3,0,1,3]
path = {}
def nextJump(index):

    if index == len(arr) -1:
        return 0
        
    min = sys.maxsize
    ind = None
    for i in range(1,arr[index]+1):

        if index+i < len(arr):
            temp = 1 + nextJump(index+i)

            if temp<min:
                ind = index+i
                min = temp

    path[index]=(ind)
    return min


nextJump(0)
val = 0
temp = path[0]
p = []
while val!=len(arr)-1:
    p.append(val)
    val = path[val]

p.append(val)
print (p)


arr = [1, 1, 3, 6, 9, 3, 0, 1, 3,1, 3, 6, 9, 3, 0, 1, 3]
nextJump(0)
val = 0
temp = path[0]
p = []
while val!=len(arr)-1:
    p.append(val)
    val = path[val]


print (p)
