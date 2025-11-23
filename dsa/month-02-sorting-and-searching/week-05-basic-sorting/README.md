# Week 05: Basic Sorting

## Overview

This week covers the fundamental sorting algorithms: Bubble Sort, Selection Sort, and Insertion Sort. While not used in production, understanding these forms the foundation for more advanced algorithms.

## Learning Objectives

- Understand how each basic sorting algorithm works
- Implement sorting algorithms from scratch
- Analyze time and space complexity
- Know when to use each algorithm
- Trace through sorting process

## Algorithms

### 1. Bubble Sort

**Concept:** Repeatedly step through the list, compare adjacent elements, and swap them if they're in wrong order.

```python
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

**Complexity:**
- Time: O(n²) average/worst, O(n) best
- Space: O(1)
- Stable: Yes

**When to use:** Educational purposes, nearly sorted data

---

### 2. Selection Sort

**Concept:** Divide array into sorted and unsorted parts. Repeatedly find minimum in unsorted part and move to sorted part.

```python
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Complexity:**
- Time: O(n²) all cases
- Space: O(1)
- Stable: No

**When to use:** When memory is limited, educational purposes

---

### 3. Insertion Sort

**Concept:** Build sorted array one element at a time. Take each element and insert into correct position.

```python
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Complexity:**
- Time: O(n²) average/worst, O(n) best
- Space: O(1)
- Stable: Yes

**When to use:** Small arrays, nearly sorted data, online sorting

---

## Comparison

| Aspect | Bubble | Selection | Insertion |
|--------|--------|-----------|-----------|
| Worst Case | O(n²) | O(n²) | O(n²) |
| Best Case | O(n) | O(n²) | O(n) |
| Average | O(n²) | O(n²) | O(n²) |
| Space | O(1) | O(1) | O(1) |
| Stable | Yes | No | Yes |
| Adaptive | Yes | No | Yes |

## Key Insights

1. **Stability matters:** When equal elements must maintain order
2. **Adaptive algorithms:** Perform better on nearly sorted data
3. **In-place sorting:** No extra space needed
4. **Simple but slow:** O(n²) not suitable for large datasets

## Problems

See [problems.md](problems.md) for this week's challenges.

## Resources

- [Complexity Cheatsheet](../../resources/complexity-cheatsheet.md)
- [Solution Approaches](solutions/)
- [Community Solutions](community-solutions/)

## Tips

1. **Trace through examples:** Draw out each step
2. **Understand the invariant:** What property is maintained?
3. **Optimize:** Can you add early termination?
4. **Compare:** Know differences between algorithms
5. **Practice:** Implement multiple times
