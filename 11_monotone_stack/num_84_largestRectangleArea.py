class Solution:
    def largestRectangleArea(self, heights) -> int:
        # 方法一 双指针 超时
        # right = 1
        # max_ = heights[0]
        # for right in range(1, len(heights)):
        #     for left in range(right+1):
        #         max_ = max(max_, min(heights[left:right+1])*(right-left+1))
        # return max_

        # 方法二 动态规划
        # res = 0
        # # 两个DP数列储存的均是下标index
        # left_min = [0] * len(heights)
        # right_min = [0] * len(heights)
        # left_min[0] = -1
        # for i in range(1, len(heights)):
        #     # 以当前柱子为主心骨，向左迭代寻找次级柱子
        #     temp = i - 1
        #     while temp >= 0 and heights[temp] >= heights[i]:
        #         # 当左侧的柱子持续较高时，尝试这个高柱子自己的次级柱子（DP
        #         temp = left_min[temp]
        #     # 当找到左侧矮一级的目标柱子时
        #     left_min[i] = temp

        # right_min[-1] = len(heights)
        # for i in range(len(heights)-2, -1, -1):
        #     # 以当前柱子为主心骨，向右迭代寻找次级柱子
        #     temp = i + 1
        #     while temp < len(heights) and heights[temp] >= heights[i]:
        #         # 当右侧的柱子持续较高时，尝试这个高柱子自己的次级柱子（DP
        #         temp = right_min[temp]
        #     # 当找到右侧矮一级的目标柱子时
        #     right_min[i] = temp

        # for i in range(len(heights)):
        #     res = max(res, heights[i]*(right_min[i]-left_min[i]-1))

        # return res

        # 方法三 单调栈

        heights.insert(0, 0)
        heights.append(0)
        res = 0
        stack = [0]
        for i in range(1, len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid_index = stack[-1]
                    stack.pop()
                    if stack:
                        left_index = stack[-1]
                        right_index = i
                        w = right_index - left_index - 1
                        h = heights[mid_index]
                        res = max(res, w * h)
                stack.append(i)
        return res


s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
# print(s.largestRectangleArea([5, 4, 1, 2]))