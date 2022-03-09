def canPartitionKSubsets(nums, k):
    if k == 1:
        return True
    target, resid = sum(nums) // k, sum(nums) % k
    if resid != 0:
        return False

    def dfs(groups):
        if not nums:
            return True
        # [前进尝试] 选择数字 看放在哪个篮子里面 for i in range(k)
        v = nums.pop()
        print('尝试放置数字{}, 剩余数组={}'.format(v, nums))
        for i in range(k):
            if groups[i] + v <= target:
                # [前进尝试]
                groups[i] += v
                print('尝试放数字{}在位置{}, groups变成={} 向下递归'.format(v, i, groups))
                if dfs(groups):
                    return True
                # [后退重置] gorups[i]返回状态
                print('数字{}放位置{}尝试失败, groups退回成{}'.format(v, i, groups))
                groups[i] -= v
            if groups[i] == 0:
                break  # 细节：减少重复搜索 保证0(没有数的篮子)始终在末尾
        # [后退重置] 循环所有的group之后 nums再返回之前状态
        nums.append(v)
        print('数字{}尝试失败 放回nums nums退回成{} \n---'.format(v, nums))
        return False
    nums.sort()
    # 如果最大值大于target则一定不能分成
    if nums[-1] > target:
        return False
    # 如果有等于target的单个数字 则将其先进行处理
    while nums and nums[-1] == target:
        nums.pop()
        k -= 1
    # 如果k=0 或者 剩下的nums里的值全是0 都return true
    if k == 0 or not any(nums):
        return True
    return dfs([0] * k)


def canPartitionKSubsets_2(nums, k):
    # 特殊情况处理
    if k == 1:
        return True  # 特殊情况1
    target, resid = sum(nums) // k, sum(nums) % k
    if resid != 0:
        return False  # 特殊情况2
    nums = sorted(nums, reverse=True)
    if nums[0] > target:
        return False  # 特殊情况3
    # 预处理
    while nums and nums[0] == target:
        nums.pop(0)
        k -= 1  # 如果有等于target的数字 则先弹出
    if not any(nums):
        return True  # 特殊情况4

    # 递归判断 （回溯法）
    def dfs(groups, nums):
        if not nums:
            return True
        v = nums[0]
        for i in range(k):
            if groups[i] + v <= target:
                # 向下递归
                groups[i] += v
                if dfs(groups, nums[1:]):
                    return True
                # 回置状态
                groups[i] -= v

            if groups[i] == 0:
                break  # 避免重复搜索
        return False

    return dfs([0] * k, nums)



# print(canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
# print(canPartitionKSubsets(nums=[4, 4, 3, 4, 5, 3, 1], k=4))
# print(canPartitionKSubsets(nums = [1,2,3,4], k = 3))
# print(canPartitionKSubsets_2(nums=[4, 4, 0, 0], k=4))

print(canPartitionKSubsets_2(nums=[4, 3, 2, 3, 5, 2, 1], k=4))

