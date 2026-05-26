class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first=list(s)
        first.sort()
        second=list(t)
        second.sort()
        if first==second:
            return True
        else:
            return False
        