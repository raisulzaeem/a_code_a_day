class NewNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None



def dive_deep(node,level):
    if node != None:
        level+=1
        global max_level
        global max_val
        if level > max_level:
            max_level = level
            max_val = node.data
        dive_deep(node.left, level)
        dive_deep(node.right, level)


def find_deepest(root):
    level = 0
    global max_level
    global max_val
    max_level = 0
    max_val = 0

    dive_deep(root, level)

    return max_level, max_val

if __name__ == "__main__":

    root = NewNode(1)
    root.left = NewNode(2)

    root.left.left = NewNode(4)
    root.left.right = NewNode(5)
    root.left.right.left = NewNode(6)
    root.left.right.right = NewNode(7)
    root.left.right.right.right = NewNode(8)

    root.right = NewNode(3)
    root.right.right = NewNode(9)
    root.right.right.left = NewNode(10)
    root.right.right.right = NewNode(11)
    root.right.right.left.left = NewNode(12)
    root.right.right.left.right = NewNode(13)
    root.right.right.right.right = NewNode(14)
    root.right.right.right.left = NewNode(15)
    root.right.right.right.left.right = NewNode(16)

    deepest_level, deepest_value = find_deepest(root)

    print(f"Deepest level: {deepest_level} \nValue: {deepest_value}")