class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

day1 = Node('Monday')
day2 = Node('Tuesday')
day3 = Node('Wednesday')


day1.next = day2
# day1.next.next = day3
day2.next = day3

print(day1.data)
print(day2.data)
print(day2.next.data)

print('traversing through the linked list')
current = day1
while current:
    print(current.data)
    current = current.next