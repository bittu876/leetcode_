class MyQueue(object):

    def __init__(self):
        self.queue=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        return 

    def pop(self):
        """
        :rtype: int
        """
        x=self.queue[0]
        if len(self.queue) != 0:
            self.queue=self.queue[1:]
        return x
        

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()