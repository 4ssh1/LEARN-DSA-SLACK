# Week 06: Advanced Sorting - Problems

## Problem Set

### Problem 1: Implement Merge Sort
**Difficulty:** Medium

Implement the merge sort algorithm. Sort an array in ascending order using merge sort.

**Example:**
```
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
```

**Constraints:**
- 1 <= arr.length <= 10^5
- -10^6 <= arr[i] <= 10^6

---

### Problem 2: Implement Quick Sort
**Difficulty:** Medium

Implement the quick sort algorithm. Sort an array in ascending order using quick sort.

**Example:**
```
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
```

**Constraints:**
- 1 <= arr.length <= 10^5
- -10^6 <= arr[i] <= 10^6

---

### Problem 3: Implement Heap Sort
**Difficulty:** Medium

Implement the heap sort algorithm. Sort an array in ascending order using heap sort.

**Example:**
```
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
```

**Constraints:**
- 1 <= arr.length <= 10^5
- -10^6 <= arr[i] <= 10^6

---

### Problem 4: Sort an Array
**Difficulty:** Medium

Given an array of integers nums, sort the array in ascending order and return it.

**Example:**
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

**Constraints:**
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4

---

### Problem 5: Relative Sort Array
**Difficulty:** Easy

Given two arrays arr1 and arr2, elements of arr1 are all distinct, and all elements of arr1 are also in arr2. Sort arr1 such that the order of elements in arr1 is the same as in arr2. Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

**Example:**
```
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
```

**Constraints:**
- 1 <= arr1.length, arr2.length <= 1000
- 0 <= arr1[i], arr2[i] <= 1000

## Submission Guidelines

1. Implement all 3 advanced sorting algorithms
2. Implement in your preferred language
3. Place solutions in `solutions/[language]/` folder
4. Include time and space complexity analysis
5. Add comments explaining pivot selection or merge strategy
6. Test with various input sizes (small, large, edge cases)
7. Compare performance with Quick Sort vs Merge Sort
