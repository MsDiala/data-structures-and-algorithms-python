class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.length = 0

    '''Adds node to head of linked list'''

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    '''Takes in a target value and iterates through Linked List
    until the value is found, or the end of the list is reached
    returns a boolean'''

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __str__(self):
        values = ''
        current = self.head
        while current:
            values += f'Node: {str(current.value)} '
            current = current.next
        return values

    '''Iterates to the end of a Linked List and appends a value'''

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

   
    def insertBefore(self, exisiting_value, new_value):
        new_node = Node(new_value)
        current = self.head
        
        while current.next:
            if current.next.value == exisiting_value:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next


    def insertAfter(self, existing_value, new_value):
      new_node = Node(new_value)
      current = self.head
      while current:
        if current.value == existing_value:

          old_node = current.next
          current.next = new_node
          new_node.next = old_node

          return
        else:
          current = current.next


    def length(self): 
        current = self.head 
        count = 0 
        while (current): 
            count += 1
            current = current.next
        return count 
          

    def nthFromEnd(self,n=0):
        if type(n)!=int:
            return'Exception'
        if n>self.length() or n<0:
            return'Exception'  
        current= self.head
        counter= 0
        while current.next():
            current= current.next
            counter+=1
            if counter>n:
                current= current.next
            return current.value                         
        
   
    








   


          
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
ll = LinkedList()
ll.insert(node1)
ll.insert(node2)
ll.insert(node3)
ll.insertBefore(node2,node4)
ll.insertAfter(node3,node5)
print(ll)

   
   