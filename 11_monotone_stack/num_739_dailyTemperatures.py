class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)

        stack = []
        for i in range(0, len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    n = stack.pop()
                    res[n] = i - n
                stack.append(i)
        return res

s = Solution()
s.dailyTemperatures([73,74,75,71,69,72,76,73])