# #Arrays
# arr = [10 , 20 , 30 , 40 ,50]

# print(arr[0]) # -> 10

# arr.append(60) # -> [10 , 20 , 30 , 40 ,50 , 60] add to end 60
# arr.insert(2, 99) # -> [10 , 20 , 99 , 30 , 40 , 50 , 60] add 99
# arr.pop(2) # -> [10 , 20 , 30 , 40 ,50 , 60] deleted 99

# print(arr) # print all arr







def sum_evens(arr):
    total = 0
    for i in arr:
        if i % 2 == 0:
            total += i
    return total

arr = [1 , 2, 3, 4 ,5  ,6 ,7 ,8 ,9 , 0, 10 ,11, 12, 10 , 120 ,130]
print(sum_evens(arr))