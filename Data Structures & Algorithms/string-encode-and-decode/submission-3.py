class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for strings in strs:
            encoded += str(len(strings)) + "#" + strings
        
        return encoded 

    def decode(self, s: str) -> List[str]:
        left, right = 0, 0
        decoded = []
        while right < len(s):
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            decoded.append(s[left:right + length + 1])
            left = right + length + 1
            right = left

        return decoded
