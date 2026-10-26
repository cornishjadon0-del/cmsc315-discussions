"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque
from operator import truediv


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values
        self.stk = []
        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # appending to the list lets the first in always be the bottom of the stack
        self.stk.append(value)
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # the pop method needs to check if the stack is empty so it does not return a value
        # that the program doesn't know what to do with
        # in this case the pop method will throw a message that the stack is empty
        if self.is_empty() == True:
            return "Stack is empty"
        else:
            return self.stk.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek returns the top value without removing the value
        if self.is_empty() == True:
            return "Stack is empty"
        else:
            return self.stk[len(self.stk) - 1]


    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        if len(self.stk) == 0:
            return True
        else:
            return False



class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.dq = deque()
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # enqueue adds to the queue from the back from which it can't leave until the first element leaves
        self.dq.append(value)
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # if the queue is empty dequeue could output a nonsense value the program can't use causing an error
        if self.is_empty() == True:
            return "Queue is empty"
        else:
            return self.dq.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # front return the first element of the list
        if self.is_empty() == True:
            return "Queue is empty"
        else:
            return self.dq[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        if len(self.dq) == 0:
            return True
        else:
            return False


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
st = Stack()
st.push(3)
st.push(5)
st.push(10)
st.push(8)
print("\n=== STACK DEMO ===")
print("The number 3, 5, 10, and 8 are pushed to the stack in that order")
print("To demonstrate LIFO I'll use a loop")
for values in range(4):
    print(st.pop())
print("If we pop from an empty stack it will output:", st.pop())
print("If we peek from an empty stack it will output:", st.peek())
print("Our current stack is empty after having its last output popped, thus the output of is_empty is:",st.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.
dq = Queue()
dq.enqueue(10)
dq.enqueue(15)
dq.enqueue(17)
dq.enqueue(8)
print("\n=== QUEUE DEMO ===")
print("The number 10, 15, 17, and 8 are added to the Queue in that order")
print("To demonstrate FIFO I'll use a loop")
for values in range(4):
    print(dq.dequeue())
print("If we dequeue from an empty queue it will output:", dq.dequeue())
print("If we peek from an empty stack it will output:", dq.front())
print("Our current stack is empty after having its last output dequeued, thus the output of is_empty is:",dq.is_empty())

if __name__ == "__main__":
    main()
