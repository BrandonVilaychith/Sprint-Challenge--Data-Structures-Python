from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Add to tail
        # If storage length >= capacity remove oldest value and replace it with the new one
        if self.storage.length is self.capacity:
            if self.current.next is not None:
                temp_current = self.current.next
            else:
                temp_current = self.storage.head
            self.current.insert_after(item)
            self.storage.delete(self.current)
            self.current = temp_current
            self.storage.length += 1
        else:
            self.storage.add_to_tail(item)

        if self.current is None:
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # Traverse through dll and add the values to the list
        temp = self.storage.head
        while temp is not None:
            list_buffer_contents.append(temp.value)
            temp = temp.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
