# Selection Sort
# Repeatedly select the minimum element from the unsorted part
# and move it to the sorted part.
# Time Complexity: O(n^2)

n = int(input("Enter number of elements: "))

arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    min_index = i

    # Find minimum in arr[i...n-1]
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap arr[i] and arr[min_index]
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:", end=" ")
for num in arr:
    print(num, end=" ")
