"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""



class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.key = value
        self.left = None
        self.right = None
        pass


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None
        pass

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # checks if the BST is empty, and sets the new node as root if true
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
        pass

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # explores node.right if value is greater than the current node
        if value > node.key:
            # if the right reference is empty then the correct location has been found
            # a new node is set as node.right
            if node.right is None:
                node.right = Node(value)

            else:
                # if node.right points to a node, then insert recursive calls itself using node.right as a parameter
                self._insert_recursive(node.right, value)
        # works same way as above
        if value < node.key:
            if node.left is None:
                node.left = Node(value)

            else:
                self._insert_recursive(node.left, value)


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # immediately returns false if  BST is empty
        if self.root is None:
            return False
        return self._search_recursive(self.root, value)


    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node.key == value:
            return True
        # finds value and returns true
        if value > node.key:
            # if the reference where the value shold be is empty then it doesn't exist and returns false
            if node.right is None:
                return False
            else:
            # if the reference where the value should be, exists then the method calls itself using the reference
            # as the new parameter
                return self._search_recursive(node.right, value)
        else:
            if node.left is None:
                return False
            else:
                return self._search_recursive(node.left, value)


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        return self._inorder_recursive(self.root,values)

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        #exit condition when reaching empty references
        if node is None:
            return values
        # calls itself on all the left subtrees first
        self._inorder_recursive(node.left, values)
        # first to reach this code is the left most subtree
        values.append(node.key)
        # then once the left is fully iterated, calls itself with the right subtrees, this produces a list in order
        self._inorder_recursive(node.right, values)
        return values



def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.
    print("\n=== TREE CONSTRUCTION ===")
    print("Inserting the values 12, 8, 17, 3, 10, 15, and 19 in the new BST")
    opp = BST()
    opp.insert(12)
    opp.insert(8)
    opp.insert(17)
    opp.insert(3)
    opp.insert(10)
    opp.insert(15)
    opp.insert(19)
    # a BST is more efficient at searching a BST because each element is guaranteed to be smaller or
    # larger than its parent based on its location. A search algorithm can eliminate paths
    # this means the worst case is O(sqrt(N)) as apposed to O(N)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("Below is the elements of the BST from smallest to largest")
    print(opp.inorder())
    # the traversal is able to print the elements sorted because it starts by calling itself on both its left
    # subtree and its right subtree. Each subtree calls itself on its left and right subtree. It adds its value
    # to a list after exploring the left subtree and before the right subtree this way the lowest is added first
    # and the highest last
    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("Searching for value 17")
    print(opp.search(17)) # 17 is in the tree it returns true
    print("Searching for value 3")
    print(opp.search(3)) # 3 is in the tree it returns true
    print("Searching for value 21")
    print(opp.search(21)) # 21 is not in the tree it returns false
    print("Searching for value 67")
    print(opp.search(67)) ## 67 is not in the tree it returns false

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("I will insert the value 3 that already exists in the tree the tree should not change")
    opp.insert(3)
    print(opp.inorder())


if __name__ == "__main__":
    main()