def is_min_heap(arr):
    n = len(arr)
    
    # Traverse all internal nodes
    for i in range(n // 2):  # Only check until the last non-leaf node
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        
        # Check if left child exists and satisfies the min-heap property
        if left_child_index < n and arr[i] > arr[left_child_index]:
            return "No"
        
        # Check if right child exists and satisfies the min-heap property
        if right_child_index < n and arr[i] > arr[right_child_index]:
            return "No"
    
    return "Yes"
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        # Write you code to check if the arr represents a heap
        print(is_min_heap(arr))
        