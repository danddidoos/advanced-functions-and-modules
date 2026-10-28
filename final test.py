import copy
def hypotenuse(a=3, b=4):
    return (a**2 + b**2)**0.5

print(hypotenuse())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

list = [1,2,3,4,5]
list1 = copy.copy(list)
list[0] = 10
print(list)
print(list1)

set = {(5,4), (2,2), (3,1)}
set1 = copy.deepcopy(set)
set.add((0,0))
print(set)
print(set1)

def filename():
    while True:
        try:
            filename = input("Enter a filename: ")
            if filename.strip():
                return filename
        except:
            print("Invalid input. please try again")


filename()

