class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size=k
        self.cir_deque=[]
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.cir_deque) < self.size :
            self.cir_deque.insert(0,value)
            return True
        else:
            return False
        
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.cir_deque) < self.size  :
            self.cir_deque.append(value)
            return True
        else:
            return False
        
    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.cir_deque) != 0:
            self.cir_deque=self.cir_deque[1:len(self.cir_deque)]
            return True
        else:
            return False
        
    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.cir_deque) != 0:
            self.cir_deque=self.cir_deque[:len(self.cir_deque)-1]
            return True
        else:
            return False

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.cir_deque) != 0: 
            return self.cir_deque[0]
        else:
            return -1
        

    def getRear(self):
        """
        :rtype: int
        """
        if len(self.cir_deque) != 0: 
            return self.cir_deque[len(self.cir_deque)-1]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.cir_deque) != 0:
            return False
        else:
            return True
        

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.cir_deque) == self.size:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()