import numpy as np
l1 = [[[1,2,3], [4,5,6]],[[7,8,9,],[10,11,12]]]
l2 = [[[1,2,np.nan], [4,5,6]],[[7,np.nan,9,],[10,11,12]]]

print(l1[0])
test1 = np.mean(l1[0])
print(test1)

test2 = np.mean(l2[0])
print(test2)

test3 = np.nanmean(l2[0])
print(test3)

l3 = []
for i in range(0, len(l2)):
    tmp = np.nanmean(l2[i])
    l3.append(tmp)

print(l3)