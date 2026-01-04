import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if self._canFinish(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        
        return left

    
    def _canFinish(self, piles, h: int, k: int) -> bool:
        time_taken = 0
        for p in piles:
            time_taken += math.ceil(p / k)
        return time_taken <= h
    

if __name__ == "__main__":
    solution = Solution()

    piles = [3,6,7,11]
    h = 8
    assert solution.minEatingSpeed(piles, h) == 4

    piles = [30,11,23,4,20]
    h = 5
    assert solution.minEatingSpeed(piles, h) == 30

    piles = [30,11,23,4,20]
    h = 6
    assert solution.minEatingSpeed(piles, h) == 23
