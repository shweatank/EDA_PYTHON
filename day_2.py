def logic_and(a,b):
    c=a&b
    return c
def logic_or(a,b):
    c=a | b
    return c
def logic_not(a):
    if a==1:
        return 0
    else:
        return 1
print(r"x, y, out")
for i in range(2):
    for j in range(2):
        print(i,j,logic_and(i,j))
print("\nx, y, out")
for i in range(2):
    for j in range(2):
        print(i,j,logic_or(i,j))
print("\nx, out")
for i in range(2):
    print(i,logic_not(i))