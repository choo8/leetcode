class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # Numbers left of mid are sorted
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
    

if __name__ == "__main__":
    solution = Solution()

    nums = [4,5,6,7,0,1,2]
    target = 0
    assert solution.search(nums, target) == 4

    nums = [4,5,6,7,0,1,2]
    target = 3
    assert solution.search(nums, target) == -1

    nums = [1]
    target = 0
    assert solution.search(nums, target) == -1
