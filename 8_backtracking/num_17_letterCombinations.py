class Solution:
    def __init__(self):
        self.results = []
        self.result = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        k = len(digits)
        def backtracking(k, start_index):
            if len(self.result) == k:
                self.results.append("".join(self.result[:]))
                return
            letters = self.letter_map[digits[start_index]]
            for letter in letters:
                self.result.append(letter)
                backtracking(k, start_index + 1)
                self.result.pop()
        backtracking(k, 0)
        return self.results

s = Solution()
print(s.letterCombinations("23"))