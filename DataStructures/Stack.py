from DoubleLinkedList import DoubleLinkedList


class Stack(DoubleLinkedList):
    
    def __init__(self):
        super().__init__()
   
    def push(self,item : object) -> None:
        self.add_at_end(item)
        
    def pop(self) -> object:
        if  not self.is_empty():
            
            return self.delete_from_end()
    
    def is_empty(self) -> bool:
        if self.size == 0:
            print("Stack is empty")
            return True
    
    def print_stack(self) -> None :
        self.print_list()        
    
    def insert_at_beginning(self,item):
        raise NotImplemented("Insert at Begining is not allow in Stack.")

    def insert(self, pos, item):
        raise NotImplementedError("This operation is not allowed in Stack.")

    def delete(self, pos):
        raise NotImplementedError("This operation is not allowed in Stack.")

  
    
   
def main():
   s = Stack()
   s.push(3)
   s.push(4)
   s.print_stack()
   s.pop()
   s.print_stack()
   s.pop()
   s.pop()
   
if __name__ == "__main__":
    main()