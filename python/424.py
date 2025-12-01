from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        count_to_char = defaultdict(set)
        char_to_count = defaultdict(int)
        
        count_to_char[1].add(s[0])
        char_to_count[s[0]] += 1 

        left, right = 0, 1
        while right < len(s):
            # Update dicts
            char_to_count[s[right]] += 1
            count_to_char[char_to_count[s[right]]].add(s[right])

            cur_len = right - left + 1
            while left < right and len(count_to_char[max(1, cur_len - k)]) == 0:
                count_to_char[char_to_count[s[left]]].remove(s[left])
                char_to_count[s[left]] -= 1
                left += 1

                cur_len = right - left + 1

            longest = max(longest, cur_len)

            # Update right pointer
            right += 1

        return longest
    

if __name__ == "__main__":
    solution = Solution()

    s = "ABAB"
    k = 2
    assert solution.characterReplacement(s, k) == 4

    s = "AABABBA"
    k = 1
    assert solution.characterReplacement(s, k) == 4
