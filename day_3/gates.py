def or_gate(a,b):
    return a|b

def and_gate(a,b):
    return a&b

def not_gate(a):
    return 1 if not a else 0

print("OR GATE")
for i in [0,1]:
    for j in [0,1]:
        print(f'{i} {j}={or_gate(i,j)}')


print("AND GATE")
for i in [0,1]:
    for j in [0,1]:
        print(f'{i} {j}={and_gate(i,j)}')

print('NOT GATE')
for i in [0,1]:
    print(f'{i}={not_gate(i)}')