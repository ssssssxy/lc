def countSubArray_0(nums):
    ans = 0
    for i in range(1, len(nums)+1):
        ans += i
    return ans


def countSubArray_1(nums):
    ans = 0
    pre = 0
    i = 1
    while i < len(nums):
        if nums[i] - nums[i-1] == 1:
            pre += 1
        else:
            pre = 0
        ans += pre
        i += 1
    return ans

def countSubArray_2(nums, k):
    ans = 0
    pre = 0
    i = 0
    while i < len(nums):
        if nums[i] <= k:
            pre += 1
        else:
            pre = 0
        ans += pre
        i += 1
    return ans


print(countSubArray_0([1,3,4,5]))
print(countSubArray_1([1,3,4,5]))
print(countSubArray_2([1,3,4], 3))