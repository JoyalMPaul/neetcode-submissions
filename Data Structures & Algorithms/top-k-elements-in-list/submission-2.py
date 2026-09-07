class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        count = [0] * len(nums)

        for key, value in seen.items():
            if count[value - 1] == 0:
                count[value - 1] = [key]
            else:
                count[value - 1].append(key)
        
        answer = []
        for lst in count[::-1]:
            if lst == 0:
                continue
            while lst != []:
                popped = lst.pop()
                answer.append(popped)
                k -= 1
                if k == 0: return answer

        