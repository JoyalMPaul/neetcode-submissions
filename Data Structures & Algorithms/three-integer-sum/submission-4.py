class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()

        for index in range(len(nums) - 2):
            num = nums[index]

            if index > 0 and nums[index] == nums[index - 1]:
                continue
            if num > 0:
                break

            left, right = index + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + num
                
                if total == 0:
                    answer.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return list(answer)