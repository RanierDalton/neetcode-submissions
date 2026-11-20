class Solution:
    def isValid(self, s: str) -> bool:
        # se não fechar números de pares, em teoria é para voltar
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
        is_open = False
        # colocar tudo na stack
        for i in range(len(s)): 
            if s[i] in open_cond:
                stack.append(s[i])
                is_open = True

            if s[i] in close_cond and len(stack) > 0 and is_open:
                # espio, se não for da condição, nn dou pop
                if close_cond[s[i]] != stack[-1]: return False
                stack.pop()

        return len(stack) == 0 and is_open