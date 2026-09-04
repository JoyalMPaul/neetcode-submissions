class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for i in s:
            if (ord("a") <= ord(i) <= ord("z")):
                new_string += i
            elif (ord("A") <= ord(i) <= ord("Z")):
                new_string += i
            elif (ord("0") <= ord(i) <= ord("9")):
                new_string += i
        new_string = new_string.lower()
        print(new_string)

        left = 0
        right = len(new_string) - 1
        while left < right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -=1
        return True
