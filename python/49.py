class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in groups:
                groups[sorted_s] = [s]
            else:
                groups[sorted_s].append(s)

        return [group for group in groups.values()]
    

if __name__ == "__main__":
    solution = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    assert solution.groupAnagrams(strs) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    strs = [""]
    assert solution.groupAnagrams(strs) == [[""]]

    strs = ["a"]
    assert solution.groupAnagrams(strs) == [["a"]]
