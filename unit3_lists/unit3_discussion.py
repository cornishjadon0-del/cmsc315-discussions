"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    if index >= 0:
        lst.insert(index, value)
        return True
    else:
        return False
    # The above method inserts the value at the specified index by shifting elements after
    # that index to the right then inserting the value in the empty spot


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if len(lst) != 0 and len(lst) > index >= 0:
    # verifies that the list has element by checking it isn't empty, then verifies that the index is
    # greater than -1 and less than the elements in the list to prevent errors
        return lst.pop(index)
    else:
        return None
    # index validation is required so that the program does not result in an error when the index
    # does not exist also if the index were negative an unintended element may be removed with little hope
    # for recovery

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    if value in lst:
        return lst.index(value)
    else:
        return -1
    # the method I'm using to get the index of the value cannot be called with an element that
    # is not on the list so the if statement checks that it exists
    # the method cannot just single out the value, it must check each element until it finds the
    # matching value to return its index



def main():
    print("=== UNIT 3: LIST OPERATIONS ===")
    print("\n=== INSERTION TESTS ===")
    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    print("Creating List")
    lst = [9,67,32,56,89,12] # creating the list
    # 2. Display the original list.
    print("Displaying List:")
    print(lst)
    # 3. Test insertion at:
    print("Inserting value 72 at beginning:")
    insert_at(lst,0,72) # inserts at index 0 which is always the beginning
    print(lst)
    #    - the beginning
    print("Inserting value 45 in the middle:")
    insert_at(lst,4,45) # inserts at index 4 which is roughly the middle of the list
    print(lst)
    #    - the middle
    print("Inserting value 98 at the end:")
    insert_at(lst,15,45) # attempts to insert at index 15 which will result in it being appended to the end
    print(lst)
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("Deleting from the beginning:")
    delete_at(lst,0) # deletes from the start which is index 0
    print(lst)
    print("Deleting from the middle:")
    delete_at(lst, 5) # deletes from roughly the middle of an 8 element list
    print(lst)
    print("Deleting from the end")
    delete_at(lst, 6) # deletes from the index of the last element
    print(lst)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("Searching for value 32 in the list:")
    print(search_value(lst,32), "this is the index of the value")
    print("Searching for value 113 which does not exist")
    print(search_value(lst,113), "this value should be -1 if the value doesn't exist")




    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    nlst = []
    print("inserting into an empty list")
    # the method needs to be able to handle inserting when the list is empty
    insert_at(nlst,0,5)
    print("Printing List:")
    print(nlst)
    print("removing from a list with the improper index")
    # if the index is improper then the program needs to output none otherwise it could spit an error
    print("The method returns:",delete_at(nlst,7), ",this should return None")
    print("Printing list:")
    # the method should also no remove anything from the list if the index is wrong
    print(nlst, "nothing should be removed")



if __name__ == "__main__":
    main()