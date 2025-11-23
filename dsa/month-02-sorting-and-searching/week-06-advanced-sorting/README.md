# Week 06: Advanced Sorting

## Overview

This week covers advanced sorting algorithms that achieve better time complexity: Merge Sort, Quick Sort, and Heap Sort. These are the algorithms used in production systems and interviews.

## Learning Objectives

- Understand divide-and-conquer sorting approach
- Implement Merge Sort, Quick Sort, and Heap Sort
- Analyze worst-case and average-case complexities
- Know when to use each advanced algorithm
- Implement sorting optimizations and variations

## Algorithms

### 1. Merge Sort

**Concept:** Divide array in half, recursively sort each half, then merge sorted halves.

```python
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Complexity:**
- Time: O(n log n) all cases
- Space: O(n)
- Stable: Yes

**When to use:** When O(n log n) guaranteed, linked lists, external sorting

---

### 2. Quick Sort

**Concept:** Pick pivot, partition array around pivot, recursively sort partitions.

```python
def quickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Complexity:**
- Time: O(n log n) average, O(n²) worst
- Space: O(log n) for recursion
- Stable: No (standard implementation)

**When to use:** General-purpose sorting, good cache locality, average case matters

---

### 3. Heap Sort

**Concept:** Build max heap, repeatedly extract max element and place at end.

```python
def heapSort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

**Complexity:**
- Time: O(n log n) all cases
- Space: O(1)
- Stable: No

**When to use:** When space is critical, guaranteed O(n log n) needed

---

## Comparison with Basic Sorts

| Aspect | Merge | Quick | Heap |
|--------|-------|-------|------|
| Best Case | O(n log n) | O(n log n) | O(n log n) |
| Average | O(n log n) | O(n log n) | O(n log n) |
| Worst Case | O(n log n) | O(n²) | O(n log n) |
| Space | O(n) | O(log n) | O(1) |
| Stable | Yes | No | No |
| In-place | No | Yes | Yes |

## Key Insights

1. **Merge Sort:** Stable and predictable, uses extra space
2. **Quick Sort:** Fast average case, popular in practice
3. **Heap Sort:** Guaranteed O(n log n), minimal space
4. **Divide-and-conquer:** Efficient recursive approach
5. **Hybrid approaches:** TimSort combines multiple techniques

## Problems

See [problems.md](problems.md) for this week's challenges.

## Resources

- [Complexity Cheatsheet](../../resources/complexity-cheatsheet.md)
- [Solution Approaches](solutions/)
- [Community Solutions](community-solutions/)

## Tips

1. **Understand recursion:** How base cases work
2. **Analyze partitioning:** Critical for Quick Sort
3. **Heap operations:** Understand parent-child relationships
4. **Trace examples:** Work through small arrays manually
5. **Compare:** Know trade-offs between algorithms
