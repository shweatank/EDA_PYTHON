#----------------------------------wave form-------------------------------

import matplotlib.pyplot as plt
def logic_and(a, b):
    return a & b

def logic_or(a, b):
    return a | b

def logic_not(a):
    return 1 - a

def logic_nand(a, b):
    return logic_not(logic_and(a, b))

def logic_nor(a, b):
    return logic_not(logic_or(a, b))

inputs = [(i, j) for i in range(2) for j in range(2)]

x_vals = [f"({i},{j})" for i, j in inputs]

plt.figure(figsize=(12, 8))

and_output = [logic_and(i, j) for i, j in inputs]
plt.subplot(3, 2, 1)
plt.plot(x_vals, and_output, marker='o', linestyle='-', color='b')
plt.title("AND Gate")
plt.ylabel("Output")

or_output = [logic_or(i, j) for i, j in inputs]
plt.subplot(3, 2, 2)
plt.plot(x_vals, or_output, marker='o', linestyle='-', color='g')
plt.title("OR Gate")
plt.ylabel("Output")

not_output = [logic_not(i) for i, _ in inputs]
plt.subplot(3, 2, 3)
plt.plot([str(i) for i, _ in inputs], not_output, marker='o', linestyle='-', color='orange')
plt.title("NOT Gate")
plt.ylabel("Output")

nand_output = [logic_nand(i, j) for i, j in inputs]
plt.subplot(3, 2, 4)
plt.plot(x_vals, nand_output, marker='o', linestyle='-', color='r')
plt.title("NAND Gate")
plt.ylabel("Output")

nor_output = [logic_nor(i, j) for i, j in inputs]
plt.subplot(3, 2, 5)
plt.plot(x_vals, nor_output, marker='o', linestyle='-', color='purple')
plt.title("NOR Gate")
plt.ylabel("Output")

plt.tight_layout()
plt.show()


#------------------------------ logic ----------------------------------------

def comb_logic(a,b,c):
    an1=a&b
    a1=1-a
    b1=1-b
    an2=(a1&b1)&c
    fin=an1|an2
    return fin
print(r"x  |  y  |  z  |  out")
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f"{i}  |  {j}  |  {k}  |  {comb_logic(i,j,k)}")
