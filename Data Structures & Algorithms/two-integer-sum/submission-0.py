class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_size = len(nums)
        
        if nums_size <= 1: return [] 
        
        for i in range(nums_size):
            for j in range(nums_size):
                if i == j: continue

                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

                