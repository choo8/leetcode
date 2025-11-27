class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, min_height * (right - left))

            if height[left] <= height[right]:
                cur_height = height[left]
                while left < right and height[left] <= cur_height:
                    left += 1
            elif height[left] > height[right]:
                cur_height = height[right]
                while right > left and height[right] <= cur_height:
                    right -= 1

        return max_area
    

if __name__ == "__main__":
    solution = Solution()

    height = [1,8,6,2,5,4,8,3,7]
    assert solution.maxArea(height) == 49

    height = [1,1]
    assert solution.maxArea(height) == 1
