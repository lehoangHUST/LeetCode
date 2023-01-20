class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Ki?m tra di?u ki?n li?u s có r?ng hay không ?
        if s == "":
            return 0

        maxans = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans