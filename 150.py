class Solution:
    @staticmethod
    def evaluate(num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "/":
            if num1 * num2 < 0:
                result = abs(num1) // abs(num2)
                return -result
            return num1 // num2
        elif operator == "*":
            return num1 * num2

    def evalRPN(self, tokens) -> int:
        if len(tokens) == 1:
            return tokens[0]

        result = None
        numStack = []
        operandSet = {"+", "-", "/", "*"}

        for i, val in enumerate(tokens):
            if val in operandSet:
                num2 = numStack.pop()
                num1 = numStack.pop()

                result = self.evaluate(num1, num2, val)
                numStack.append(result)
            else:
                numStack.append(int(val))

        return result
