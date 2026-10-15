class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        seen = set()

        for index in range(len(nums)):
            num = nums[index]

            left, right = 0, len(nums) - 1
            while left < right:
                if left >= index:
                    break
                if right == index:
                    right -= 1
                    continue
                
                total = nums[left] + nums[right] + num
                if total == 0:
                    numbers = tuple(sorted([num, nums[left], nums[right]]))
                    if numbers not in seen:
                        seen.add(numbers)
                        answer.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return answer