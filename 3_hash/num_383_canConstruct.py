class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        for i in magazine:
            record[ord(i)-ord("a")] += 1
        for i in ransomNote:
            record[ord(i)-ord("a")] -= 1
        for i in range(26):
            if record[i] < 0:
                return False
        return True