class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for c in s:
            if c in char_map.values():
                stack.append(c)
            else:
                if len(stack) > 0 and char_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
    

if __name__ == "__main__":
    solution = Solution()

    s = "()"
    assert solution.isValid(s)

    s = "()[]{}"
    assert solution.isValid(s)

    s = "(]"
    assert not solution.isValid(s)

    s = "([])"
    assert solution.isValid(s)

    s = "([)]"
    assert not solution.isValid(s)

    s = "["
    assert not solution.isValid(s)

    s = "]"
    assert not solution.isValid(s)
