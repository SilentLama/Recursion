# since the code gets run line by line. The function will wait for it's new instance to return before running the next line of code so it stays in memory.
# The instance of the recursion can only return once the base statement (n < 1) is met, resulting in a backwards loop.

def fun1(n):
    
    if n < 1:
        return
    print(n)
    fun1(n-1)
    print(n)
    return


# fun1(4)

def fun2(x, y):
    if x == 0:
        return y
    return fun2(x - 1, x + y)

# print(fun2(3, 4))

##### Write a Python program to calculate the sum of a list of numbers. #####
# the list the first index of the list gets added to the second index. The sliced list (worked index gets sliced off) is going into the next recursion 
# until there's only one value left
def calculate_sum(li):
    if len(li) == 1:
        return li[0]
    return li[0] + calculate_sum(li[1:])    

# li = [1,2,3,4,5,6,7,8,9]
# print(calculate_sum(li))



##### Write a Python program to get the factorial of a non-negative integer. #####
# for each value between n to 1. n gets multiplied with n-1. (Imagine the backwards loop when n <= 1)
# normal factorial of n: n*(n-1)*(n-2)*(n-3)*[...]*1
# recursion calculation: 1*[...]*(n-3)*(n-2)*(n-1)*n
def factorial(n):
    if n <= 1:
        return n
    return n*factorial(n-1)

# print(factorial(5))


##### Write a Python program to get the factorial of a non-negative integer. #####

def fibonacchi(n):
    if n == 1 or n == 2:
        return 1
    return fibonacchi(n - 1) + fibonacchi(n - 2)

# print(fibonacchi(50))


##### Write a Python program of recursion list sum. Go to the editor #####
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
# In essence the function goes into a list and adds every item to a total. 
# If the item happens to be another list we could just run the same code over it again to extract the values.
def sum_nested_list(li):
    total = 0
    for item in li:
        if type(item) == type([]):
            total += sum_nested_list(item)
        else:
            total += item
    return total

# li = [1, 2, [3,4], [5,6]]
# print(sum_nested_list(li))

##### Write a Python program to get the sum of a non-negative integer. Go to the editor #####
# Test Data: 
# sumDigits(345) -> 12
# sumDigits(45) -> 9 
# With Modulo of 10 you can get the last number of any multi-digit-number
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(int(n / 10))

# print(digit_sum(345))


##### Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). Go to the editor #####
# Test Data: 
# sum_series(6) -> 12
# sum_series(10) -> 30 

def calculate_sum_row(n):
    if n <= 1:
        return n
    return n + calculate_sum_row(n - 2)

# print(calculate_sum_row(10))


##### Write a Python program to calculate the value of 'a' to the power 'b'. #####

def to_the_power(n, x):
    if x == 1:
        return n
    return n * to_the_power(n, x - 1)

# print(to_the_power(3, 4))

#####   Write a Python program to find  the greatest common divisor (gcd) of two integers.   #####
def greatest_common_divisor(x, y):
    low = min(x, y)
    high = max(x, y)

    if low == 0:
	    return high
    elif low == 1:
	    return 1
    else:
        return greatest_common_divisor(low, high % low)

print(greatest_common_divisor(342, 540))


