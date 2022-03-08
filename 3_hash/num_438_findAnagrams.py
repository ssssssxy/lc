class Solution:
    def findAnagrams(self, s: str, p: str):
        results = []
        len_s = len(s)
        len_p = len(p)

        if len_s < len_p:
            return []
        record = [0] * 26
        for i in range(len_p):
            record[ord(s[i]) - ord("a")] += 1
            record[ord(p[i]) - ord("a")] -= 1

        differ = [c != 0 for c in record].count(True)

        if differ == 0:
            results.append(0)

        for i in range(len_s - len_p):
            if record[ord(s[i]) - ord("a")] == 1:
                differ -= 1
            elif record[ord(s[i]) - ord("a")] == 0:
                differ += 1
            record[ord(s[i]) - ord("a")] -= 1

            if record[ord(s[i + len_p]) - ord("a")] == -1:
                differ -= 1
            elif record[ord(s[i + len_p]) - ord("a")] == 0:
                differ += 1
            record[ord(s[i + len_p]) - ord("a")] += 1

            if differ == 0:
                results.append(i + 1)

        return results

