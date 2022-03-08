class Solution:
    def trap(self, height) -> int:
        res = 0
        stack = [0]
        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    low_ = stack.pop()
                    if stack:
                        res_tmp = (min(height[stack[-1]], height[i]) - height[low_]) * (i - stack[-1] - 1)
                        res += res_tmp
                stack.append(i)
        return res


s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
