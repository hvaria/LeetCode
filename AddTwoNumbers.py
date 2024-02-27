class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        head = ListNode()
        current = head
        carry = 0

        while l1 or l2 or carry:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value + carry
            carry, val = divmod(total, 10)
            current.next = ListNode(val)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        return head.next

    @staticmethod
    def listToLinkedList(elements):
        head = ListNode(0)
        current = head
        for element in elements:
            current.next = ListNode(element)
            current = current.next
        return head.next

l1_list = [2,4,3]
l2_list = [5,6,4]
l1 = Solution.listToLinkedList(l1_list)
l2 = Solution.listToLinkedList(l2_list)


answer = Solution.addTwoNumbers(l1, l2)


def printLinkedList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

printLinkedList(answer)
