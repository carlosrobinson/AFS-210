class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

my_list = ['May', 'the', 'force', 'be', 'with', 'you', '!']

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list                                           
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head != None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.count = self.count + 1

    def addLast(self, data) -> None:
        # Add a node at the end of the list
        # create new node
        new_node = Node(data)
        # Points to null
        new_node.next = None
        # check if there s a tail
        
        if self.tail != None:
            new_node.prev = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.count = self.count + 1
        

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        new_node = Node(data)
        
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        if (index == self.count):
            return self.addLast(data)
        # If index is greater than the length, the data will not be inserted.
        if (index > self.count):
            return 'Out of range'
        # This function does not replace the data at the index, but pushes everything else down.
        if index == 0:
            return self.addFirst(data)
        cur = self.head
        location = 0
        while cur.next and location < index:
            cur = cur.next
            location = location + 1
        print(cur.data)
        previous = cur.prev
        nex = cur
        cur = new_node
        previous.next = new_node
        nex.prev = new_node

        new_node.prev = previous
        new_node.next = nex
        self.count = self.count + 1

    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        cur = self.head
        found = False
        location = 0
        while cur and found is False:
            if cur.data == data:
                found = True
            else:
                location = location + 1
                cur = cur.next
        if found == True:
            return location
        else: 
            return - 1


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr



add_node = DoublyLinkedList()
add_node.addFirst('be')
add_node.addFirst('Force')
add_node.addFirst('the')
add_node.addFirst('May')



add_node.addLast('with')
add_node.addLast('you')
add_node.addLast('!')


print(add_node.__str__())

print(add_node.indexOf('with'))
add_node.delete('you')
add_node.delete('!')
add_node.addAtIndex('us', 5)
add_node.addAtIndex('all', 6)
add_node.addLast('!')
print(add_node.__str__())