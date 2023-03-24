"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        current=self.head
        count=1
        while current.next !=None and count<position:
            current=current.next
            count+=1
        if count==position:
            return current
        return None
    
    def insert(self, new_element, position):
        new=Element(new_element.value)
        new.next=None
        current=self.head
        count=1
        pos=position-1
        while current.next !=None and count<pos:
            current=current.next
            count+=1
        if position==1:
            new.next=self.head
            self.head=new
            return
        elif pos==count:
            new.next=current.next
            current.next=new
            return
        else:
            print("error")
    
    
    def delete(self, value):
        current=self.head
        if self==None:
            print("ll is empty")
            return
        if self.head.value==value:
            self.head=self.head.next
            return
        while current.next is not None:
            if current.next.value==value:
                break
            current=current.next
        if current.next is None:
            print("No such element")
            return
        else:
            current.next=current.next.next
            return
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value