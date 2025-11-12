class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        smallest = nums[0]
        max_diff = -1

        for i in range(1, len(nums)):
            if nums[i] - smallest > 0: 
                max_diff = max(max_diff, nums[i] - smallest)
            smallest = min(smallest, nums[i])

        return max_diff
    

if __name__ == "__main__":
    solution = Solution()

    nums = [7, 1, 5, 4]
    assert solution.maximumDifference(nums) == 4

    nums = [9, 4, 3, 2]
    assert solution.maximumDifference(nums) == -1

    nums = [1, 5, 2, 10]
    assert solution.maximumDifference(nums) == 9
