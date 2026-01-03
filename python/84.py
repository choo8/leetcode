class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights = heights + [0]

        monotonic_stack = [-1]
        largest_area = 0

        for idx, h in enumerate(heights):
            while monotonic_stack[-1] != -1 and h < heights[monotonic_stack[-1]]:
                cur_height = heights[monotonic_stack.pop()]
                cur_width = idx - monotonic_stack[-1] - 1
                largest_area = max(largest_area, cur_height * cur_width)

            monotonic_stack.append(idx)

        return largest_area
    

if __name__ == "__main__":
    solution = Solution()

    heights = [2,1,5,6,2,3]
    assert solution.largestRectangleArea(heights) == 10

    heights = [2,4]
    assert solution.largestRectangleArea(heights) == 4
