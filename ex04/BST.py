import random
from urllib import request

class Node:
    def __init__(self, word: str, left = None, right = None, parent = None):
        self.word = word
        self.left = left
        self.right = right
        self.parent = parent

class BST:
    def __init__(self, source: str, **kwargs):
        self.root = None
        self.count = 0
        # default values
        file = True
        url = False
        try:
            file = kwargs['file']
        except KeyError:
            pass

        try:
            url = kwargs['url']
        except KeyError:
            pass

        if file == url:
            print("Wrong input data")
            exit(1)

        words = self._read_dictionary(source, file)

        random.shuffle(words)

        for word in words:
            self.add(Node(word))


    def _read_dictionary(self, source: str, file: bool) -> list[str]:
        res = []
        if file == True:
            with open(source) as f:
                txt = f.read()
                res = txt.split()
        else:
            with request.urlopen(source) as response:
                html = response.read().decode()
                res = html.split()
        return res



    def add(self, node: Node):
        def add_node(root: Node, node: Node) -> Node:
            if root == None:
                return node
            
            if node.word.lower() < root.word.lower():
                root.left = add_node(root.left, node)
                root.left.parent = root
            else:
                root.right = add_node(root.right, node)
                root.right.parent = root
            
            return root

        self.root = add_node(self.root, node)
        self.count += 1

    def print(self):
        def print_rec(node: Node):
            if node == None:
                return
            
            print_rec(node.left)
            print(node.word)
            print_rec(node.right)

        print_rec(self.root)

    def successor(self, node: Node):
        def minimum(node: Node):
            if node.left == None:
                return node
            
            return minimum(node.left)
        
        if node.right != None:
            return minimum(node.right)
        
        p = node.parent
        while p != None and p.right == node:
            node = p
            p = p.parent

        return p
    
    def find_node_of_prefix(self, word) -> Node | None:
        def find_rec(node: Node, word: str) -> Node | None:
            if node is None:
                return None
            if node.word.lower() == word.lower():
                return node
            
            if word.lower() < node.word.lower():
                return find_rec(node.left, word)
            else:
                return find_rec(node.right, word)
            
        node = find_rec(self.root, word)
        if node == None:
            aux = Node(word)
            self.add(aux)
            node = self.successor(aux)
            
            if aux.parent.left == aux:
                aux.parent.left = None
            else:
                aux.parent.right = None

            del aux

        return node

    def autocomplete(self, prefix: str) -> list[str]:
        node = self.find_node_of_prefix(prefix)
        res = []
        while node is not None and node.word[:len(prefix)].lower() == prefix.lower():
            res.append(node.word)
            node = self.successor(node)

        return res