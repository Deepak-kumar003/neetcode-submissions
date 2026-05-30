class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        max_lenght = 1
        charIn = set()
        for right in range(len(s)):
            while s[right] in charIn:
                charIn.remove(s[left])
                left += 1
            length = right - left + 1
            charIn.add(s[right])
            max_lenght = max(length, max_lenght)
        return max_lenght
