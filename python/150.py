class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        
        return stack[-1]
    

if __name__ == "__main__":
    solution = Solution()

    tokens = ["2","1","+","3","*"]
    assert solution.evalRPN(tokens) == 9

    tokens = ["4","13","5","/","+"]
    assert solution.evalRPN(tokens) == 6

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    assert solution.evalRPN(tokens) == 22
