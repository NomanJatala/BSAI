print("Binary Search Progarmm ")
arr = []
n = int(input("Enter numbers of element:"))
for i in range(n):
    arr.append(int(input("=>")))


item = int(input("Enter number to search:"))
low = 0
high = n-1

def binary_search(arr,low,high,item):
    if low <=high:
        mid = (low + high) //2

        if arr[mid] == item:
            print(f"item is at {mid} index")
        elif arr[mid] > item:
            binary_search(arr,low,mid-1,item)
        else:
            binary_search(arr,mid+1,high,item)

    else:
        print("Element not found")

    


binary_search(arr,low,high,item)