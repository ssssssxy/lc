class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        start = 0
        curSum = 0
        totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0: return -1
        return start

s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))