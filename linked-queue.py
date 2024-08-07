def line():
    print('~'*20)

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
    
class SongQueue():
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data): # O(1) - Constant
        new_song = Node(data)
        if self.head == None: #is my linked list empty
            self.head = new_song #new_song becomes the first item
            self.tail = new_song #new_song becomes the last item
        else: #if the list is not empty
            self.tail.next = new_song #find the tail, and set the tail's next to new_song (adding new song to the end)
            self.tail = new_song #assigning the 'tail' title to the new_song

    def traverse(self): # O(n) - Linear
        current = self.head
        while current:
            print(current.data)
            current = current.next

# 
    def dequeue(self): #Playing a song
        if self.head == None: #Check if queue is empty
            return "Can't dequeue an empty list"
        else:
            removed = self.head #remove the head
            self.head = self.head.next #reassign the title of head to what comes next
            return removed.data #return the severed head
        


queue = SongQueue()

queue.enqueue("Bad")
queue.enqueue('yesterday')
queue.enqueue('gimme my bag')
queue.enqueue('tribe')
queue.enqueue('dance monkey')
queue.enqueue('Safe Haven')

line()

queue.dequeue()
queue.dequeue()
queue.dequeue()


line()

queue.traverse()