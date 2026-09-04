class DynamicArray:
    
    def __init__(self, capacity: int):
        # initialise an empty array with capacity
        self.array = [None] * capacity
        self.size = capacity
        self.last = -1

    def get(self, i: int) -> int:
        # return element at i
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        # set the element at i to n
        self.array[i] = n
        if i > self.last:
            self.last = i

    def pushback(self, n: int) -> None:
        # push the element n to the end of the array
        if self.last == self.size - 1:
            self.resize()
        self.array[self.last + 1] = n
        self.last += 1
        

    def popback(self) -> int:
        # remove last element and return
        res = self.array[self.last]
        self.array[self.last] = None
        self.last -= 1
        return res
 

    def resize(self) -> None:
        # double capacity
        self.size *= 2
        bigger = [0] * self.size
        i = 0
        while i < self.size / 2 and self.array[i] != None:
            bigger[i] = self.array[i]
            i += 1
        self.array = bigger


    def getSize(self) -> int:
        # return number of elements
        return 0 if self.last == -1 else self.last + 1
        
    
    def getCapacity(self) -> int:
        # return capacity
        return self.size
