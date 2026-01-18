from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next

        list_length = len(stack)

        cur = head
        for _ in range(list_length // 2):
            to_insert = stack.pop()

            next = cur.next
            cur.next = to_insert
            to_insert.next = next

            cur = next

        cur.next = None

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

    head = [1,2,3,4]
    head_ll = create_linked_list(head)
    solution.reorderList(head_ll)
    assert linked_list_to_list(head_ll) == [1,4,2,3]

    head = [1,2,3,4,5]
    head_ll = create_linked_list(head)
    solution.reorderList(head_ll)
    assert linked_list_to_list(head_ll) == [1,5,2,4,3]
