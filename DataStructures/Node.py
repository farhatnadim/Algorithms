''' Node.py implements a Node . Node is an element of a linked list'''
from math import inf
import copy
class Node:
    ''' Single linked node'''
    ''' REF page 142'''
    def __init__(self,item : object , next = None):
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
    def __init__(self,item : object,next=None,previous=None):
        super().__init__(item,next)
        self.previous = previous

    def get_previous(self):
        return self.previous

    def set_previous(self,previous):
        self.previous = previous
  
class Vertex:
      def __init__(self, edges=[],explored=False, distance = inf ):
          self.explored = explored
          self.edges=edges
          self.distance = distance
    
      def set_explored(self) -> None:
          self.explored = True    
      
      def set_unexplored(self) -> None:
          self.unexplored = False
      
      def is_explored(self) -> bool:
          return self.explored 
      
      def get_edges(self) -> list:
          return self.edges
      
      def set_edges(self,edges:list) -> None:
          self.edges = edges
     
      def copy(self)-> object :
         return copy.deepcopy(self)
          
      
