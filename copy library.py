import copy #Practicing with the copy library

L = [[1,2],[3,4],[5,6]]
L1 = copy.deepcopy(L)
L[0][0] = 20
print(L)
print(L1)