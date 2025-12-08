from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1) - 1
        
        char_dict = defaultdict(int)
        for c in s1:
            char_dict[c] += 1

        while right < len(s2):
            failed = False

            for i in range(left, right + 1):
                if char_dict[s2[i]] <= 0:
                    failed = True
                    break
                else:
                    char_dict[s2[i]] -= 1
            
            if not failed:
                return True
                
            for j in range(left, i):
                char_dict[s2[j]] += 1
            
            if char_dict[s2[i]] == 0:
                left = i + 1
                right = i + len(s1)
            else:
                left += 1
                right += 1

        return False
    

if __name__ == "__main__":
    solution = Solution()

    s1 = "ab"
    s2 = "eidbaooo"
    assert solution.checkInclusion(s1, s2)

    s1 = "ab"
    s2 = "eidboaoo"
    assert not solution.checkInclusion(s1, s2)

    s1 = "adc"
    s2 = "dcda"
    assert solution.checkInclusion(s1, s2)
