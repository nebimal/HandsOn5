def Parent(i):
    return (i - 1) // 2

def Left(i):
    return (i * 2) + 1

def Right(i):
    return (i * 2) + 2

def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]

def heapify(heap, i, size):
    smallest = i
    left = Left(i)
    right = Right(i)

    if left < size and heap[left] < heap[smallest]:
        smallest = left
    if right < size and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        swap(heap, i, smallest)
        heapify(heap, smallest, size)

def build_min_heap(arr):
    size = len(arr)
    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, i, size)

def push(heap, value):
    heap.append(value)
    i = len(heap) - 1
    while i > 0 and heap[Parent(i)] > heap[i]:
        swap(heap, i, Parent(i))
        i = Parent(i)

def pop(heap):
    if len(heap) == 0:
        return None    
    root = heap[0]
    last = heap.pop()

    if len(heap) > 0:
        heap[0] = last
        heapify(heap, 0, len(heap))

    return root

def display(heap):
    print(heap)


heap = [25, 17, 8, 20, 15, 5, 30]
build_min_heap(heap)
display(heap)

push(heap, 3)
push(heap, 10)
push(heap, 2)
display(heap)

while heap:
    print("Popped:", pop(heap))
    display(heap)
