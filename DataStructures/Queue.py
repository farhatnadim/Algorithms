from DoubleLinkedList import DoubleLinkedList, DoubleNode


class Queue(DoubleLinkedList):
    
    def __init__(self):
        super().__init__()
   
    def enqueue(self,item : float | int | str) -> None:
        self.add_at_end(item)
        
    def dequeue(self) -> float | int | str :
        return self.delete_from_beginning()
    
    def print_queue(self) -> None :
        self.print_list()        
    
    def insert_at_beginning(self,item):
        raise NotImplemented("Insert at Begining is not allow in Queues")

    def insert(self, pos, item):
        raise NotImplementedError("This operation is not allowed in Queue.")

    def delete(self, pos):
        raise NotImplementedError("This operation is not allowed in Queue.")

    

    def delete_from_end(self):
        raise NotImplementedError("This operation is not allowed in Queue.")
    
  
    
'''    
def main():
    q = Queue()
    q.enqueue(10)
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(12)
    q.enqueue(1)
    q.print_queue()
    print(q.dequeue())
    q.print_queue()
    print(q.dequeue())
    q.print_queue()
    print(q.dequeue())
    q.print_queue()
    print(q.dequeue())
    q.print_queue()
    print(q.dequeue())
    q.print_queue()
if __name__ == "__main__":
    main()
'''