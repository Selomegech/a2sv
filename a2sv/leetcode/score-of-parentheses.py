class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                curr_score = stack.pop()
                prev_score = stack.pop()
                stack.append(prev_score + max(2 * curr_score, 1))

        return stack.pop()
        