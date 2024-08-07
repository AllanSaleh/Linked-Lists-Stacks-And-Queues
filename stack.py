def line():
    print('~'*20)

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)

        if self.head == None: #Checking if list is empty
            self.head = new_node #first
            self.tail = new_node #and last
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.lenght+=1;

    def traverse(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

    def pop(self):
        if not self.tail:
            return "Can't pop from an empty stack"
        popped = self.tail
        self.tail = popped.prev
        self.tail.next = None
        self.length -= 1
        return popped.data
    
    def insert (self, pos, data):
        new_node = Node(data)
        current = self.head
        count = 1

        while count < pos:
            current = current.next
            count += 1
        
        new_node.next = current.next
        new_node.prev = current

        current.next = new_node
        new_node.next.prev = new_node
        length +=1




alist = Stack()
alist.append('plain pancake')
alist.append('blueberry pancake')
alist.append('chocolote chip pancake')
alist.append('red velvet pancake')

alist.traverse()

line()

print('Time to each pancake...')
print(alist.pop())
# print(alist.pop())

line()

alist.insert(2, 'peanut butter pancake')

print("Stack now...")
alist.traverse()
