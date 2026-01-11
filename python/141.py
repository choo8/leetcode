from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

            if slow and fast and slow == fast:
                return True

        return False


def create_linked_list_with_cycle(arr: list[int], pos: int) -> Optional[ListNode]:
    """
    Creates a linked list from an array.
    If pos is >= 0, creates a cycle connecting the tail to the node at index pos.
    """
    if not arr:
        return None
    
    # 1. Create all nodes first and store them to easily access by index
    nodes = [ListNode(val) for val in arr]
    
    # 2. Link the nodes linearly
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    
    # 3. Create the cycle if pos is valid
    if pos != -1 and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
        
    return nodes[0]


if __name__ == "__main__":
    solution = Solution()

    head = [3,2,0,-4]
    pos = 1
    assert solution.hasCycle(create_linked_list_with_cycle(head, pos))

    head = [1,2]
    pos = 0
    assert solution.hasCycle(create_linked_list_with_cycle(head, pos))

    head = [1]
    pos = -1
    assert not solution.hasCycle(create_linked_list_with_cycle(head, pos))
