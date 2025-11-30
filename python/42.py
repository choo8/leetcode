class Solution:
    def trap(self, height: list[int]) -> int:
        trapped_water = 0
        
        # Stores index of monotonically decreasing heights
        monotonic_stack = []
        for idx, h in enumerate(height):
            # If no wall on the left, don't need to consider 0 since we cannot trap water
            if len(monotonic_stack) == 0 and h == 0:
                continue

            if len(monotonic_stack) == 0 or height[monotonic_stack[-1]] > h:
                monotonic_stack.append(idx)
            else:
                while len(monotonic_stack) > 0 and height[monotonic_stack[-1]] <= h:
                    popped_idx = monotonic_stack.pop()
                    # No more trapped water to be added
                    if len(monotonic_stack) == 0:
                        break
                    max_height = min(height[monotonic_stack[0]], h)
                    trapped_water += (popped_idx - monotonic_stack[-1]) * (max_height - height[popped_idx])
                monotonic_stack.append(idx)
        return trapped_water
    

if __name__ == "__main__":
    solution = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert solution.trap(height) == 6

    height = [4,2,0,3,2,5]
    assert solution.trap(height) == 9
