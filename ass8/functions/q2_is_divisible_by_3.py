def is_div(x):
    num=x%10
    if(num%3==0):
        return True
    return False

n=int(input("Enter a number"))
if is_div(n):
    print("Divisible")
else:
    print("Not divisible")
