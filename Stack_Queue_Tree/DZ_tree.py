#обход дерева в порядке "preorder" (сначала корень, затем левое поддерево,
# затем правое поддерево)
#В этом примере:
#- `preorder_traversal` - метод, выполняющий обход дерева в порядке "preorder".
#- `_preorder_traversal` - вспомогательный метод, который рекурсивно выполняет обход и добавляет значения узлов в список.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, root, res):
        if root:
            res.append(root.val)
            self._preorder_traversal(root.left, res)
            self._preorder_traversal(root.right, res)
        return res

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

# Пример использования:
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(20)
bt.insert(3)
bt.insert(7)

print("Preorder Traversal:", bt.preorder_traversal())
node = bt.search(7)
if node:
    print(f"Node with key 7 found: {node.val}")
else:
    print("Node with key 7 not found")
