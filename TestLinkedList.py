
import random


class Link (object):
    # constructor
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next


class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__ (self):
        self.first = None

    # Get number of links of a singly Linked List.
    # "Input: [1, 2, 3, 4, 5, 6]"
    # "Expected: 6"
    # TODO!
    def get_num_links (self):
        current = self.first
        counter = 0
        while current:
            counter+=1
            current = current.next
        return counter
        

    # Add an item at the beginning of the list
    def insert_first (self, data):
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    # add an item at the end of a list
    def insert_last (self, data):
        newLink = Link(data)
        current = self.first
        
        if current == None:
            self.first = newLink
            return 
        
        while current.next != None:
            current = current.next
        current.next = newLink


    # Add an item in an ordered list in ascending order
    # Assume that the list is already sorted
    def insert_in_order (self, data):
        newLink = Link(data)
        current = self.first 
        
        if current == None:
            newLink.next = current
            self.first = newLink
            
            
        elif newLink.data < current.data:
            newLink.next = current
            self.first = newLink
            
        elif newLink.data > current.data:
            while newLink.data > current.data:
                current = current.next
            
            newLink.next = current.next
            current.next = newLink
            
     


    # Search in an unordered list, return None if not found
    def find_unordered (self, data):
        current = self.first 
        if current == None:
            return None
        
        while current.data != data:
            if current.next == None:
                return None
            else:
                current = current.next
        return current


    # Search in an ordered list, return None if not found
    def find_ordered (self, data):
        current = self.first 
        if current == None:
            return None
        
      
        while current.data < data:
            current = current.next
            if current.data == data:
                return current 
            else:
                return None
            
        
        
      
        
     



    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        string = ""
        count = 0
        curr = self.first
        if curr == None:
            return string

        while curr.next != None:
            string += str(curr.data)
            count += 1
            if count != 10:
                string += "  "
            else:
                string += "\n"
                count = 0
            curr = curr.next
        string += str(curr.data)
        return string

# This main function is just for your visualization and tests.
# The Gradescope system will get your Class and run tests on the methods.

def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    linked_List = LinkedList()
    for i in range(9, -1, -1):
        linked_List.insert_first(i)
    print(linked_List)

    # Test method insert_last()
    linked_List.insert_last(10)
    print(linked_List)

    # Test method insert_in_order()
    linked_List.insert_in_order(5)
    print(linked_List)

    # Test method get_num_links()
    num_links = linked_List.get_num_links()
    print(num_links)

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print(linked_List.find_unordered(3))
    print(linked_List.find_unordered(11))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print(linked_List.find_ordered(6))
    print(linked_List.find_ordered(12))

if __name__ == "__main__":
    main()

# python3 TestLinkedList.py
