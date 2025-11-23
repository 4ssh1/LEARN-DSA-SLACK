# C++ Setup Guide

## Compiler Installation

### Windows

#### Using MinGW

1. **Download MinGW**
   - Visit [MinGW website](http://www.mingw.org/)
   - Download installer

2. **Install**
   - Select g++, gcc, mingw32-make
   - Add to PATH

3. **Verify**
   ```bash
   g++ --version
   ```

#### Using Visual Studio

1. Download Visual Studio Community
2. Select "Desktop development with C++"
3. Install MSVC compiler

### macOS

```bash
# Using Homebrew
brew install gcc

# Or install Xcode Command Line Tools
xcode-select --install

# Verify
g++ --version
clang++ --version
```

### Linux (Ubuntu/Debian)

```bash
# Install compiler
sudo apt update
sudo apt install build-essential

# Verify
g++ --version
gcc --version
```

## Setting Up Build Tools

### CMake

```bash
# Install
# Windows: download from cmake.org
# macOS: brew install cmake
# Linux: sudo apt install cmake

# Verify
cmake --version
```

### Make (already included with build tools)

```bash
# Verify
make --version
```

## IDE Setup

### VS Code

1. **Install Extensions**
   - C/C++ (Microsoft)
   - C/C++ Extension Pack
   - Code Runner

2. **Configure (launch.json)**
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "g++ - Build and debug",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/a.out",
      "args": [],
      "stopAtEntry": false,
      "cwd": "${fileDirname}",
      "environment": [],
      "externalConsole": true,
      "MIMode": "gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ],
      "preLaunchTask": "C/C++: g++ build"
    }
  ]
}
```

### CLion

1. Download JetBrains CLion
2. Built-in C++ support
3. Configure compiler in Settings

### Code::Blocks

1. Download Code::Blocks
2. Install with compiler bundle
3. Create new project

## Compiling

### Basic Compilation

```bash
# Simple compile
g++ solution.cpp -o solution

# With optimization
g++ -O2 solution.cpp -o solution

# With debugging
g++ -g solution.cpp -o solution

# With warnings
g++ -Wall -Wextra solution.cpp -o solution
```

### Running

```bash
# Windows
solution.exe

# macOS/Linux
./solution
```

## Project Structure

```
dsa-practice/
├── CMakeLists.txt
├── src/
│   ├── week01/
│   │   ├── two_sum.cpp
│   │   └── best_time.cpp
│   └── week02/
├── include/
│   └── algorithms.h
├── tests/
│   ├── test_week01.cpp
│   └── CMakeLists.txt
└── build/
```

## CMakeLists.txt Example

```cmake
cmake_minimum_required(VERSION 3.10)
project(dsa_practice)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Main executable
add_executable(solution src/solution.cpp)

# Include directories
target_include_directories(solution PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
```

## Testing

### Using Google Test

```bash
# Install
# Can use package manager or git clone

# CMakeLists.txt
enable_testing()
add_executable(tests tests/test_suite.cpp)
target_link_libraries(tests gtest gtest_main)
add_test(NAME AllTests COMMAND tests)
```

### Manual Testing

```cpp
#include <iostream>
#include <cassert>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    // Implementation
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    auto result = twoSum(nums, 9);
    assert(result[0] == 0 && result[1] == 1);
    cout << "Test passed!" << endl;
    return 0;
}
```

## Common Libraries

### STL Containers

```cpp
#include <vector>      // Dynamic array
#include <map>         // Ordered map
#include <unordered_map>  // Hash map
#include <set>         // Ordered set
#include <unordered_set>  // Hash set
#include <queue>       // Queue
#include <stack>       // Stack
#include <deque>       // Double-ended queue
```

### Algorithms

```cpp
#include <algorithm>   // sort, binary_search, etc
#include <numeric>     // accumulate, iota, etc
```

## Debugging

### Using GDB

```bash
# Compile with debugging symbols
g++ -g solution.cpp -o solution

# Run with gdb
gdb ./solution

# GDB commands
run         - Run program
break main  - Set breakpoint
next        - Next line
step        - Step into
print var   - Print variable
quit        - Exit
```

## Performance Tips

### Optimization Flags

```bash
# -O0: No optimization (default)
# -O1: Basic optimization
# -O2: Standard optimization
# -O3: Aggressive optimization
# -Os: Optimize for size

g++ -O2 solution.cpp -o solution
```

### Measuring Performance

```cpp
#include <chrono>

auto start = chrono::high_resolution_clock::now();
// Code to measure
auto end = chrono::high_resolution_clock::now();
auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);
cout << "Time: " << duration.count() << "ms" << endl;
```

## Common Issues

### Undefined Reference

```bash
# Compile all source files
g++ src/main.cpp src/utils.cpp -o program
```

### Library Not Found

```bash
# Link library
g++ solution.cpp -o solution -lm  # -lm for math library
```

### Path Issues

```bash
# Include path
g++ solution.cpp -I/path/to/include -o solution

# Library path
g++ solution.cpp -L/path/to/lib -lmylib -o solution
```

## Tips

1. Use -Wall -Wextra for development
2. Use -O2 for competitive programming
3. Compile frequently while developing
4. Use meaningful variable names
5. Comment complex logic
