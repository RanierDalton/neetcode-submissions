class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # tabela hash com os elementos e um contador 
        elements = {}

        # loop nela adicionando ao contador
            # se maior que 2, já corta true
        for i in nums:
            if i in elements:
                elements[i] = elements[i] + 1
            else:
                elements[i] = 1

            if elements[i] >= 2:
                return True

        # se passar do loop, retorna false
        return False
        