from python.data_structures.double_linked_list import DoubleLinkedList


class Queue(DoubleLinkedList):
    
    def __init__(self):
        super().__init__()
   
    def enqueue(self,item : object) -> None:
        self.add_at_end(item)
        
    def dequeue(self) -> object:
        return self.delete_from_beginning()
    
    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False
    
    def print_queue(self) -> None :
        super().print_list()        
    
    def insert_at_beginning(self,item):
        raise NotImplementedError("Insert at Begining is not allowed in Queues")

    def insert(self, pos, item):
        raise NotImplementedError("This operation is not allowed in Queue.")

    def delete(self, pos):
        raise NotImplementedError("This operation is not allowed in Queue.")

    

    def delete_from_end(self):
        raise NotImplementedError("This operation is not allowed in Queue.")