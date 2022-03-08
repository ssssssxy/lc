class Solution:
    def totalFruit(self, fruits) -> int:
        if len(fruits) in [0, 1]:
            return len(fruits)
        n = 0
        left = 0
        right = 1
        result = 0
        two_frults = [fruits[0]]
        while right < len(fruits):
            if fruits[right] != fruits[right - 1]:
                if fruits[right] not in two_frults:
                    if len(two_frults) > 1:
                        two_frults[0] = fruits[right - 1]
                        two_frults[1] = fruits[right]
                        left = n + 1
                    else:
                        two_frults.append(fruits[right])
                n = right - 1
            result = max(result, right - left + 1)
            right += 1

        return result

s = Solution()
# print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.totalFruit([14,14,1,1,14,5,14,1,14,1,5,5,1,24,7,7,8,7,7,12,12,8,23,8,23,8,20,10,0,17]))

print(s.totalFruit([3,3,3,1,2,1,12,2]))
print(s.totalFruit([1,2,1]))