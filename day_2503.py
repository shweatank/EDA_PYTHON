mat=[[0,0],[0,1],[1,0],[1,1]]
def comp(num):
    if num==0:
        # print('1')
        return 1
    else:
        # print('0')
        return 0

def func_and(mat):
    lst=[]
    for item in mat:
        a, b = item[0], item[1]
        output = a & b
        lst.append(output)
    return lst

def func_or(mat):
    lst=[]
    for item in mat:
        a, b = item[0], item[1]
        output = a | b

        lst.append(output)
    print(lst)
    return lst

func_or(mat)
print('_'*10)
func_and(mat)
print('-'*10)
num=0
comp(num)



