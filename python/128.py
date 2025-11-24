class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set()
        nums_set = set(nums)

        longest = 0
        for n in nums:
            if n in seen:
                continue

            if n - 1 not in nums_set:
                offset = 1
                while True:
                    if n + offset in nums_set:
                        offset += 1
                    else:
                        break
                longest = max(longest, offset)
            
            seen.add(n)

        return longest
    

if __name__ == "__main__":
    solution = Solution()

    nums = [100,4,200,1,3,2]
    assert solution.longestConsecutive(nums) == 4

    nums = [0,3,7,2,5,8,4,6,0,1]
    assert solution.longestConsecutive(nums) == 9

    nums = [1,0,1,2]
    assert solution.longestConsecutive(nums) == 3
