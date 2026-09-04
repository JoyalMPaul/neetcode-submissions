class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{", "]":"[", ")":"("}
        stack = []

        for bracket in s:
            if bracket in pairs.keys():
                if not stack:
                    return False
                popped = stack.pop()
                if popped != pairs[bracket]:
                    return False
            else:
                stack.append(bracket)
        return stack == []