class MyStack(object):

    def __init__(self):
        self.stack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        return None
    
    def pop(self):
        """
        :rtype: int
        """
        x=self.stack[len(self.stack)-1]
        if len(self.stack)  != 0:
            
            self.stack=self.stack[:len(self.stack)-1]
        return  x

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        print(self.stack)
        if len(self.stack) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()