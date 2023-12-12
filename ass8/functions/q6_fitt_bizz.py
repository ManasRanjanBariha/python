def fun(x):
    if x % 5==0 and x%3 ==0:
        return "FizzBuz"
    elif x% 5==0:
        return "Buzz"
    elif x%3==0:
        return "Fizz"
    else:
        return x

print(fun(10))
print(fun(51))
print(fun(15))
print(fun(77))
