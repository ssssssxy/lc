class Solution:
    def corpFlightBookings(self, bookings, n: int):
        nums = [0] * n
        for left, right, inc in bookings:
            nums[left - 1] += inc
            if right < n:
                nums[right] -= inc

        for i in range(1, n):
            nums[i] += nums[i - 1]

        return nums

s = Solution()

print(s.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))