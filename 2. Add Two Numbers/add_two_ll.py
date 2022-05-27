# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_node=ListNode() #create a node
        curr=new_node # create a pointer to point to the node 
        
        carry=0
        while l1 or l2 or carry: #while l1 , l2 has elements in the list
            v1= l1.val if l1 else 0
            v2 =l2.val if l2 else 0
            
            sum = v1+v2+carry #sum the values 
            carry= sum//10 
            sum = sum%10
            curr.next =ListNode(sum)# append new nodes the head
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return new_node.next
