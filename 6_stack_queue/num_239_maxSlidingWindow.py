from collections import deque
class Myqueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        q = Myqueue()
        ans = []
        for i in range(k):
            q.push(nums[i])
        ans.append(q.front())
        for i in range(k, len(nums)):
            q.pop(nums[i-k])
            q.push(nums[i])
            ans.append(q.front())
        return ans