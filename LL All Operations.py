class Node:
    def __init__(self, value):
        # Initialize a node with a value and a pointer to the next node
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # Initialize the linked list with a single node
        new_node = Node(value)
        self.head = new_node  # Head points to the first node
        self.tail = new_node  # Tail points to the last node
        self.length = 1       # Length of the list is initially 1

    def print_list(self):
        # Print all values in the list
        curr = self.head
        while curr:
            print(f"{curr.value} -> ", end="")
            curr = curr.next
        print("None")  # Indicate the end of the list

    def append_end(self, value):
        # Add a new node with the given value to the end of the list
        new_node = Node(value)
        if self.length == 0:
            # If the list is empty, set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, append the new node to the end and update the tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1  # Increment the length of the list
        
    def pop_last(self):
        # Remove the last node from the list
        if self.length == 0:
            return None
        temp1 = self.head
        temp2 = self.head
        while temp2.next:
            temp1 = temp2
            temp2 = temp2.next
        self.tail = temp1
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

    def prepend(self, value):
        # Add a new node with the given value to the start of the list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        # Remove the first node from the list
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
    
    def get_index(self, index):
        # Get the node at a specific index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def change_at_index(self, index, val):
        # Change the value of the node at a specific index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = val

    def insert_at(self, index, val):
        # Insert a new node at a specific index
        if index < 0 or index >= self.length:
            return None
        new_node = Node(val)
        temp1 = self.head
        temp2 = self.head
        for _ in range(index):
            temp1 = temp2
            temp2 = temp2.next
        temp1.next = new_node
        new_node.next = temp2
        self.length += 1

    def remove_from(self, index):
        # Remove the node at a specific index
        if index < 0 or index >= self.length:
            return None
        temp1 = self.head
        temp2 = self.head
        for _ in range(index):
            temp1 = temp2
            temp2 = temp2.next
        temp1.next = temp2.next
        self.length -= 1

    def reverse(self):
        # Reverse the linked list
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        if self.head is None or self.head.next is None:
            return False
        slow = self.head
        fast = self.head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def partition_list(self, x):
        if not self.head:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next

    def remove_duplicates(self):
            values = set()
            previous = None
            current = self.head
            while current:
                if current.value in values:
                    previous.next = current.next
                    self.length -= 1
                else:
                    values.add(current.value)
                    previous = current
                current = current.next

    def binary_to_decimal(self):
        if self.head is None:
            return 0
        string = ""
        curr = self.head
        while curr:
            string += "".join(str(curr.value))
            curr = curr.next
        return int(string,2)
