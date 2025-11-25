class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
    

if __name__ == "__main__":
    solution = Solution()

    numbers = [2,7,11,15]
    target = 9
    assert solution.twoSum(numbers, target) == [1,2]

    numbers = [2,3,4]
    target = 6
    assert solution.twoSum(numbers, target) == [1,3]

    numbers = [-1,0]
    target = -1
    assert solution.twoSum(numbers, target) == [1,2]
