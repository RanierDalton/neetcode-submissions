class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums): return []

        counter = {}

        for num in nums: counter[num] = counter.get(num, 0) + 1

        sorted_nums = sorted(counter, key=counter.get, reverse=True)

        return sorted_nums[:k]