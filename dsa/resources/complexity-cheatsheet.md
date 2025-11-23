# Complexity Cheatsheet

Quick reference for Big O complexities and performance analysis.

## Big O Notation

### Common Time Complexities (Best to Worst)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Hash table lookup, array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Simple loop, linear search |
| O(n log n) | Linearithmic | Merge sort, Quick sort |
| O(n²) | Quadratic | Nested loops, Bubble sort |
| O(n³) | Cubic | Triple nested loops |
| O(2^n) | Exponential | Recursive fibonacci |
| O(n!) | Factorial | Generating permutations |

## Data Structure Operations

### Array/List
- Access: O(1)
- Search: O(n)
- Insertion: O(n)
- Deletion: O(n)

### Linked List
- Access: O(n)
- Search: O(n)
- Insertion: O(1) if position known
- Deletion: O(1) if position known

### Hash Table
- Access: N/A
- Search: O(1) average, O(n) worst
- Insertion: O(1) average, O(n) worst
- Deletion: O(1) average, O(n) worst

### Binary Search Tree
- Access: O(log n) average, O(n) worst
- Search: O(log n) average, O(n) worst
- Insertion: O(log n) average, O(n) worst
- Deletion: O(log n) average, O(n) worst

### Stack
- Push: O(1)
- Pop: O(1)
- Peek: O(1)

### Queue
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

## Space Complexity

- O(1) - Constant space
- O(n) - Linear space
- O(n²) - Quadratic space
- O(log n) - Logarithmic space

## Tips

1. Focus on dominant term (drop constants and lower terms)
2. Consider both time and space trade-offs
3. Amortized analysis for sequences of operations
4. Best/Average/Worst case scenarios matter
