class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        num_1 = len(nums1)
        num_2 = len(nums2)
        i = j = 0
        results = []
        while i < num_1 and j < num_2:
            if nums1[i] == nums2[j]:
                results.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return results
