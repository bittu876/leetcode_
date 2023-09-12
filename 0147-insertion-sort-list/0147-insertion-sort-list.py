# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = []
        temp = head
        #retriving all elements i n linked list
        while temp != None:
            nums.append(temp.val)
            temp = temp.next
        #sorting list using insertion sort algorithm
        for i in range(1,len(nums)):
            low = nums[i]
            for j in range(i-1,-1,-1):
                if low < nums[j]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
        #convrting sorted list to linked list
        ref = ListNode(nums[0])
        res =ref  
        j = 1
        while j < len(nums):
            ref.next = ListNode(nums[j])
            ref = ref.next
            j = j + 1
        return res
        