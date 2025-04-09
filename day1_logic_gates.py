def and_gate(a,b):
    return  a and b

def or_gate(a,b):
    return  a or b

def not_gate(a):
    return  not a

def nor_gate(a,b):
    return  not(a or b)

def nand_gate(a,b):
    return  not(a and b)

def xor_gate(a,b):
    return  a ^ b

def xnor_gate(a,b):
    return  not(a ^ b )

for i in range(2):
    for j in range(2):
        print(xnor_gate(i,j))
