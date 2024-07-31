'''Your task is to make two functions ( max and min, or maximum and minimum, 
etc., depending on the language ) that receive a list of integers as input, 
and return the largest and lowest number in that list, respectively.'''
# def minimum(arr):
#     min_arr=min(arr)
#     return min_arr

# def maximum(arr):
#     max_arr=max(arr)
#     return max_arr

'''Your task is to create a function that does four basic mathematical operations.
The function should take three arguments - operation(string/char), value1(number), 
value2(number).
The function should return result of numbers after applying the chosen operation.'''
# def basic_op(operator, value1, value2):
#     res=(value1,operator,value2)
#     c=''.join(res)
#     d=eval(c)
#     return d
# a=basic_op('*','4','2')
# print(a)

'''Sum all the numbers of a given array ( cq. list ), except the highest and the lowest 
element ( by value, not by index! ).The highest or lowest element respectively is a single 
element at each edge, even if there are more than one with the same value.
Mind the input validation.'''
# def sum_array(arr):
#     arr.sort()
#     b=arr[1:-1]
#     s=0
#     for i in b:
#         s=s+i
#     return s
# a=sum_array([1,2,3,10,4])
# print(a)

'''Given a string of digits, you should replace any digit below 5 with '0' and 
any digit 5 and above with '1'. Return the resulting string.
Note: input will never be an empty string'''
def fake_bin(x):
    x=int(x)
    if x<=5:
        x=0
    else:
        x=1
    return x
f=fake_bin(6)
print(f)



