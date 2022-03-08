class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x[0], x[1]))

        tmp = intervals[0]
        res = [tmp[:]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= tmp[1]:
                res.pop()
                tmp = [tmp[0], max(tmp[1], intervals[i][1])]
                res.append(tmp[:])
            else:
                tmp = intervals[i]
                res.append(tmp[:])
        return res


s = Solution()
s.merge([[1,4],[2,3]])