class Node:
    def __init__(self, next_node=None):
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


node1 = Node()
node2 = Node()

node1.set_next_node(node2)
print(node1)