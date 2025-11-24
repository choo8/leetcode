class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = "".join(filter(str.isalnum, s.lower()))
        return alpha_s == alpha_s[::-1]
    
if __name__ == "__main__":
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s)

    s = "race a car"
    assert not solution.isPalindrome(s)

    s = " "
    assert solution.isPalindrome(s)
