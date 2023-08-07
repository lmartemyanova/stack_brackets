class Stack():


    def __init__(self):
        self.data = []


    def is_empty(self) -> bool:
        if self.data:
            return False
        return True


    def push(self, elem: any) -> None:
        self.data.append(elem)
        return


    def pop(self) -> any:
        return self.data.pop()


    def peek(self) -> any:
        return self.data[-1]


    def size(self) -> int:
        return len(self.data)
