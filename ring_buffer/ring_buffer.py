from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        if self.storage.length == self.capacity:
            self.current.value = item

            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        buffer_list = []

        node = self.storage.head
        while node is not None:
            buffer_list.append(node.value)
            node = node.next
        
        return buffer_list