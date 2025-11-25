# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = 0
        number2 = 0
        i = 1 
        while l1.next!=None:
            number1 = number1 + l1.val*i
            i = i*10
            l1 = l1.next
        number1 = number1 + l1.val*i
        i = 1
        while l2.next!=None:
            number2 = number2 + l2.val*i
            i = i*10
            l2 = l2.next 
        number2 = number2+l2.val*i
        sum_nums = int(number1 + number2)
        return_ll = ListNode()
        head = return_ll
        div = 10
        while sum_nums!=0:
            val = sum_nums%div
            sum_nums = sum_nums//div
            head.val = val
            if sum_nums==0:
                head.next=None
            else:
                head.next = ListNode()
                head = head.next
        return return_ll
