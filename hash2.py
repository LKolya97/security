m2 = 419
n = int(input())
def hash2(a):
    h=0
    b = str(abs(a))
    for i in range(len(b)):
        h=h*m2+int(b[i])
    return h
print(hash2(n))