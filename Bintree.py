class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = self.putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return self.finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        self.skriv(self.root)
        print("\n")

    def putta(self, node, newvalue):
        #Tar en nod och ett värde som parametrar, använder sedan rekursion för att sätta noden på rätt plats
        if (self.root == None):
            return Node(newvalue)
        else:
            if (node.value == newvalue):
                print("Detta finns redan i trädet")
                return node
            if (newvalue < node.value):
                if (node.left == None):
                    node.left = Node(newvalue)
                    return node
                else:
                    self.putta(node.left, newvalue)
                    return node
            if (newvalue > node.value):
                if (node.right == None):
                    node.right = Node(newvalue)
                    return node
                else:
                    self.putta(node.right, newvalue)
                    return node

    def finns(self, node, value):
        if(node == None):
            return False

        if value == node.value:
            return True

        if(node.right == None and node.left == None):
            return False

        if node.value > value:
            if self.finns(node.left, value):
                return True
            else:
                return False

        if node.value < value:
            if (self.finns(node.right, value)):
                return True
            else:
                return False


    def skriv(self, node):
        if(node == None):
            return

        if(node.right == None and node.left == None):
            print(str(node.value))
            return

        self.skriv(node.left)
        print(str(node.value))
        self.skriv(node.right)
        return
if __name__ == "__main__":
    tree = Bintree()
    tree.put(10)
    tree.put(15)
    tree.put(5)
    tree.put(8)
    tree.put(12)
    tree.put(17)
    tree.put(3)
    tree.put(8)
    tree.write()

    print(tree.__contains__(5))
    print(tree.__contains__(1))
    print(tree.__contains__(17))
    print(tree.__contains__(8))
    print(tree.__contains__(18))
