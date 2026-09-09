class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0

        for right in range(len(s)): 
            while s[right] in s[left:right]:
                left += 1
            maximum = max(maximum, len(s[left:right + 1])) if right < len(s) else max(maximum, len(s[left:right]))
        
        return maximum

# a, ""
# b, a
# c, ab
# a, abc