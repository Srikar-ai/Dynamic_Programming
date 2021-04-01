def LongestCommonSubsequence(nums):
    output=[1]*len(nums)
    for x in range(1,len(nums)):
        for y in range(x-1,-1,-1):
            if nums[x]<nums[y] or nums[x]==nums[y]:
                continue
            ans=output[y]+1
            if ans>output[x]:
                output[x]=ans
    return max(output)
print(LongestCommonSubsequence([6, 1, 7, 2, 8, 3, 4, 5]))  
