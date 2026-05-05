# 1
double = lambda x : x * x
print('#1')
print(double(4))
# 2
add = lambda x: x + x
print('#2')
print(add(2))
# 3
max = lambda x , y: x if x > y else y  
print('#3')
print(max(4 , 9 ))
# 4
min = lambda x , y: x if x < y else y
print('#4')
print(min(5, 8))
# 5  
is_even = lambda x : x % 2 == 0 
print('#5')
print(is_even(8))
print(is_even(11))
# 6 
age_check = lambda x: True if x >= 18 else False
print('#6')
print(age_check(17))
print(age_check(19))