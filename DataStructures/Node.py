''' Node.py implements a Node . Node is an element of a linked list'''

class Node:
    ''' Single linked node'''
    ''' REF page 142'''
    def __init__(self,item, next):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_item(self,item):
        self.item = item

    def set_next(self,next):
        self.next = next
    
    class Node:
        ''' Single linked node''' 
        def __init__(self, item,next):
            self.item = item
            self.next = next
        ''' Utility '''

class DoubleNode(Node):

    ''' DoubleNode inherits from Node'''
    def __init__(self,item,next,previous):
        super().__init__(item,next)
        self.previous = previous

    def get_previous(self):
        return self.previous

    def set_previous(self,previous):
        self.previous = previous
        