class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        # para cada número na lista
        for n in nums:
            # caso não exista um número anterior na ordem
            if (n - 1) not in numSet:
                length = 0

                # valida o tamnho da sequencia somando o length na iteração
                while(n + length) in numSet:
                    length += 1

                # pega o maior do longest comparado com o tamanho
                longest = max(length, longest)
        return longest