class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0
        chars = set()

        for right in range(len(s)): 
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[right])
            maximum = max(maximum, right - left + 1)
        
        return maximum