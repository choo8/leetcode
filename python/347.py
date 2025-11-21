from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        heap = [(n_freq, n) for n, n_freq in freq.items()]
        heapq.heapify(heap)

        return [element[1] for element in heapq.nlargest(k, heap)]
    

if __name__ == "__main__":
    solution = Solution()

    nums = [1,1,1,2,2,3]
    k = 2
    assert solution.topKFrequent(nums, k) == [1, 2]

    nums = [1]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]

    nums = [1,2,1,2,1,2,3,1,3,2]
    k = 2
    assert solution.topKFrequent(nums, k) == [2, 1]
