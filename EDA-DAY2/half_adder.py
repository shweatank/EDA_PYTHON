print("A   |  B  |  SUM  |  CARRY_OUT")
for i in[0,1]:
    for j in[0,1]:
        summation=i^j
        carry_out=i&j
        print(f"{i}  |  {j}  |  {summation}  |  {carry_out}")