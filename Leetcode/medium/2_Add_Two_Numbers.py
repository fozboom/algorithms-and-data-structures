from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        before_first = ListNode()
        curr = before_first
        to_add = 0

        while l1 and l2:
            res_val = l1.val + l2.val + to_add
            to_add = res_val // 10
            new_node = ListNode(res_val % 10)
            curr.next = new_node
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            res_val = l1.val + to_add
            to_add = res_val // 10
            new_node = ListNode(res_val % 10)
            curr.next = new_node
            curr = curr.next

            l1 = l1.next

        while l2:
            res_val = l2.val + to_add
            to_add = res_val // 10
            new_node = ListNode(res_val % 10)
            curr.next = new_node
            curr = curr.next

            l2 = l2.next

        if to_add:
            new_node = ListNode(to_add)
            curr.next = new_node

        return before_first.next


def create_linked_list(values: list[int]) -> Optional[ListNode]:
    head = ListNode(values[0])
    curr = head
    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head


def print_linked_list(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('None')


num1 = create_linked_list([7, 2, 3])
print_linked_list(num1)

num2 = create_linked_list([9, 6])
print_linked_list(num2)

s = Solution()
res = s.addTwoNumbers(num1, num2)

print_linked_list(res)
