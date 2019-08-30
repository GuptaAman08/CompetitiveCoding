from heapq import heapify, heappop, heappush

class Min_Heap():

    def __init__(self):
        self.heap = []
        self.heap_size = 0
        heapify(self.heap)

    def insertKey(self, i):
        self.heap_size += 1
        heappush(self.heap, i)
    
    def getMin(self):
        return self.heap[0]

    def extractMin(self):
        return heappop(self.heap)
    
    def getParent(self, i):
        return int((i-1)/2)

    def decreaseKey(self, i, new_key):
        if self.heap[i] < new_key:
            print("New key is greater than current key")
        else:
            self.heap[i] = new_key
            while i != 0 and self.heap[i] < self.heap[self.getParent(i)]:
                self.heap[i], self.heap[self.getParent(i)] = self.heap[self.getParent(i)], self.heap[i]
                i = self.getParent(i)

    def deleteKey(self, i):
        if i > (self.heap_size - 1):
            print("Invalid Key")
        else:
            self.decreaseKey(i, float("-inf"))
            self.extractMin()

        
heapObj = Min_Heap()
heapObj.insertKey(3) 
heapObj.insertKey(2) 
heapObj.deleteKey(1) 
heapObj.insertKey(15) 
heapObj.insertKey(5) 
heapObj.insertKey(4) 
heapObj.insertKey(45) 

print (heapObj.extractMin(), )
print (heapObj.getMin()) 
heapObj.decreaseKey(2, 1) 
print (heapObj.getMin())