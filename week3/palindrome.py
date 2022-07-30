class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def iter(self):
        # Iterate through the list.
        current = self.top
        while current:
            val = current.data
            current = current.next
            yield val

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else: 
            new_node.next = self.top
            self.top = new_node
        self.size = self.size + 1
        print(f'Pushed {data}.' )

    def pop(self):
        cur = self.top
        if cur:
            data = self.top.data
            self.size = self.size  - 1
            if cur.next:
                self.top = cur.next
            else:
                cur = None
            return data
        else:
            return None

    def stack_size(self): 
        print(f'Stack size is: {self.size}')

    def isEmpty(self):
        if self.size <= 0:
            return 'The stack is empty'
        else:
            return f'The stack size is at {self.size}. It is not empty '

    def peek(self):
        if self.size != 0:
            return self.top.data
        else:
            return None


class Queue:
    def __init__(self):
        self.que_stack = []
        self.size = 0

    def enqueue(self, data):
        self.que_stack.append(data)
        self.size+=1

    def dequeue(self, data):
        if self.que_stack:
            self.que_stack.pop(data)
            self.size -=1
        return self.que_stack

    def isEmpty(self):
        if self.size <= 0:
            return 'The queue is empty'
        else:
            return f'The queue size is at {self.size}. It is not empty '        

    def getSize(self):
        queue_size = len(self.que_stack)
        return queue_size 
    
    def peek(self):
        return self.que_stack[0]


# A function that accepts a string as a 
# parameter and returns either True or 
# False if the string is a Palindrome.

def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


#  Stack
print(" ", end= '___Stack___\n\n')
stack = Stack()
stack.push('f')
stack.push('g')
stack.push('e')
print(stack.__str__())
stack.stack_size()
print(f'"{stack.peek()}" is the front item in the Stack')
stack.pop()
print(stack.__str__())
stack.stack_size()
print(stack.isEmpty())
print(f'"{stack.peek()}" is the front item in the Stack')


# Queue
queue = Queue()
queue.enqueue('e')
queue.enqueue('f')
queue.enqueue('g')
print(" ", end= '\n___Queue___\n\n')
print(queue.que_stack)
queue.dequeue(0)
print(queue.que_stack)
print(f'The current size of the queue is: {queue.getSize()}')
print(queue.isEmpty())
print(f'"{queue.peek()}" is the front item in the Queue')


# Palindrome
print(" ", end= '\n___Palindrome___\n\n')
print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))