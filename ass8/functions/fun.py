def my_function(fname,lname):
	print(fname+" "+lname)

my_function("Emil","Parker")

#When the number of argument is not known
def my_fun(*kids):
    print("The yougest child is "+kids[2])
    print("The elder one is "+kids[0])
my_fun("Emil","John","TEd")

#when key value pair is passed and we don't know how many
#para is there

def my_name(**kid):
    print("Her last name is "+kid["lname"])

my_name(fname="Marie",lname="parker")

# default value of the para is null

def my_country(country="Norway"):
    print("I am from"+country)
my_country("India")
my_country("England")
my_country()

# WE can pass list to a a function directly
def my_list(subject):
    for i in subject:
        print(i)
my_list(["Dbms","os","Python"])


def power(x):
    return 5**x;
print(power(4))


#recursive function

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
print(gcd(16,40))
