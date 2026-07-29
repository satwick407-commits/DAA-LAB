n = int(input("Enter the number of elements: "))

print("Enter the elements:")
arr = list(map(int, input().split()))

key = int(input("Enter the element to search: "))

found = -1

for i in range(n):
    if arr[i] == key:
        found = i
        break

if found != -1:
    print("Element found at position", found + 1)
else:
    print("Element not found")