class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i not in hashmap:
                stack.append(i)
            else:
                if len(stack) and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
        return not len(stack)