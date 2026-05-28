class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []
        for ops in operations:
            if ops == '+':
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif ops == 'D':
                total += 2 * stack[-1]
                stack.append(2 * stack[-1])
            elif ops == 'C':
                total -= stack.pop()
            else:
                stack.append(int(ops))
                total += int(ops)

        return total
