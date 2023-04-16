# Binary Search Algorithm
# Recursive Method
# Time Complexity: O(log n)
# Space Complexity: O(log n)

def binary_search(input_list, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if x == input_list[mid]:
            return mid
        elif x < input_list[mid]:
            return binary_search(input_list, low, mid - 1, x)  # x is on left side
        else:
            return binary_search(input_list, mid + 1, high, x)  # x is on right side
    else:
        return -1   # x is not present in the list 



input_list = []
n = int(input("Print number of elements : "))
print("Enter elements : ")

for i in range(0, n):
    ele = input()
    input_list.append(ele)

x = input("Enter search item : ")
    
result = binary_search(input_list, 0, len(input_list) - 1, x)

if result == -1:
    print("Search item not found")
else:
    print("Search item found at index ",result)

