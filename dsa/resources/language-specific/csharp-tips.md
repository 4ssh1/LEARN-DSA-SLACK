# C# Tips for DSA

## Arrays and Collections

### Arrays
```csharp
// Fixed size array
int[] arr = new int[10];
int[] arr = new int[] {1, 2, 3};
int[] arr = {1, 2, 3};                  // Initializer

// Multi-dimensional
int[,] matrix = new int[5, 3];
int[,] matrix = {{1, 2, 3}, {4, 5, 6}};

// Jagged array
int[][] jagged = new int[5][];
jagged[0] = new int[3];

// Length
int length = arr.Length;
```

### List (Dynamic Array)
```csharp
// Create
List<int> list = new List<int>();
List<int> list = new List<int>(10);     // Capacity
List<int> list = new List<int> {1, 2, 3};

// Operations
list.Add(4);                            // O(1) amortized
list.Remove(4);                         // O(n)
list.RemoveAt(0);                       // O(n)
list.Insert(0, 0);                      // O(n)
list.Contains(2);                       // O(n)
list.IndexOf(2);                        // O(n)
list.Clear();                           // Remove all

// Properties
int count = list.Count;                 // Size
list.Capacity;                          // Allocated size

// Iteration
foreach (int item in list)
{
    Console.WriteLine(item);
}

// LINQ
var doubled = list.Select(x => x * 2).ToList();
var filtered = list.Where(x => x > 2).ToList();
```

## Dictionary (Hash Map)

### Basic Operations
```csharp
// Create
Dictionary<int, int> dict = new Dictionary<int, int>();
Dictionary<string, int> map = new();     // Type inference

// Add/Access
dict[5] = 10;                           // Add or update: O(1)
dict.Add(5, 10);                        // Add (throws if exists)
dict.TryAdd(5, 10);                     // Returns bool

// Access
int value = dict[5];                    // Throws if not found
dict.TryGetValue(5, out int val);       // Safe access

// Check/Remove
dict.ContainsKey(5);                    // O(1)
dict.Remove(5);                         // O(1)

// Iterate
foreach (var kvp in dict)
{
    int key = kvp.Key;
    int value = kvp.Value;
}

// Keys/Values
dict.Keys;                              // ICollection<TKey>
dict.Values;                            // ICollection<TValue>
```

## HashSet (Unique Elements)

```csharp
// Create
HashSet<int> set = new HashSet<int>();
HashSet<int> set = new() {1, 2, 2, 3}; // {1, 2, 3}

// Operations
set.Add(5);                             // O(1)
set.Remove(5);                          // O(1)
set.Contains(5);                        // O(1)

// Set operations
set.UnionWith(other);                   // Union
set.IntersectWith(other);               // Intersection
set.ExceptWith(other);                  // Difference

// Properties
int count = set.Count;
```

## SortedDictionary & SortedSet

```csharp
// SortedDictionary (ordered by key)
SortedDictionary<int, string> sorted = new();
sorted.Add(3, "three");
sorted.Add(1, "one");
// Iteration order: 1, 3

// SortedSet (ordered, unique)
SortedSet<int> sortedSet = new() {5, 2, 8, 2};
// {2, 5, 8}
```

## Stacks and Queues

```csharp
// Stack (LIFO)
Stack<int> stack = new();
stack.Push(1);                          // Add: O(1)
int top = stack.Pop();                  // Remove & return: O(1)
int peek = stack.Peek();                // View top: O(1)
bool empty = stack.Count == 0;

// Queue (FIFO)
Queue<int> queue = new();
queue.Enqueue(1);                       // Add: O(1)
int front = queue.Dequeue();            // Remove & return: O(1)
int peek = queue.Peek();                // View front: O(1)

// Priority Queue
PriorityQueue<int, int> pq = new();
pq.Enqueue(5, 5);                       // Element, priority
int min = pq.Dequeue();
```

## String Operations

```csharp
string s = "hello";

// Properties
s.Length;                               // 5
s[0];                                   // 'h'

// Modification
s.ToUpper();                            // "HELLO"
s.ToLower();                            // "hello"
s.Trim();                               // Remove whitespace
s.Replace("l", "x");                    // "hexxo"
s.Substring(1, 3);                      // "ell"
s.Split(' ');                           // Split into array

// Search
s.Contains("ell");                      // true
s.IndexOf("l");                         // 2
s.StartsWith("he");                     // true
s.EndsWith("lo");                       // true

// Join
string.Join(",", new[] {"a", "b", "c"}); // "a,b,c"

// Concatenation
string result = s + " world";           // Avoid in loops!
string result = $"{s} world";           // String interpolation (better)

// StringBuilder (for many concatenations)
StringBuilder sb = new();
sb.Append("hello");
sb.Append(" ");
sb.Append("world");
string result = sb.ToString();
```

## LINQ Essentials

```csharp
List<int> nums = new() {1, 2, 3, 4, 5};

// Filtering
nums.Where(x => x > 2);                 // {3, 4, 5}

// Transformation
nums.Select(x => x * 2);                // {2, 4, 6, 8, 10}

// Aggregation
nums.Sum();                             // 15
nums.Average();                         // 3.0
nums.Max();                             // 5
nums.Min();                             // 1
nums.Count();                           // 5

// Existence checks
nums.Any(x => x > 4);                   // true
nums.All(x => x > 0);                   // true

// Accumulation
nums.Aggregate((acc, x) => acc + x);    // 15

// Sorting
nums.OrderBy(x => x);                   // Ascending
nums.OrderByDescending(x => x);         // Descending
nums.Reverse();                         // Reverse

// Distinct
nums.Distinct();                        // Remove duplicates

// Take/Skip
nums.Take(3);                           // {1, 2, 3}
nums.Skip(2);                           // {3, 4, 5}

// Convert
nums.ToList();                          // List<int>
nums.ToArray();                         // int[]
nums.ToHashSet();                       // HashSet<int>
nums.ToDictionary(x => x, x => x * 2); // Dict by key, value
```

## Useful Patterns

### Two Pointer
```csharp
int[] arr = {1, 2, 3, 4, 5};
int left = 0, right = arr.Length - 1;

while (left < right)
{
    if (arr[left] + arr[right] == target)
        return new[] {left, right};
    else if (arr[left] + arr[right] < target)
        left++;
    else
        right--;
}
```

### Frequency Counter
```csharp
string s = "hello";
Dictionary<char, int> freq = new();

foreach (char c in s)
{
    if (freq.ContainsKey(c))
        freq[c]++;
    else
        freq[c] = 1;
}

// Or using LINQ
var freq = s.GroupBy(c => c)
            .ToDictionary(g => g.Key, g => g.Count());
```

### Sliding Window
```csharp
string s = "abcabcbb";
int maxLen = 0;
Dictionary<char, int> charCount = new();
int left = 0;

for (int right = 0; right < s.Length; right++)
{
    charCount[s[right]] = charCount.GetValueOrDefault(s[right], 0) + 1;
    
    while (charCount.Values.Any(v => v > 1))
    {
        charCount[s[left]]--;
        if (charCount[s[left]] == 0)
            charCount.Remove(s[left]);
        left++;
    }
    
    maxLen = Math.Max(maxLen, right - left + 1);
}
```

### Binary Search
```csharp
int BinarySearch(int[] arr, int target)
{
    int left = 0, right = arr.Length - 1;
    
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}
```

## Type Conversion

```csharp
// String conversions
int num = int.Parse("123");             // Throws if invalid
int.TryParse("123", out int num);       // Returns bool

// Casting
int x = 5;
double y = (double)x;                   // Explicit cast
object obj = 5;
int num = (int)obj;                     // Unboxing

// ToString
int.ToString();                         // "5"
(5.5).ToString();                       // "5.5"
true.ToString();                        // "True"
```

## Useful Methods

### Math
```csharp
Math.Abs(-5);                           // 5
Math.Max(3, 7);                         // 7
Math.Min(3, 7);                         // 3
Math.Pow(2, 3);                         // 8
Math.Sqrt(16);                          // 4
Math.Floor(5.9);                        // 5
Math.Ceil(5.1);                         // 6
Math.Round(5.5);                        // 6
```

### Common Mistakes

```csharp
// Wrong: Modifying collection during iteration
foreach (var item in list)
{
    if (item > 5)
        list.Remove(item);              // DANGER!
}

// Correct: Use where to filter
list = list.Where(x => x <= 5).ToList();

// Wrong: Comparing string with ==
if (str1 == str2) { }                   // Compares reference!

// Correct: Use Equals
if (str1.Equals(str2)) { }              // Compares value
if (string.Equals(str1, str2)) { }      // More explicit

// Wrong: List parameters are passed by reference
void Modify(List<int> list)
{
    list.Add(5);                        // Modifies original!
}

// Correct: Create copy if needed
void Modify(List<int> list)
{
    var copy = new List<int>(list);
    copy.Add(5);
}
```

## Performance Tips

1. Use List<T> for dynamic arrays (not ArrayList)
2. Use Dictionary for O(1) lookups, not List.Contains()
3. Use StringBuilder for string concatenation in loops
4. LINQ is convenient but can be inefficient - profile before optimizing
5. Avoid boxing/unboxing (use generics)
6. Use async/await for I/O operations
7. Consider using Span<T> for performance-critical code

## Tips

1. C# has strong type safety - leverage it
2. Use var for type inference when obvious
3. Use null-coalescing operator (??)
4. Use null-conditional operator (?.)
5. Use pattern matching for cleaner code
6. Leverage LINQ for collections
7. Test with xUnit framework
