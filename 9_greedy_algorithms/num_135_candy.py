class Solution:
    def candy(self, ratings: List[int]) -> int:
        results = [1] * len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                results[i+1] = results[i] + 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                results[i-1] = max(results[i-1], results[i]+1)
        return sum(results)