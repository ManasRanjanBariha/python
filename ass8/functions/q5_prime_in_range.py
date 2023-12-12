def is_prime(x):
    for i in range(2,x-1):
        if x%i==0:
            return False

    return True

def prime_in_range(x,y):
    for i in range(x,y):
        if(is_prime(i)):
            print(i,end=" ")
prime_in_range(10,100)
