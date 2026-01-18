from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        delay = n + 1
        length = 0

        while fast:
            fast = fast.next
            length += 1

            if delay == 0:
                slow = slow.next
            else:
                delay -= 1

        if n == length:
            return head.next
        else:
            next = slow.next
            slow.next = next.next
            return head
    

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
    n = 2
    assert linked_list_to_list(solution.removeNthFromEnd(create_linked_list(head), n)) == [1,2,3,5]

    head = [1]
    n = 1
    assert linked_list_to_list(solution.removeNthFromEnd(create_linked_list(head), n)) == []

    head = [1,2]
    n = 1
    assert linked_list_to_list(solution.removeNthFromEnd(create_linked_list(head), n)) == [1]
