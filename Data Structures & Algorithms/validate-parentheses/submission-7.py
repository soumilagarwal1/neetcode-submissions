class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []

        if s[0] == '}' or s[0] == ']' or s[0] == ')':
            return False

        for i, ltr in enumerate(s):
            if ltr == '{' or ltr == '[' or ltr == '(':
                stack.append(ltr)
            elif stack and ltr == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and ltr == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and ltr == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False

        