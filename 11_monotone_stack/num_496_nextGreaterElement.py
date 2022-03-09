class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            if not stack:
                stack.append(i)
                continue

            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums2[i] > nums2[stack[-1]]:
                    n = stack.pop()
                    if nums2[n] in nums1:
                        res[nums1.index(nums2[n])] = nums2[i]
                stack.append(i)
        return res

s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
