#Experimenting with global scope

x = 100
def f():
    x = 200
    print("Inside f:", x)
f()
print("Outside f:", x)