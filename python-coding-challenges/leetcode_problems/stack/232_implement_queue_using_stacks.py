
# (top of file)
from typing import List  # optional

class MyQueue:
    def __init__(self):
        self.in_stack = []   # type: List[int]
        self.out_stack = []  # type: List[int]

    def push(self, x: int) -> None:
        self.in_stack.append(x)


    def _move_in_to_out(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        if self.empty():
            raise ValueError("Queue is empty")
        self._move_in_to_out()
        return self.out_stack.pop()

    def peek(self) -> int:
        if self.empty():
            raise ValueError("Queue is empty")
        self._move_in_to_out()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


# Example usage
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # Expected 1
print(q.pop())   # Expected 1
print(q.empty()) # Expected False
