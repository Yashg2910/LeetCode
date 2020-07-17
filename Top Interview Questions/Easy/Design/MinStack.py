class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack  = []
        self.min = float('inf')
        self.min_array = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if x<=self.min:
            self.min = x
            self.min_array.append(x)
        #print(self.stack)
        

    def pop(self):
        """
        :rtype: None
        """
        x = self.stack.pop()
        
        if x == self.min:
            del self.min_array[-1]
            
        if len(self.min_array)!=0:
            self.min = self.min_array[-1]
        else:
            self.min = float('inf')
            
        #print("Min array", self.min_array)
        #print(self.stack)
        return x
        

    def top(self):
        """
        :rtype: int
        """
        #print(self.stack)
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        #print(self.stack)
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()