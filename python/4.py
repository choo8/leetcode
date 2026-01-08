import heapq


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        lower_heap, upper_heap = [], []

        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) or ptr2 < len(nums2):
            if ptr1 == len(nums1):
                next = nums2[ptr2]
                ptr2 += 1
            elif ptr2 == len(nums2):
                next = nums1[ptr1]
                ptr1 += 1
            else:
                next1, next2 = nums1[ptr1], nums2[ptr2]
                if next1 <= next2:
                    next = next1
                    ptr1 += 1
                else:
                    next = next2
                    ptr2 += 1

            # First element
            if len(upper_heap) == 0:
                upper_heap.append(next)
                continue

            median = self._get_median(lower_heap, upper_heap)
            if next == median:
                if len(lower_heap) == len(upper_heap):
                    heapq.heappush(upper_heap, next)
                else:
                    heapq.heappush(lower_heap, -next)
            elif next < median:
                if len(lower_heap) == len(upper_heap):
                    popped = -heapq.heappop(lower_heap)
                    heapq.heappush(upper_heap, popped)
                    heapq.heappush(lower_heap, -next)
                else:
                    heapq.heappush(lower_heap, -next)
            else:
                if len(lower_heap) == len(upper_heap):
                    heapq.heappush(upper_heap, next)
                else:
                    popped = heapq.heappop(upper_heap)
                    heapq.heappush(lower_heap, -popped)
                    heapq.heappush(upper_heap, next)
        
        return self._get_median(lower_heap, upper_heap)
    
    def _get_median(self, lower_heap: list[int], upper_heap: list[int]) -> float:
        if len(lower_heap) == len(upper_heap):
            return (upper_heap[0] + -lower_heap[0]) / 2
        else:
            return upper_heap[0]


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,3]
    nums2 = [2]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.00000

    nums1 = [1,2]
    nums2 = [3,4]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.50000