l = [
    [1,2,3],[4,5,6],[7,8,9]
]
f =[]
s=[]
def c():
    for i in l:
        for j in i:
            f.append(j*5)
        s.append(f)
        break
print(s)