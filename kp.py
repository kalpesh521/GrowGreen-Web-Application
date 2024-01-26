def findLargestNumber(arr):
    # Custom comparator function to compare two numbers as strings
    def customComparator(x, y):
        return int(y + x) - int(x + y)
    
    # Convert array elements to strings and sort using customComparator
    arr_str = [str(x) for x in arr]
    arr_str.sort(key=customComparator)
    
    # Join the sorted strings to form the largest number
    largest_number = ''.join(arr_str)
    return largest_number

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the size of the array and the elements
    N = int(input())
    arr = list(map(int, input().split()))
    
    # Call the function and print the result
    result = findLargestNumber(arr)
    print(result)
