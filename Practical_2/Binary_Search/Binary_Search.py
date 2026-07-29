n = int(input("Enter the number of elements: "))

print("Enter the elements (sorted):")
arr = list(map(int, input().split()))

key = int(input("Enter the element to search: "))

low = 0
high = n - 1
found = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        found = mid
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found != -1:
    print("Element found at position", found + 1)
else:
    print("Element not found")