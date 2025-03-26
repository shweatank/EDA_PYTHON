
a=[0,0,1,1]
b=[0,1,0,1]
# x=[]
# y=[]
# z=[]
# for i in range(len(a)):
#     x.append(nega(a[i]&b[i]))
#     y.append(nega(a[i] & b[i]))
#     z.append(nega(x[i] or y[i]))

def nega(a):
   return 1 if a == 0 else 0

def and_gate(x, y):

    result = []
    for i in range(len(x)):
        result.append(x[i] & y[i])
    return result

def or_gate(x, y):
    result = []
    for i in range(len(x)):
        result.append(x[i] | y[i])
    return result

def not_gate(x):
    result = []
    for i in range(len(x)):
        result.append(nega(x[i]))
    return result


or_g = or_gate(a, b)
and_g = and_gate(a, b)
not_g = not_gate(a)


print("a b OR")
for i in range(4):
    print(a[i], b[i], or_g[i])

print("-----------")

print("a b AND")
for i in range(4):
    print(a[i], b[i], and_g[i])

print("-----------")

print("a NOT")
for i in range(4):
    print(a[i], not_g[i])
