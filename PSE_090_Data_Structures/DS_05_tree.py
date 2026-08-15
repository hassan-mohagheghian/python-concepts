# Data Structures - Tree
# -----------------------------------------------------------------------------
# A tree is a hierarchical structure of nodes connected by edges.
# Each node has at most one parent (except the root, which has none).
#
# Key concepts:
# 1. TreeNode — value + children
# 2. Binary Search Tree (BST) — left < node < right
# 3. Traversals — inorder, preorder, postorder, level-order
# 4. Search/insert in BST — O(log n) when balanced, O(n) worst case
# -----------------------------------------------------------------------------


from collections import deque

# =============================================================================
# TreeNode
# =============================================================================


class TreeNode:
    def __init__(self, value: int):
        self.value: int = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


# =============================================================================
# Binary Search Tree
# =============================================================================


class BST:
    def __init__(self):
        self.root: TreeNode | None = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
            return
        self._insert(self.root, value)

    def _insert(self, node: TreeNode, value: int) -> None:
        """Insert a value recursively below the given node.

        Compares against `node.value` and recurses into the left or right
        subtree, attaching a new TreeNode once an empty child slot is found.
        Duplicate values are silently ignored.

        Complexity:
            Time:  O(log n) when balanced, O(n) worst case (skewed tree)
            Space: O(log n) when balanced, O(n) worst case — call stack
        """
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def _insert_non_recursive(self, value: int) -> None:
        """Insert a value into the BST iteratively.

        Walks down the tree comparing against node values until it finds
        an empty child slot, then attaches a new TreeNode there. Duplicate
        values are silently ignored.

        Complexity:
            Time:  O(log n) when balanced, O(n) worst case (skewed tree)
            Space: O(1) — iterative, no call stack
        """
        if self.root is None:
            self.root = TreeNode(value)
            return
        node = self.root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    return
                node = node.left
            elif value > node.value:
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                node = node.right
            else:
                return  # duplicate, ignore

    def search(self, value: int) -> bool:
        return self._search(self.root, value)

    def _search(self, node: TreeNode | None, value: int) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)


# =============================================================================
# Traversals
# =============================================================================


def inorder(node: TreeNode | None) -> list[int]:
    """Left → Root → Right (sorted order for BST)."""
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def preorder(node: TreeNode | None) -> list[int]:
    """Root → Left → Right."""
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def postorder(node: TreeNode | None) -> list[int]:
    """Left → Right → Root."""
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


def level_order(node: TreeNode | None) -> list[int]:
    """Breadth-first, level by level."""
    if node is None:
        return []
    result: list[int] = []
    queue: deque[TreeNode] = deque([node])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


# =============================================================================
# Usage
# =============================================================================


def main():
    bst = BST()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.insert(value)

    print("=== BST Search ===")
    for target in [6, 99]:
        print(f"  search({target}): {bst.search(target)}")

    print("\n=== Traversals ===")
    print(f"  inorder:    {inorder(bst.root)}")
    print(f"  preorder:   {preorder(bst.root)}")
    print(f"  postorder:  {postorder(bst.root)}")
    print(f"  level-order:{level_order(bst.root)}")


if __name__ == "__main__":
    main()
