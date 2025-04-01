# truth tables for and or  and not

def and_gate(a,b):
    return a and b
def or_gate(a,b):
    return a or b
def not_gate(a):
    return int(not(a))
def nand_gate(a,b):
    return int(not(a and b))
def nor_gate(a,b):
    return int(not(a or b))
print("X  |  Y  |AND(X.Y)|OR(X+Y)|NOT(X)|NAND(X,Y)|NOR(X,Y)")
print("-------------------------------------")
for a in range(0,2):
    for b in range(0,2):
        print(f"{a}   {b}     {and_gate(a,b)}       {or_gate(a,b)}       {not_gate(a)}         {nand_gate(a,b)}       {nor_gate(a,b)}")