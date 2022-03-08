class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cur_diff = 0
        pre_diff = 0
        res = 1
        for i in range(len(nums) - 1):
            cur_diff = nums[i+1] - nums[i]
            if cur_diff*pre_diff <= 0 and cur_diff != 0:
                res += 1
                pre_diff = cur_diff
        return res