print("a  | b  | sum  | carry_out ")
for a in [0,1]:
    for b in[0,1]:
        summation=a^b
        carry_out=a&b
        print(f"{a}  | {b}  | {summation}  | {carry_out} ")
