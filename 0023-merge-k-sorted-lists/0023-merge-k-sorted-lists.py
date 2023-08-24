# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res=[]
        for i in range(len(lists)):
            j=lists[i]
            temp=[]
            while j!=None:
                temp.append(j.val)
                j=j.next
            res.append(temp)
        print(res)
        tmp_lst=[]
        for i in res:
            tmp_lst+=i
        tmp_lst.sort()
        print(tmp_lst)
        rslt=ListNode("")
        for i in range(0,len(tmp_lst)):
            if i==0:
                res=ListNode()
                res.val=tmp_lst[i]
                rslt=res
            else:
                res.next=ListNode()
                res=res.next
                res.val=tmp_lst[i]

        return rslt
                
