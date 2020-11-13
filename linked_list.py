class Node():
    def __init__(self, first_value):     # default constructor
        self.pointer = None
        self.value = first_value

class LinkedList():
    def __init__(self):
        self.head = None

    def deleteNode(self, data):
        temp = self.head

        # if the head is to be deleted
        if temp is not None:
            if temp.value == data:
                self.head = temp.pointer
                temp = None
                return

        # Search for the node to be deleted
        while temp is not None:
            if temp.value == data:
                break
            prev = temp
            temp = temp.pointer

        # if the data is not found at all in our list
        if temp is None:
            return

        # remove the link of the node from our list
        prev.pointer = temp.pointer
        temp = None

    def insert_front(self, new_value):
        new_node = Node(new_value)
        # if there is no head, make the new value the head
        if self.head is None:
            self.head = new_node
            return
        # new node pointer points to the head
        new_node.pointer = self.head
        # the head value points to the new node
        self.head = new_node
        return self.head

    # Note for this function: You may keep the function definition the way you want but
    # for abstraction, try to insert it based on an index value.
    # Ex: Insert new_value after the 3rd node.
    def insert_between(self, new_value, value_before_new_value, value_after_new_value):
        # if list is empty then return
        if self.head is None:
            print('list is empty')
            return

        before_curr = self.head
        after_curr = self.head

        # find the position of the node 'before the value'
        before_pos = None
        while before_curr is not None:
            if before_curr.value == value_before_new_value:
                before_pos = before_curr
                break
            before_curr = before_curr.pointer
        # if the first value is not found then return
        if before_pos is None:
            print('value not found')
            return

        # find the position of the node 'after the value'
        after_pos = None
        while after_curr is not None:
            if after_curr.value == value_after_new_value:
                after_pos = after_curr
                break
            after_curr = after_curr.pointer
        # if the first value is not found then return
        if after_pos is None:
            print('value not found')
            return

        # alter the pointers
        new_node = Node(new_value)
        new_node.pointer = after_pos
        before_pos.pointer = new_node

    def insert_back(self, new_value):

        # If the list is empty then make the new node the head
        if self.head is None:
            self.head = new_value
            return

        # Traverse through the list to get the last node
        temp = self.head
        while temp is not None:
            if temp.pointer is None:
                break
            temp = temp.pointer

        temp.pointer = Node(new_value)


    def printList(self):
        toPrint = ''
        temp = self.head
        head = True
        while temp:
            if head:
                toPrint += str(temp.value) + ' (head) -> '
                head = False
            elif temp.pointer is None:
                toPrint += str(temp.value) + ' (tail)'
            else:
                toPrint += str(temp.value) + ' -> '

            temp = temp.pointer
        print(toPrint + '\n')

    def reverse(self):
        current = self.head
        prev = None

        while current is not None:
            # if temp.pointer is None:
            #     break
            temp = current.pointer
            current.pointer = prev
            self.head = current
            prev = current
            current = temp


# Main code starts here. 
if __name__ == '__main__':
    llist = LinkedList()    # instantiate your class variable object
