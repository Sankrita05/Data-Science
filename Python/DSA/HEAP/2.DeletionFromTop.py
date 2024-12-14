class Heap:
    def __init__(self):
        self.arr = []
        
    def insert(self, val):
        self.arr.append(val)
        cur_index = len(self.arr)-1
        while(cur_index!=0):
            parent_index = (cur_index-1)//2
            if(self.arr[parent_index]>self.arr[cur_index]):
                self.arr[parent_index], self.arr[cur_index] = self.arr[cur_index], self.arr[parent_index]
            cur_index = parent_index
            
    
    def heapify(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.arr) and self.arr[left_child] < self.arr[index]:
            self.arr[index], self.arr[left_child] = self.arr[left_child], self.arr[index]
            self.heapify(left_child)

        if right_child < len(self.arr) and self.arr[right_child] < self.arr[index]:
            self.arr[index], self.arr[right_child] = self.arr[right_child], self.arr[index]
            self.heapify(right_child)

    def delete_from_heap(self, index):
        print("Deleting the element", self.arr[index])
        self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
        self.arr.pop()
        self.heapify(index)
        
if __name__== '__main__':
    n = int(input())
    h1 = Heap()
    nums = list(map(int, input().split()))
    for i in nums:
        h1.insert(i)
    print(*h1.arr)
    x = int(input())
    indexes = list(map(int, input().split()))
    for index in indexes:
        h1.delete_from_heap(index)
        print(*h1.arr)