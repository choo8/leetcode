from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        cur_chars = defaultdict(int)
        cur_chars[s[0]] += 1
        max_length = 1
        left, right = 0, 1

        while right < len(s):
            while cur_chars[s[right]] > 0:
                cur_chars[s[left]] -= 1
                left += 1

            cur_chars[s[right]] += 1
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
    

if __name__ == "__main__":
    solution = Solution()

    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s) == 3

    s = "bbbbb"
    assert solution.lengthOfLongestSubstring(s) == 1

    s = "pwwkew"
    assert solution.lengthOfLongestSubstring(s) == 3
