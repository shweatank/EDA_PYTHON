def not_gate(n):
    if n==1:
        return 0
    else: return 1

def or_gate(i,j):
    return i|j

def and_gate(i,j):
    return i&j

a=[0,1]
b=[0,1]
for i in a:
    for j in b:
        x=not_gate(and_gate(i,j))
        y=not_gate(and_gate(i,j))
        z=not_gate(or_gate(x,y))
        # print(i,j,x,y,z)











