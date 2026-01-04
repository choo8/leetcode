class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[right]
    

if __name__ == "__main__":
    solution = Solution()

    nums = [3,4,5,1,2]
    assert solution.findMin(nums) == 1

    nums = [4,5,6,7,0,1,2]
    assert solution.findMin(nums) == 0

    nums = [11,13,15,17]
    assert solution.findMin(nums) == 11
