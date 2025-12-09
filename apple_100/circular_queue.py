#https://leetcode.com/problems/design-circular-queue/
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = []
        self.length = k

    def enQueue(self, value: int) -> bool:
        if len(self.arr)<self.length:
           self.arr.append(value)
           return True
        return False

    def deQueue(self) -> bool:
        if len(self.arr)>0:
            del self.arr[0]
            return True
        return False

    def Front(self) -> int:
        if len(self.arr)>0:
            return self.arr[0]
        else:
            return -1
        

    def Rear(self) -> int:
        if len(self.arr)>0:
            return self.arr[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.arr)==0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.arr) == self.length:
            return True
        else:
            return False