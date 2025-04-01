# def nega(a):
#     """NOT Gate - Returns the negation of a single-bit input (0 or 1)."""
#     return 1 if a == 0 else 0
#
# def and_gate(x, y):
#     """AND Gate - Performs bitwise AND operation on two lists."""
#     return [x[i] & y[i] for i in range(len(x))]
#
# def or_gate(x, y):
#     """OR Gate - Performs bitwise OR operation on two lists."""
#     return [x[i] | y[i] for i in range(len(x))]
#
# def not_gate(x):
#     """NOT Gate - Performs bitwise NOT operation on a list."""
#     return [nega(x[i]) for i in range(len(x))]
#
# # Inputs (covering all possible cases)
# a = [0, 0, 1, 1]
# b = [0, 1, 0, 1]
#
# # Total number of test cases
# total_cases = len(a) * 3  # Each input set runs through AND, OR, and NOT gates
# executed_cases = 0
#
# # Function to update and print progress
# def update_progress():
#     global executed_cases
#     executed_cases += 1
#     progress = (executed_cases / total_cases) * 100
#     print(f"Code Coverage: {progress:.2f}% completed")
#
# # Performing logic operations with progress tracking
# print("a b OR")
# or_g = or_gate(a, b)
# for i in range(4):
#     print(a[i], b[i], or_g[i])
#     update_progress()
#
# print("-----------")
#
# print("a b AND")
# and_g = and_gate(a, b)
# for i in range(4):
#     print(a[i], b[i], and_g[i])
#     update_progress()
#
# print("-----------")
#
# print("a NOT")
# not_g = not_gate(a)
# for i in range(4):
#     print(a[i], not_g[i])
#     update_progress()
#
# print("-----------")
# print("Code Coverage: 100% completed ✅")
def nega(a):
    """NOT Gate - Returns the negation of a single-bit input (0 or 1)."""
    return 1 if a == 0 else 0

def and_gate(x, y, z):
    """AND Gate - Performs bitwise AND operation on three inputs."""
    return x & y & z

def or_gate(x, y, z):
    """OR Gate - Performs bitwise OR operation on three inputs."""
    return x | y | z

def not_gate(x):
    """NOT Gate - Performs bitwise NOT operation on a single bit."""
    return nega(x)

# Storing all possible test cases (000 to 111)
possible_cases = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
                  (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)}

total_cases = len(possible_cases)
executed_cases = 0

# Function to update progress
def update_progress():
    global executed_cases
    progress = (executed_cases / total_cases) * 100
    print(f"Code Coverage: {progress:.2f}% completed")

# Function to process a given input
def process_input(a, b, c):
    global executed_cases

    # Check if input is a new test case
    if (a, b, c) in possible_cases:
        possible_cases.remove((a, b, c))
        executed_cases += 1

        # Compute logic outputs
        or_result = or_gate(a, b, c)
        and_result = and_gate(a, b, c)
        not_result = not_gate(a)

        # Print results
        print(f"Input: {a}{b}{c} | OR: {or_result}, AND: {and_result}, NOT(A): {not_result}")
        update_progress()
    else:
        print(f"Input: {a}{b}{c} | Duplicate - Already Tested ❌")

# Sample test cases (run all 8 unique cases + a duplicate)
test_inputs = [
    (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
    (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1),
    (0, 1, 1)  # Duplicate case
]

print("=== Code Coverage Tracker ===")
for t in test_inputs:
    process_input(*t)

print("Code Coverage: 100% completed ✅" if executed_cases == total_cases else "Some cases remain untested!")
