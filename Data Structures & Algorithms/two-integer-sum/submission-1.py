class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_size = len(nums)

        for i in range(nums_size):
            for j in range(i+1, nums_size):
                if i == j: continue

                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

                