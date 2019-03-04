
map = {}
memo = {}

for i in range(1,27):
    map[i] = chr(ord('a')+i-1)


def decode(str):


    if str in memo:
        return memo[str]

    if len(str) == 0:
        memo[str] = 1
        return 1

    n1 = 0
    n2 = 0

    if len(str)>=1:
        n1 = decode(str[1:])

    if len(str)>=2 and int(str[:2])<=26:
        n2 = decode(str[2:])

    memo[str] = n1+n2
    return n1+n2


print (decode("27"))
print (decode("255"))
print (decode("11111111111111"))
print (decode("369"))
print (decode("2726"))
