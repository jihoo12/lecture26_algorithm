import sys

def make_tree():
    first_line = sys.stdin.readline().strip()
    if not first_line:
        return []
    
    n = int(first_line)
    tree_data = {}
    root = None
    
    for i in range(1, n + 1):
        line = sys.stdin.readline().strip()
        if not line:
            break
        
        parent, left, right = line.split()
        
        if i == 1:
            root = parent
            
        left_child = None if left == '.' else left
        right_child = None if right == '.' else right
        
        tree_data[parent] = [left_child, right_child]

    def build_nested_list(node):
        if node is None or node not in tree_data:
            return None
        
        left_child = tree_data[node][0]
        right_child = tree_data[node][1]
        
        result = [node]
        
        left_list = build_nested_list(left_child)
        if left_list is not None:
            result.append(left_list)
            
        right_list = build_nested_list(right_child)
        if right_list is not None:
            result.append(right_list)
            
        return result

    return build_nested_list(root)
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

arr = make_tree() 
preorder(arr)
print()
inorder(arr)
print()
postorder(arr)
print()