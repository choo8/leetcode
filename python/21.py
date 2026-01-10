from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        head, cur = None, None

        while ptr1 is not None or ptr2 is not None:
            if ptr1 is not None and ptr2 is not None:
                if ptr1.val < ptr2.val:
                    next = ptr1
                    ptr1 = ptr1.next
                else:
                    next = ptr2
                    ptr2 = ptr2.next
            elif ptr1 is not None:
                next = ptr1
                ptr1 = ptr1.next
            elif ptr2 is not None:
                next = ptr2
                ptr2 = ptr2.next

            if not head:
                head = next
                cur = next
            else:
                cur.next = next
                cur = next

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

    list1 = [1,2,4]
    list2 = [1,3,4]
    assert linked_list_to_list(solution.mergeTwoLists(create_linked_list(list1), create_linked_list(list2))) == [1,1,2,3,4,4]

    list1 = []
    list2 = []
    assert linked_list_to_list(solution.mergeTwoLists(create_linked_list(list1), create_linked_list(list2))) == []

    list1 = []
    list2 = [0]
    assert linked_list_to_list(solution.mergeTwoLists(create_linked_list(list1), create_linked_list(list2))) == [0]
