# C# Setup Guide

## .NET Installation

### Windows

1. **Download .NET**
   - Visit [dotnet.microsoft.com](https://dotnet.microsoft.com/download)
   - Download latest LTS version (or latest)

2. **Install**
   - Run installer
   - Follow prompts
   - Restart may be required

3. **Verify**
   ```bash
   dotnet --version
   ```

### macOS

```bash
# Using Homebrew
brew install dotnet

# Or download from microsoft.com
# Visit https://dotnet.microsoft.com/download

# Verify
dotnet --version
```

### Linux (Ubuntu/Debian)

```bash
# Add Microsoft package repository
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb

# Install .NET
sudo apt update
sudo apt install dotnet-sdk-8.0

# Verify
dotnet --version
```

## Project Setup

### Create New Project

```bash
# Create console app
dotnet new console -n dsa-practice
cd dsa-practice

# Or create class library
dotnet new classlib -n dsa-algorithms
```

### Project Structure

```
dsa-practice/
├── dsa-practice.csproj
├── Program.cs
├── Algorithms/
│   ├── Week01/
│   │   ├── TwoSum.cs
│   │   └── BestTime.cs
│   └── Week02/
├── Tests/
│   ├── Week01Tests.cs
│   └── Week02Tests.cs
└── bin/
```

## IDE Setup

### Visual Studio Community

1. Download Visual Studio Community
2. Select ".NET desktop development" workload
3. Install
4. Create new C# Console App project

### Visual Studio Code

1. **Install Extensions**
   - C# (powered by OmniSharp)
   - C# Dev Kit
   - Roslyn analyzers

2. **Configure (launch.json)**
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${workspaceFolder}/bin/Debug/net8.0/dsa-practice.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "stopAtEntry": false,
            "console": "internalConsole"
        }
    ]
}
```

### JetBrains Rider

1. Download Rider
2. Built-in C# support
3. Create new C# Console App

## Building & Running

### Basic Commands

```bash
# Build project
dotnet build

# Run project
dotnet run

# Run with arguments
dotnet run -- arg1 arg2

# Run specific file
dotnet run --project path/to/project.csproj
```

### Create Executable

```bash
# Release build
dotnet build -c Release

# Publish standalone
dotnet publish -c Release -r win-x64 --self-contained

# Run executable
./bin/Release/net8.0/publish/dsa-practice.exe
```

## Testing Framework

### Setup xUnit

```bash
# Add xUnit to project
dotnet add package xunit
dotnet add package xunit.runner.visualstudio

# Add test project
dotnet new xunit -n dsa-practice.tests
```

### Write Tests

```csharp
using Xunit;
using dsa_practice;

public class TwoSumTests
{
    [Fact]
    public void TwoSum_FindsValidPair()
    {
        var solution = new Solution();
        int[] result = solution.TwoSum(new[] {2, 7, 11, 15}, 9);
        
        Assert.Equal(new[] {0, 1}, result);
    }

    [Theory]
    [InlineData(new[] {2, 7, 11, 15}, 9, new[] {0, 1})]
    [InlineData(new[] {3, 2, 4}, 6, new[] {1, 2})]
    public void TwoSum_MultipleInputs(int[] nums, int target, int[] expected)
    {
        var solution = new Solution();
        int[] result = solution.TwoSum(nums, target);
        
        Assert.Equal(expected, result);
    }
}
```

### Run Tests

```bash
# Run all tests
dotnet test

# Run specific test project
dotnet test Tests/dsa-practice.tests.csproj

# Run with verbose output
dotnet test -v d

# Run specific test
dotnet test --filter "FullyQualifiedName~TwoSumTests.TwoSum_FindsValidPair"
```

## NuGet Packages

### Useful Packages

```bash
# Testing
dotnet add package xunit
dotnet add package Moq

# Benchmarking
dotnet add package BenchmarkDotNet

# Debugging & Profiling
dotnet add package System.Diagnostics

# Collections extensions
dotnet add package System.Collections.Immutable
```

## Debugging

### Using Visual Studio

1. Set breakpoint (F9)
2. Start debugging (F5)
3. Step over (F10), Step into (F11)
4. Watch variables
5. View call stack

### Using Console Debugging

```csharp
// Debug output
Console.WriteLine($"Value: {value}");
System.Diagnostics.Debug.WriteLine("Debug message");

// Conditional breakpoint
#if DEBUG
    Console.WriteLine("Debug build");
#endif
```

## Performance Profiling

### Measuring Execution Time

```csharp
using System.Diagnostics;

var stopwatch = Stopwatch.StartNew();

// Code to measure
Array.Sort(largeArray);

stopwatch.Stop();
Console.WriteLine($"Time: {stopwatch.ElapsedMilliseconds}ms");
```

### Using BenchmarkDotNet

```bash
dotnet add package BenchmarkDotNet
```

```csharp
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

[SimpleJob(warmupCount: 3, targetCount: 5)]
[MemoryDiagnoser]
public class SortingBenchmark
{
    private int[] data;

    [GlobalSetup]
    public void Setup()
    {
        data = new int[10000];
        for (int i = 0; i < data.Length; i++)
            data[i] = Random.Shared.Next();
    }

    [Benchmark]
    public void BubbleSort()
    {
        // Bubble sort implementation
    }

    [Benchmark]
    public void QuickSort()
    {
        // Quick sort implementation
    }
}

// Run
BenchmarkRunner.Run<SortingBenchmark>();
```

## Common Commands

```bash
# Create new project
dotnet new console -n MyApp
dotnet new classlib -n MyLibrary
dotnet new xunit -n MyTests

# Manage packages
dotnet add package PackageName
dotnet remove package PackageName
dotnet list package

# Clean & rebuild
dotnet clean
dotnet build

# Publish
dotnet publish -c Release

# Watch mode (auto-rebuild)
dotnet watch run
```

## Tips

1. Use async/await for I/O operations
2. Use LINQ for collection operations
3. Leverage built-in Collections (List, Dictionary, HashSet)
4. Use string interpolation ($"text {var}")
5. Enable nullable reference types
6. Use records for immutable data
7. Test frequently with `dotnet test`
