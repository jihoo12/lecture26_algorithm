arr = ["A",["B",["D"]],["C",["E"],["F",["G"]]]]
def preorder(arr):
    temp = []
    for i in arr:
        if type(i) == list:
            temp.append(i)
        else:
            print(i,end="")
    if temp:
        for j in temp:
            preorder(j)

def postorder(arr):
    temp = []
    for i in arr:
        if type(i) != list:
            temp.append(i)
        else:
            postorder(i)
    if temp:
        for j in temp:
            print(j,end="")

def inorder(arr):
    temp = []
    count = 0
    temp2=[]
    for i in arr:
        if type(i) != list:
            temp.append(i)
        else:
            if count == 0:
                inorder(i)
            else:
                temp2.append(i)
            count +=1
    if temp:
        temp.reverse()
        for j in temp:
            print(j,end="")
    if temp2:
        for k in temp2:
            if len(k) <= 2:
                preorder(k)
            else:
                inorder(k)
preorder(arr)
print()
inorder(arr)
print()
postorder(arr)
print()