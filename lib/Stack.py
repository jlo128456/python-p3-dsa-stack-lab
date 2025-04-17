class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit = limit
        self.items =[]

        for item in items:
            if len(self.items) < self.limit:
                self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
           self.items.append(item)
        else:
           return None
        

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None    

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None    
    
    def size(self):
        return len(self.items) 

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
           return len(self.items) - 1 - self.items.index(target)
        return -1  

