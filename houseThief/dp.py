def dp(index , arr):

    if index>= len(arr):
        return 0
    
    #Steal from next+1 house
    option1 = dp(index+2,arr) + arr[index]
    
    #Steal from next+2 house
    option2 = dp(index+3,arr) + arr[index]

    return max(option1,option2)


print (max(dp(0,[2, 5, 1, 3, 6, 2, 4,2, 5, 1, 3, 6, 2, 4,2, 5, 1, 3, 6, 2, 42, 5, 1, 3, 6, 2, 4]),dp(1,[2, 5, 1, 3, 6, 2, 4,2, 5, 1, 3, 6, 2, 4,2, 5, 1, 3, 6, 2, 42, 5, 1, 3, 6, 2, 4])))
print (max(dp(0,[2, 10, 14, 8, 1,2, 5, 1, 3, 6, 2, 4,2, 10, 14, 8, 1,2, 5, 1, 3, 6, 2, 4]),dp(1,[2, 10, 14, 8, 1,2, 5, 1, 3, 6, 2, 4,2, 10, 14, 8, 1,2, 5, 1, 3, 6, 2, 4])))
