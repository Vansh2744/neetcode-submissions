class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            visited = set()
            for j in range(i, len(s)):
                if s[j] in visited:
                    break
                else:
                    visited.add(s[j])
            res = max(res, len(visited))

        return res