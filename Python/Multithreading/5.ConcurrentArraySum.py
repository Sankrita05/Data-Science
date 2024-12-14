import threading

ARRAY_SIZE = 9
NUM_SEGMENTS = 3

# Object for synchronization
lock = threading.Lock()

def calculate_segment_sum(array, segment_id, segment_sum):
    segment_size = ARRAY_SIZE // NUM_SEGMENTS
    start_index = segment_id * segment_size
    end_index = start_index + segment_size if segment_id != NUM_SEGMENTS - 1 else ARRAY_SIZE
    
    # Calculate the sum of the segment
    segment_sum = sum(array[start_index:end_index])
    
    # Use the lock to safely update the segment_sums array
    with lock:
        segment_sums[segment_id] = segment_sum
    
array = list(range(1, 10))

# Threads list stores all the threads
threads = []

# SegmentSums array stores the sum of each segment
segment_sums = [0] * NUM_SEGMENTS

# Create threads to calculate segment sums
for i in range(NUM_SEGMENTS):
    segment_id = i
    thread = threading.Thread(target=calculate_segment_sum,
                              args=(array, segment_id, segment_sums))
    threads.append(thread)
    
# Start all threads
for thread in threads:
    thread.start()
    
# Wait for all threads to finish
for thread in threads:
    thread.join()
    
# Calculate the total sum by combining segment sums
total_sum = sum(segment_sums)

# Display individual segment sums and the total sum
for i in range(NUM_SEGMENTS):
    print("Segment", i, "Sum:", segment_sums[i])
    
print("Total Sum:", total_sum)
