import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return
        elif self.value is None:
            self.value = BinarySearchTree(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if root is target value
        # If not check if target is greater than/equal or less then
        # If greater/equal check right node
        # If less than then check left node
        if self.value == target:
            return True
        if self.value < target:
            if self.right:
                return self.right.contains(target)
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return

        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     queue = Queue()
    #     queue.enqueue(node)
    #
    #     while queue.len() is not 0:
    #         node = queue.dequeue()
    #         print(node.value)
    #         if node.left:
    #             queue.enqueue(node.left)
    #         if node.right:
    #             queue.enqueue(node.right)
    #
    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     stack = Stack()
    #     stack.push(node)
    #
    #     while stack.len() is not 0:
    #         node = stack.pop()
    #         print(node.value)
    #         if node.left:
    #             stack.push(node.left)
    #         if node.right:
    #             stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
