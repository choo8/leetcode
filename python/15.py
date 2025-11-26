class Solution:
    def threeSum(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        results = []

        for i in range(len(sorted_nums) - 2):
            if sorted_nums[i] > 0:
                break

            if i != 0 and sorted_nums[i - 1] == sorted_nums[i]:
                continue

            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                if sorted_nums[i] + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                elif sorted_nums[i] + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                else:
                    results.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    
                    left += 1
                    while left < len(sorted_nums) and sorted_nums[left - 1] == sorted_nums[left]:
                        left += 1

                    right -= 1
                    while right > 0 and sorted_nums[right + 1] == sorted_nums[right]:
                        right -= 1

        return results
    

if __name__ == "__main__":
    solution = Solution()

    nums = [-1,0,1,2,-1,-4]
    assert solution.threeSum(nums) == [[-1,-1,2],[-1,0,1]]

    nums = [0,1,1]
    assert solution.threeSum(nums) == []

    nums = [0,0,0]
    assert solution.threeSum(nums) == [[0,0,0]]
