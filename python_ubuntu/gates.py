def and_gate(a: int, b: int) -> int:
    return a and b

def or_gate(a: int, b: int) -> int:
    return a or b

def not_gate(a: int) -> int:
    return 1 if not a else 0

print("AND GATE")
for i in range(2):
    for j in range(2):
        print(f"{i}, {j} = {and_gate(i, j)}")

print("OR GATE")
for i in range(2):
    for j in range(2):
        print(f"{i}, {j} = {or_gate(i, j)}")

print("NOT GATE")
for i in range(2):
    print(f"{i} = {not_gate(i)}")
        

        


