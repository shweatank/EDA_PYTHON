def half_adder(a,b):
    return a^b
def half_adder_carry(a,b):
    c= a and b
    return c
for a in range(0,2):
    for b in range(0,2):
        print(f"{a}  {b}    {half_adder(a,b)}        {half_adder_carry(a,b)}")