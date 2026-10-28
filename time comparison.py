import copy
import time

nested_data = []
for i in range(1000):
    inner_list = []
    for j in range(100):
        inner_list.append(j)
    nested_data.append(inner_list)

start = time.perf_counter()
shallow = copy.copy(nested_data)
shallow_time = time.perf_counter() - start

start = time.perf_counter()
deep = copy.deepcopy(nested_data)
deep_time = time.perf_counter() - start

print("Shallow copy time:", round(shallow_time, 6), "seconds")
print("Deep copy time:", round(deep_time, 6), "seconds")

infile = open("example.txt")
s = infile.read(20)
print(s)
infile.close()

outfile = open("example.txt", "w")
outfile.write("Hello\n")
outfile.write("Hello again")
x = outfile.readlines()
print(x)
outfile.close()