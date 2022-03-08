import copy


class Solution:
    def groupAnagrams(self, strs):
        result_dict = {}
        for one_str in strs:
            record = [0] * 26
            for i in one_str:
                record[ord(i) - ord("a")] += 1
            record_copy = str(copy.deepcopy(record))
            if record_copy in result_dict:
                result_dict[record_copy].append(one_str)
            else:
                result_dict[record_copy] = [one_str]
        return list(result_dict.values())
