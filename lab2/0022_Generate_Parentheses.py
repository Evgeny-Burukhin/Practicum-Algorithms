from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        queue = deque([("", 0, 0)])
        while queue:
            s, left, right = queue.popleft()
            if len(s) == 2 * n:
                result.append(s)
            else:
                if left < n:
                    queue.append((s + '(', left + 1, right))
                if right < left:
                    queue.append((s + ')', left, right + 1))
        return result