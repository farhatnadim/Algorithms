import math # has -inf and +inf variables defined

from Node import DoubleNode

__liscence__ = "MIT"
__revision__ = "v.01"
__author__ = "Nadim Farhat nadim.farhat@gmail.com"

class DoubleLinkedList:
    r""" This class defines the API for a double linked list as defined by Sedgwick et all and Cormen et all

    Definition of a double linked list:

    Each node has a previous reference points to the previous node
    Each node has a next reference to the next node
    The previous reference of the "head" of Double Linked List points to None
    The next reference of the "head" of Double Linked List points to next node in the linked list
    The previous reference of the "tail" of Double Linked List points to precedent node
    The next reference of the "tail" of Double Linked List points to None

    Textbook definitions :
    def 1:  linked list is a recursive data structure that is either empty
    or a reference to a node having a generic item and a reference to a linked list Sedgwick et all "Algorithm 4th edition" 
    def 2 : linked list is data structure in which objects are arranged in a linear order, Unlike an array where the order i
    is determined by the indices. The order in a linked list is determeind by a pointer in each object . Linked list a part of dynamic sets and can grow and shrink depending on the need of a program
    The access to a linked list memory is not necessarilly contiguous therefore it might be slower than arrays "Introduction to Algorithms" 3rd Edition"
    """

    ########################################## Basic functionality ###########################################
    def __init__(self,head = None, tail=None, size = 0):
        """ Initializes an empty list """
        self.head = head
        self.tail = tail
        self.size = 0
       

    def get_head(self):
        """ Returns the first node/head in the linked list """
        return self.head
    
    def set_head(self,head_ref):
        """ Sets the head of the linked list to a node. 

        Keyword arguments:
        head_ref : reference to an object of type node
        """
        
        self.head = head_ref
    
    def get_tail(self):
        """ Returns the last node in the linked list """
        return self.tail
    
    def set_tail(self,tail_ref):
        """ Sets the head of the linked list to a node. 

        Keyword arguments:
        head_ref : reference to an object of type node
        """
        self.tail = tail_ref
    
    def get_size(self):
        """ Returns the size of the linked list """
        return self.size

    def set_size(self,new_size):
        """ set the size of the linked list """
        self.size = new_size

    ####################################### Expanded Functionality #################################################
    # computational complexity o(1)
    ######################################################################################################
    def insert_at_beginning(self, item):
        """ inserts a node containing item before the head.
            the head will point to the new node.

        Keyword arguments:
        param : item  can be of any type 
        """
        #  If the list is empty 
        if (self.size == 0):
        # Make is a one node list where head and tail are the same
            new_node  = DoubleNode(item,None,None)
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return 0
        # If the list is not empty 
        new_node = DoubleNode(item,self.head,None)
        # Inserts before the current head
        self.head.previous = new_node
        # Assigns head to the new node
        self.head = new_node
        self.size += 1
        return 0

    
    # computational complexity o(n)
    def traverse_list(self):
        """ Iterates from the begining of the double list till end
            sets the tail for the linked list """

        # Empty list   
        if self.size == 0:
            print("Linked List is empty")
            return - 1
        # Starts at the head
        current = self.head
        # Until we reach the tail, only at tail next == None
        while(current.get_next() != None):
            current = current.get_next()
        # Sets the tail
        self.tail = current
        
        return 0
    def to_array(self):
        """ returns an array made from the dLinkedList 
            Mostly for testing purposes, this function converts a list
            to an array/or list

        Keyword arguments:
        return : array 

        """
        array = []
        # Empty list   
        if self.size == 0:
            print("Linked List is empty")
            return - 1
        # Starts at the head
        current = self.head
        # Until we reach the tail, only at tail next == None
        while(current.get_next() != None):
            array.append(current.get_item())
            current = current.get_next()
            
        # Sets the tail
        self.tail = current
        array.append(current.get_item())
        #returns array
        return array
    
    def reverse_traverse_list(self):
        """ Iterates from the end of the double list till the begining
            sets the head for the linked list """
        # Empty list
        if self.size == 0:
            print("Linked list is empty")
            return - 1
        # Starts at the tail
        current = self.tail
        # Untill we reach the head, only at head previous == None
        while(current.get_previous() != None):
            current = current.get_previous()
        # Sets the head
        self.head = current
        return 0
    

    def reverse_convert_array(self):
        """ returns the double linked list in an array reversed

        Keyword arguments:
        return : reversed_array 
        """
        reversed_array = []
        # Empty list
        if self.size == 0:
            print("Linked list is empty")
            return - 1
        # Starts at the tail
        current = self.tail
        # Untill we reach the head, only at head previous == None
        while(current.get_previous() != None):
            reversed_array.append(current.get_item())
            current = current.get_previous()
        # Sets the head
        self.head = current
        reversed_array.append(current.get_item())
        return reversed_array
    
    def print_list(self):
        """ prints the content of the list """
        # Empty list
        if self.size == 0:
            print("Linked List is empty")
            return - 1
        # Starts at head
        current = self.head
        print(current.get_item(),end=" ")
        # Print all elements until the end
        while(current.get_next() != None):
            current = current.get_next()
            print(current.get_item(),end=" ")
        print("\n")
        return 0

    def reverse_print_list(self):
        """ prints the content of the list """
        # Empty list
        if self.size == 0:
            print("Linked List is empty")
            return - 1
        # Starts at tail
        current = self.tail
        print(current.get_item())
        # Print all elements until the end
        while(current.get_previous() != None):
            current = current.get_previous()
            print(current.get_item())
        return 0

    # computational complexity o(n)
    def add_at_end(self,item):
        """ Adds a node to the end of the double linked list

            The tail will point to the new node.

        Keyword arguments:
        param : item  can be of any type 
        """
        # Empty list
        if self.size == 0:
            new_node  = DoubleNode(item,None,None)
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return 0

        node = DoubleNode(item,None,self.tail) # since it is an end node
        self.tail.set_next(node)
        self.tail = node
        self.size += 1
        return 0

    
    def insert(self,pos,item):
        """ inserts a node containing item BEFORE a certain position
        this function uses the power of double linked list. since we have two pointers we either
        iterate from the head or tail depending on the size and the position
        so O(n/2)

        Keyword arguments:
        pos : a postive integer of the position
        param : item  can be of any type 

        """
        # Invalid size
        if  self.size == 0:
            print(f"Empty list @ function insert")
            return -1

        # Invalid position
        if  pos < 0 or pos > (self.size -1):
            print("Invalid position")
            return -1

        # At head
        if  pos == 0:
            self.insert_at_beginning(item)
            # Update the size
            self.size += 1
            return 0

        # any other position ( size and position are valid )

        new_node = DoubleNode(item,None,None)
        # since we are mantaining a head and a tail and the size, at most insert at pos
        # is n/2
        # if the position belongs to the first half of the list start from the head 

        if pos < (math.ceil(self.size/ 2.0)):
            current = self.head
            for position in range(pos-1):
                current = current.get_next()
            # Insert the node            
            new_node.set_next(current.get_next())
            new_node.set_previous(current)
            current.get_next().set_previous(new_node)
            current.set_next(new_node)
            # Update the size
            self.size += 1
        # else the position belong to the second half of the list, start from the tail
        else:
            current = self.tail
            for position in range((self.size - pos)):
                current = current.get_previous()
            # Insert the node 
            new_node.set_next(current.get_next())
            new_node.set_previous(current)
            current.get_next().set_previous(new_node)
            current.set_next(new_node)
            # Update the size
            self.size += 1
        return 0
            
    def delete_from_beginning(self):
        """ deletes the first node/head 
        
        the head will point to the next node

        """
        if self.size == 0: # empty list
            return None
        # single node, tail and head point to the same node
        if self.size == 1:
            item = self.head.get_item() 
            self.head = None
            self.tail = None
            self.size += -1
            return item
        #multiple nodes, tail and head point to different nodes
        item = self.head.get_item()
        self.head = self.head.get_next()
        self.head.get_previous().set_next(None)
        self.head.set_previous(None)
        self.size += -1
        return item
    
    def delete_from_end(self):
        """ delete the last node/tail

        the tail will point to the previous node
        """
        # Empty list
        if self.size == 0:
           return - 1
        # One node
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size += -1
            return 0
        # multiple nodes
        self.tail = self.tail.get_previous()
        self.tail.set_next(None)
        self.size += -1
        return 0

    #TODO: check the return    
    def delete(self, pos):
        """ delete at a position

        the tail will point to the previous node
        """
        # Empty List
        if self.size == 0:
            return -1
        # Invalid position
        if pos < 0 or pos > self.size -1:
            print("Invalid Position")
            return -1
        # Special case of one node is taken care of 
        # with delete_from_beginning 
        if pos == 0:
            return self.delete_from_beginning()
            
        
        # Special case of one node is taken care of 
        # with delete_from_end    
        if pos == self.size -1:
            return self.delete_from_end()
        
        # We are going to use the fact we have a head and tail references
        # if pos < size/2 +1 (if odd) , the head 
        if pos < (math.ceil(self.size/ 2.0)):
            current = self.head
            for position in range(pos-1):
                current = current.get_next()
            # Delete the node            
            current.set_next(current.get_next().get_next())
            current.get_next().set_previous(current)
            # Update the size
            self.size += -1
        # Else the position belong to the second half of the list, start from the tail
        else:
            current = self.tail
            for position in range((self.size - pos)):
                current = current.get_previous()
            # Delete the node 
            current.set_next(current.get_next().get_next())
            current.get_next().set_previous(current)
            # Update the size
            self.size += -1
        return 0
            
        
    def search(self,key): 
        ''' Returns a reference to a node containing key

        '''
        current = self.head
        if current.get_item() == key: # first case 
            return current
        while(current != None):
            if (current.get_item() == key):
                return current
            current = current.get_next()
            
        # reached end and did not find the key returning None
        return None
    
   

    
class LinkedNumber(DoubleLinkedList):
    '''Inherits SimpleLinkedList , adds some functionality for number'''
    def __init__(self,head = None,tail=None,max=0,min = 0,size =0):
        super().__init__(head,tail,size)
        self.min = 0 
        self.max = 0

    def getMax(self):
        ''' Returns the node that contains the highest value '''
        return self.max

    def getMin(self):
        ''' Returns the node that contains the highest value '''
        return self.min

    def minimum(self): #
        """ Returns the minimum of an unsorted linked list """
        if self.head == None:
            print("Emtpy list ")
            return -1
        if self.head.get_next() == None:
            return self.head
        
        minimum = math.inf
        
        current = self.head
        ref_to_minimum = None
        
        while(current  != None):
            if (current.get_item() < minimum):
                minimum = current.get_item()
                ref_to_minimum = current     
            current = current.get_next()
            
        self.min = ref_to_minimum
        
    def maximum (self): # to implement after implementing a sort
        """ Returns the maximum of an unsorted linked list """

        if self.head == None:
            print("Emtpy list ")
            return - 1
        if self.head.get_next() == None:
            return self.head
        
        maximum = -math.inf
        
        current = self.head
        ref_to_max = None
        
        while(current != None):
            if (current.get_item() > maximum):
                maximum = current.get_item()
                ref_to_max = current
            current = current.get_next()
            
        self.max = ref_to_max
    

    # there are plenty of way to implement successor,
    # first method is to find max, and remove it then run max again o(n^2)
    # second method is find max and make sure successor is less than max but bigger than anythong else o(n^2)
    # third method is find max and it successor in one pass by maintaining two variable  max and successor o(n)
    # could be other methods i am not sure, please let me know any 


    def successor(self): # o(2n) worst case ! o(n) is max is in the begining

        """Returns the second larget number in a double linked list """
        successor_ref = None
        if self.head == None:
            print("Emtpy list ")
            return - 1
        if self.head.get_next() == None:
            return - 1
        
        second_maximum = -math.inf 
        
        current = self.head
        self.maximum()
        max = self.getMax()
        while(current != None):
            if (current is max):
                current = current.get_next() # skip
            elif (current.get_item() > second_maximum):
                second_maximum = current.get_item()
                successor_ref = current
               
                current = current.get_next()
            else:
                current = current.get_next()


        return successor_ref 
        

    def predecessor(self):
        """ Return second smallest number in an unsorted linked list """
        predecessor_ref = None
        if self.head == None:
            print("Emtpy list ")
            return - 1
        if self.head.get_next() == None:
            return - 1
        
        second_minimum = + math.inf 
        
        current = self.head
        self.minimum()
        min = self.getMin()
        while(current != None):
            if (current is min):
                current = current.get_next() # skip
            elif (current.get_item() < second_minimum):
                
                second_minimum = current.get_item()
                predecessor_ref= current
               
                current = current.get_next()
            else:
                current = current.get_next()

        return predecessor_ref
    
    def insertionSort(self) -> None:
        """ Sorts a double linked list using insertion sort """
        current = self.head.get_next() # start from the second element
        while current is not None:
            # start from the second node 
            temp = current  #save the node
            is_sorted = False 
            while not is_sorted:
                if current.get_previous() is not None and current.item < current.get_previous().item:
                    current.item, current.previous.item = current.previous.item, current.item
                    current = current.get_previous()
                else:
                    is_sorted = True
            current = temp.get_next()



        