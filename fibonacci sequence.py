def f(n):
    fs=[0,1]
    for i in range(2,n):
        t=fs[i-1]+fs[i-2]
        fs.append(t)
    return fs

n=int(input("no of terms in fs:"))
x=f(n)
print("febinous Series:")
print(x)








