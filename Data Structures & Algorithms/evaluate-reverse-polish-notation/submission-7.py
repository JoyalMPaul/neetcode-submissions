class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item not in "+-*/":
                stack.append(int(item))
            else:
                first = stack.pop()
                second = stack.pop()
                
                if item == "+":
                    new = (second + first)
                elif item == "-":
                    new = (second - first)
                elif item == "*":
                    new = (second * first)
                else:
                    new = (int(second / first))
                stack.append(new)

        return stack[0]

# if symbol: add to stack
# if not symbol: pop symbol and combine with already es