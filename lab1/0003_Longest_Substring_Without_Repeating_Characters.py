class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0): return 0

        res = 1
        string = s[0]
        for r in range(1, len(s)):
            if s[r] not in string:
                string += s[r]
                res = max(res, len(string))
            else:
                res = max(res, len(string))
                string += s[r]
                while (len(string) != len(set(string))):
                    string = string[1:]
        return res