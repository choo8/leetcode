from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = defaultdict(int)

        for c in s:
            chars[c] += 1

        for c in t:
            chars[c] -= 1
            if chars[c] < 0:
                return False
            
        return True
    

if __name__ == "__main__":
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t)

    s = "rat"
    t = "car"
    assert not solution.isAnagram(s, t)
