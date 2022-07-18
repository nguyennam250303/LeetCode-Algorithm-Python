class Solution:
    def lengthOfLongestSubstring(self, s):
        res = ""
        res_len = 0
        for char in s:
            if char not in res:
                res += char
                res_len = max(res_len, len(res))
            else:
                res = res[res.index(char) + 1:] + char
        return res_len
