# List Programs
arr = [1,2,3,4,5]

# Print Numbers
for i in range(len(arr)):
    print(i)

# print Forward
arr = [1,2,3,4,5,6]
print(arr)

# Print Reverse
arr = [1,2,3,4,5,6]
print(arr[::-1])

# Insert at End
arr = [1,2,3,4,5,6]
arr.append(21)
print(arr)

# Insert at Start
arr = [1,2,3,4,5,6]
arr.insert(0,10) # 0 in index
print(arr)

# Insert At Position
arr = [1,2,3,4,5,6]
arr.insert(2,10) # insert at index 2
print(arr)

# Delete from Start/End/Position
arr = [1,2,3,4,5,6]
last = len(arr) -1
del arr[last] # "last" is the index which want to del 
print(arr)

# 

