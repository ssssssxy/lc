class Solution:
    def canJump(self, nums) -> bool:
        left = 0
        max_ = nums[0]
        right = max_
        while right < len(nums)-1 and max_ != 0:
            max_ = max(nums[left + 1: right+1])
            max_index = nums[left + 1: right+1].index(max_)
            left = max_index + left + 1
            right = max(right, left + max_)
        if right >= len(nums) - 1:
            return True
        else:
            return False

    def canJump_2(self, nums) -> bool:
        cover = 0
        if len(nums) == 1: return True
        i = 0
        # python不支持动态修改for循环中变量,使用while循环代替
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False

s = Solution()
# s.canJump([2,3,1,1,4])
print(s.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))