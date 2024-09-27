class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        if s[0] in mapping:
            return False
        elif len(s) == 1:
            return False

        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char in mapping:
                if len(stack) == 0:
                    return False
                elif mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
