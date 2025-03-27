def half_adder(i,j):
    return i^j , i&j

for i in [0,1]:
    for j in [0,1]:
        print(half_adder(i,j))

