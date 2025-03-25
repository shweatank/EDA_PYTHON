def print_truth_table():
    print("Truth Table for AND Gate:")
    print("A B | AND")
    print("------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"{a} {b} | {a & b}")

    print("\nTruth Table for OR Gate:")
    print("A B | OR")
    print("-----------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"{a} {b} | {a | b}")

    print("\nTruth Table for NOT Gate:")
    print("A | NOT")
    print("-------")
    for a in [0, 1]:
       print(f"{a} | {1 - a}")

print_truth_table()
