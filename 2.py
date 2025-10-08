#Add two number
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def LTL(listp):
    dummy = ListNode(0)
    index = dummy

    for i in listp:
        index.next = ListNode(int(i))
        index = index.next

    return dummy.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lista = []
        listb = []
        numA = 0
        numB = 0

        head = l1
        current = head

        while current is not None:
            n = current.val
            lista.append(n)
            current = current.next

        lista.reverse()
            
        head = l2
        current = head

        while current is not None:
            n = current.val
            listb.append(n)
            current = current.next
        
        listb.reverse()

        for i in lista:
            numA = numA * 10 + i

        for i in listb:
            numB = numB * 10 + i

        sumA = numA + numB 
        sumAList = str(sumA)[::-1]
        n = LTL(sumAList)
        return n

        