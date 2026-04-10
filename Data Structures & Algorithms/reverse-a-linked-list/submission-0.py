# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        print(arr)
        
        # new_head = ListNode(-1)
        # ans = new_head
        # while arr:
        #     ans.next = ListNode(arr.pop())
        #     ans = ans.next

        # return new_head.next 
        ans = None 
        for i in arr:
            node = ListNode(i)
            node.next = ans
            ans = node

        return ans



            


        
 