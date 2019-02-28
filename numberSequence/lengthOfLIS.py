
def lengthOfLIS(nums):

    dp = [0] * len(nums)

    if len(nums) > 0:
        dp[0] = 1
    else:
        return 0

    for i in range(1, len(nums)):
        maxlen = 0

        for j in range(0, i):

            if nums[i] > nums[j]:
                maxlen = max(maxlen, dp[j])

        dp[i] = maxlen + 1

    return max(dp)


print (lengthOfLIS([10,9,2,5,3,7,101,18]))
