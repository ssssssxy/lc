class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        sum1 = {}
        result = 0
        for i in nums1:
            for j in nums2:
                if i + j in sum1:
                    sum1[i + j] += 1
                else:
                    sum1[i + j] = 1

        for i in nums3:
            for j in nums4:
                if -(i + j) in sum1 and sum1[-(i + j)] != 0:
                    result += sum1[-(i + j)]
                    # sum1[-(i+j)] -= 1

        return result



s = Solution()
print(s.fourSumCount([-1,-1],
[-1,1],
[-1,1],
[1,-1]))