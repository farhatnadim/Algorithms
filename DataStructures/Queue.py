from DoubleLinkedList import DoubleLinkedList, DoubleNode


class Queue(DoubleLinkedList):
    
    def __init__(self):
        super.__init__()
    
    def enqueue(self,item : float | int | str) -> None:
        self.add_at_end(item)
        
    def dequeue(self) -> float | int | str :
        return self.delete_from_beginning()        
    
    
    
    '''ef insert_at_beginning(self, item):
        raise NotImplementedError("This operation is not allowed in Queue.")

    def insert(self, pos, item):
        raise NotImplementedError("This operation is not allowed in Queue.")

    def delete(self, pos):
        raise NotImplementedError("This operation is not allowed in Queue.")

    def add_at_end(self, item):
        raise NotImplementedError("Use 'enqueue' method instead.")

    def delete_from_end(self):
        raise NotImplementedError("This operation is not allowed in Queue.")'''