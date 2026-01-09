from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        cur = head
        next = head.next
        prev = None
        while True:
            # Reached end of linked list
            if next is None:
                cur.next = prev
                break

            # Update current element
            cur.next = prev

            # Update pointers
            prev = cur
            cur = next
            next = cur.next

        return cur


def create_linked_list(arr: list[int]) -> Optional[ListNode]:
    """Converts a Python list [1,2,3] into a Linked List 1->2->3."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(node: Optional[ListNode]) -> list[int]:
    """Converts a Linked List 1->2->3 back into a Python list [1,2,3]."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    solution = Solution()

    head = [1,2,3,4,5]
    assert linked_list_to_list(solution.reverseList(create_linked_list(head))) == [5,4,3,2,1]

    head = [1,2]
    assert linked_list_to_list(solution.reverseList(create_linked_list(head))) == [2,1]

    head = []
    assert linked_list_to_list(solution.reverseList(create_linked_list(head))) == []
