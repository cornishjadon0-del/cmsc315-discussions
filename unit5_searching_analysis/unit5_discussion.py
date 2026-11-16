"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    i = 0 # declare variable is O(1)
    for x in lst: # declare x plus loop is now O(1 + 1 + 3N + 1) in worst case as each
        # loop is changing x to the next value, checking x against target, and incrementing i and when loop finished
        # one last check is made to end the loop, then including the return statement is O(4 + 3N) which simplified is
        # O(N) because insignificant variables are removed as well as constants in big O notation
      print(i)
      if x == target:
          return i
      else:
          i += 1
    return -1

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # these variable represent the bounds of the subarray the program is working with
    l = 0
    h = len(lst) - 1
    # currently low = 0 and high is the highest index in the array/list
    while h >= l:
        m = (h + l) // 2 # m is our midpoint and is also the index of the list that is checked each loop
        # whatever the subarray is m will always be the middle of it rounded down
        print(m)
        if lst[m] < target: # if our target is larger than m the low point is set to the index above m
            # this way the program is working with a subarray half the size of the previous one each loop until the
            # end is reached
            l = m + 1
        elif lst[m] > target:
            # this works the same way as above, but instead it changes the high point to half the subarray
            h = m - 1
        else:
            # here the target matches the value, thus the program returns the index
            return m
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    smlst = [1, 3, 5, 7, 9, 11, 13]
    print("Creating list with values:", smlst)
    print("Searching linearly for index of value 11:", linear_search(smlst,11))
    # calling the above function iterates over the list until it finds 11 checking against 6 values
    print("Searching using binary search for index of value 11:", binary_search(smlst,11))
    # binary search checks 7 first then checks 11 as it is the midpoint of the new subarray and only checks against
    # 2 values
    print("Searching linearly for index of value 22:", linear_search(smlst,22))
    # linear fails to find 22 after checking against all 7 values
    print("Searching using binary search for index of value 22:", binary_search(smlst,22))
    # binary search checks 7, then 11, then 13 and determines 22 is not in the array only checking against 3 values
    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    biglst = []
    for x in range(100):
        biglst.append(x + 1)
    print("Creating large list with values 1-100")
    print("Searching linearly for index of value 11:", linear_search(biglst,11))
    # calling the above function iterates over the list until it finds 11 checking against 11 values
    print("Searching using binary search for index of value 11:", binary_search(biglst,11))
    # binary search checks 50 first, then checks 25, then 12, then 6, 9, and 11 comparing 6 values total
    print("Searching linearly for index of value 22:", linear_search(biglst,122))
    # linear fails to find 122 after checking against all 100 values
    print("Searching using binary search for index of value 22:", binary_search(biglst,122))
    # binary search checks 7 values before determining 122 is not in the data set
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("Empty List demonstration")
    emplst = []
    print("Searching for 20 in empty list using linear search:",linear_search(emplst,20))
    # linear search uses a for loop, when the size of the list is 0 the for loop doesn't run and outputs -1
    print("Searching for 20 in empty list using binary search:",binary_search(emplst,20))
    # binary search uses a while loop that is predicated on h being >= 0, when the length is 0 and h becomes -1 the loop
    # doesn't run and the program outputs -1 or 0 if the target is found
    print("Single element list edge case demonstration")
    emplst.append(42)
    print("Searching for 20 in empty list using linear search:",linear_search(emplst,20))
    # the loop iterates once then doesn't find 20 so returns -1 as the index
    print("Searching for 20 in empty list using binary search:",binary_search(emplst,20))
    # regardless of the value searching for unless the value is the single value, either l is set higher than  h
    # or h is set lower than l and the loop finishes after running once and the program outputs -1 or 0


if __name__ == "__main__":
    main()