import collections
class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:

        def at_most_k_distance(nums, n):
            left = 0
            right = 0
            result = 0
            while right < len(nums):
                if len(set(nums[left: right + 1])) <= n:
                    result += right - left + 1
                    right += 1
                else:
                    while len(set(nums[left: right + 1])) > n:
                        left += 1
            return result

        return at_most_k_distance(nums, k) - at_most_k_distance(nums, k-1)


    def subarraysWithKDistinct_2(self, nums, k: int) -> int:
        n = len(nums)
        num1, num2 = collections.Counter(), collections.Counter()
        tot1 = tot2 = 0
        left1 = left2 = right = 0
        ret = 0

        for right, num in enumerate(nums):
            if num1[num] == 0:
                tot1 += 1
            num1[num] += 1
            if num2[num] == 0:
                tot2 += 1
            num2[num] += 1

            while tot1 > k:
                num1[nums[left1]] -= 1
                if num1[nums[left1]] == 0:
                    tot1 -= 1
                left1 += 1
            while tot2 > k - 1:
                num2[nums[left2]] -= 1
                if num2[nums[left2]] == 0:
                    tot2 -= 1
                left2 += 1

            ret += left2 - left1

        return ret

    def subarraysWithKDistinct_3(self, nums, k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, A, K):
        N = len(A)
        left, right = 0, 0
        counter = collections.Counter()
        distinct = 0
        res = 0
        while right < N:
            if counter[A[right]] == 0:
                distinct += 1
            counter[A[right]] += 1
            while distinct > K:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    distinct -= 1
                left += 1
            res += right - left + 1
            print(left, right, res)
            right += 1
        return res


s = Solution()
# print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.subarraysWithKDistinct_3([1,2,1,2,3], 2))
print(s.subarraysWithKDistinct([1,2,1,3,4], 3))