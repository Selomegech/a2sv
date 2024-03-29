

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  # Convert to zero-based index
        self.stream[idKey] = value

        result = []
        if idKey == self.ptr:
            result.append(value)
            self.ptr += 1
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                result.append(self.stream[self.ptr])
                self.ptr += 1

        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)