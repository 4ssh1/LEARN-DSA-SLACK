# JavaScript Tips for DSA

## Array Methods

### Creation & Manipulation
```javascript
// Create array
const arr = [1, 2, 3];
const arr2 = new Array(5);          // Empty array of length 5
const arr3 = Array.from({length: 5}, (_, i) => i);  // [0,1,2,3,4]
const arr4 = Array(5).fill(0);      // [0,0,0,0,0]

// Operations
arr.push(4);                // Add to end: O(1)
arr.pop();                  // Remove from end: O(1)
arr.unshift(0);             // Add to start: O(n)
arr.shift();                // Remove from start: O(n)
arr.slice(1, 3);            // [2,3] (doesn't modify)
arr.splice(1, 2, 5, 6);     // Remove and insert: O(n)
arr.reverse();              // In-place reverse
arr.sort((a, b) => a - b);  // Sort ascending
```

### Search & Transform
```javascript
// Search
arr.indexOf(2);             // 1
arr.lastIndexOf(2);         // Last occurrence
arr.find(x => x > 2);       // First match
arr.findIndex(x => x > 2);  // Index of first match
arr.includes(2);            // O(n) - slow for large arrays

// Transform
arr.map(x => x * 2);        // Apply function
arr.filter(x => x > 2);     // Keep matching
arr.reduce((acc, x) => acc + x, 0);  // Accumulate
arr.forEach(x => console.log(x));    // Iterate
```

## Object (Hash Map)

### Creation & Access
```javascript
// Create
const obj = {a: 1, b: 2};
const obj2 = new Map();     // Better for frequent add/remove
const obj3 = {};            // Plain object

// Access
obj.a                       // 1
obj['a']                    // 1
obj.get ? obj.get('a') : undefined  // For Map

// Operations
obj.c = 3;                  // Add: O(1)
delete obj.b;               // Delete: O(1)
'a' in obj;                 // Check key: O(1)
Object.keys(obj);           // Get all keys
Object.values(obj);         // Get all values
Object.entries(obj);        // Get [key, value] pairs
```

### Map vs Object
```javascript
// Map (usually better for DSA)
const map = new Map();
map.set('a', 1);            // O(1)
map.get('a');               // 1
map.has('a');               // true
map.delete('a');            // true
map.size;                   // Get size

// Object
const obj = {a: 1};
obj.a;                      // Direct access
Object.keys(obj).length;    // Get size (slower)
```

## Set

### Creation & Operations
```javascript
// Create
const set = new Set([1, 2, 2, 3]);  // {1, 2, 3}
const set2 = new Set();

// Operations
set.add(4);                 // O(1)
set.has(2);                 // true: O(1)
set.delete(2);              // true: O(1)
set.size;                   // Get size
set.clear();                // Remove all

// Convert
Array.from(set);            // [1, 2, 3]
[...set];                   // Spread operator
```

## String Operations

### Methods
```javascript
const s = "hello world";

// Case
s.toUpperCase();            // "HELLO WORLD"
s.toLowerCase();            // "hello world"

// Search
s.indexOf('o');             // 4
s.lastIndexOf('o');         // 7
s.includes('world');        // true
s.startsWith('hello');      // true
s.endsWith('world');        // true

// Extract
s.charAt(0);                // 'h'
s.charCodeAt(0);            // 104
s.substring(0, 5);          // "hello"
s.slice(0, 5);              // "hello"
s.slice(-5);                // "world" (last 5)

// Transform
s.split(' ');               // ["hello", "world"]
s.replace('world', 'js');   // "hello js"
s.trim();                   // Remove whitespace
s.repeat(2);                // "hello worldhello world"
```

## Useful Patterns

### Two Pointer
```javascript
function reverse(arr) {
    let left = 0, right = arr.length - 1;
    while (left < right) {
        [arr[left], arr[right]] = [arr[right], arr[left]];
        left++;
        right--;
    }
    return arr;
}
```

### Sliding Window
```javascript
function maxSumSubarray(arr, k) {
    let windowSum = arr.slice(0, k).reduce((a, b) => a + b, 0);
    let maxSum = windowSum;
    
    for (let i = k; i < arr.length; i++) {
        windowSum = windowSum - arr[i - k] + arr[i];
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}
```

### Frequency Counter
```javascript
function getFrequency(arr) {
    const freq = {};
    for (const num of arr) {
        freq[num] = (freq[num] || 0) + 1;
    }
    return freq;
}

// Or using Map
function getFrequencyMap(arr) {
    const freq = new Map();
    for (const num of arr) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }
    return freq;
}
```

## Higher-Order Functions

### map, filter, reduce
```javascript
// map: transform each element
[1, 2, 3].map(x => x * 2);  // [2, 4, 6]

// filter: keep matching
[1, 2, 3, 4].filter(x => x > 2);  // [3, 4]

// reduce: accumulate
[1, 2, 3, 4].reduce((sum, x) => sum + x, 0);  // 10

// Chaining
arr.filter(x => x > 0)
   .map(x => x * 2)
   .reduce((sum, x) => sum + x, 0);
```

## Sorting

### Basic Sort
```javascript
// Numeric sort (default is string sort!)
arr.sort((a, b) => a - b);          // Ascending
arr.sort((a, b) => b - a);          // Descending

// Sort objects
const objs = [{val: 3}, {val: 1}];
objs.sort((a, b) => a.val - b.val);

// Sort strings
strs.sort();                         // Alphabetical
strs.sort((a, b) => a.localeCompare(b));  // Better
```

## Destructuring

```javascript
// Array destructuring
const [a, b, c] = [1, 2, 3];
const [first, ...rest] = [1, 2, 3, 4];  // first=1, rest=[2,3,4]

// Object destructuring
const {name, age} = {name: 'John', age: 30};
const {x: newX, y: newY} = {x: 1, y: 2};  // Rename

// Swap
[a, b] = [b, a];
```

## Spread Operator

```javascript
// Array spread
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4];  // [1, 2, 3, 4]

// Object spread
const obj1 = {a: 1};
const obj2 = {...obj1, b: 2};  // {a: 1, b: 2}

// Function arguments
const nums = [1, 2, 3];
Math.max(...nums);             // 3
```

## Useful Math Functions

```javascript
Math.max(...arr);              // Maximum
Math.min(...arr);              // Minimum
Math.floor(5.9);               // 5
Math.ceil(5.1);                // 6
Math.round(5.5);               // 6
Math.abs(-5);                  // 5
Math.pow(2, 3);                // 8
Math.sqrt(16);                 // 4
Number.isInteger(5);           // true
Number.isInteger(5.5);         // false
```

## Performance Tips

### Avoid
```javascript
// Slow: string concatenation
let result = '';
for (let i = 0; i < 1000; i++) {
    result += i;  // Creates new string each time
}

// Fast: use array and join
const arr = [];
for (let i = 0; i < 1000; i++) {
    arr.push(i);
}
arr.join('');
```

### Use Object for Frequency
```javascript
// Slow: array.includes for checking
if (arr.includes(val)) { }  // O(n)

// Fast: use Set
const set = new Set(arr);
if (set.has(val)) { }  // O(1)
```

## Type Conversion

```javascript
// To number
Number("5");                // 5
parseInt("5");              // 5
parseFloat("5.5");          // 5.5
+"5";                       // 5

// To string
String(5);                  // "5"
5 + '';                     // "5"
`${5}`;                     // "5"

// To boolean
Boolean(1);                 // true
Boolean(0);                 // false
!!1;                        // true
```

## Debugging

```javascript
console.log(value);
console.table(array);       // Table format
console.time('label');      // Start timer
console.timeEnd('label');   // End timer
console.assert(cond);       // Assert
debugger;                   // Breakpoint

// Check type
typeof value;               // Get type
Array.isArray(arr);         // Check if array
```
