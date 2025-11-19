class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for idx, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], idx]
            seen[n] = idx

        return []
    

if __name__ == "__main__":
    solution = Solution()

    nums = [2,7,11,15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1]

    nums = [3,2,4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]

    nums = [3,3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1]
