class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        i = 0
        chars = {}
        for j in range(n):
            if s[j] in chars:
                i = max(chars[s[j]], i)
            ans = max(ans, j - i + 1)
            chars[s[j]] = j + 1

        return ans