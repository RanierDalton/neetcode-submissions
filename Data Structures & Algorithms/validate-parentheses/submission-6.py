class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        open_cond = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        close_cond = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []

        for i in range(len(s)): 
            if s[i] in open_cond:
                stack.append(s[i])
                is_open = True

            else:
                if not stack or close_cond[s[i]] != stack[-1]: return False
                stack.pop()

        return not stack