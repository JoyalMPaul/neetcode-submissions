class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            if (target - num) not in seen.keys():
                seen[num] = index
            else:
                return [seen[target - num], index]
        
        return []