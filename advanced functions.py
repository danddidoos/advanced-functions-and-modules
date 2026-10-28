def mad(a,b,c=1):
    return (a*b)+c

x = mad(2,3)
print(x)

#Example of using functions with a default value for the argument 

def recurse(n):
    if n<10 :
        print(n)
        recurse(n+1)
recurse(1)

#Example of recursion

x = 100
def f():
    print("Inside f:",x)
f()
print("Outside f:", x)

def g():
    y= 100
    print("Inside g:", y)
y=50
g()
print("Outside g:", y)

#Global vs local scope variables

