A=[]
n=int(input("Dati un numar intre 2 si 10:"))
if n>=2 and n<=10:
    m=n
else:
    print("lungimea nu corespunde cu cea ceruta")

for i in range(0,m):
    x=[]
    for j in range(0,m):
        j=int(input("Dati un numar:"))
        x.append(j)
    A.append(x)
print(A)
d_principala=[]
d_secundara=[]
d_prin_sus=[]
d_prin_jos=[]
d_sec_sus=[]
d_sec_jos=[]
for i in range(len(A)):
    for j in range(len(A[0])):
        if i==j:
            d_principala.append(A[i][j])
        if i+j==(len(A)-1):
            d_secundara.append(A[j][i])
for i in range(len(A)):
    for j in range(len(A[0])):
        if i>j:
            d_prin_jos.append(A[i][j])
        if i<j:
            d_prin_sus.append(A[i][j])
        if i+j<(len(A)-1):
            d_sec_sus.append(A[i][j])
        if i+j>(len(A)-1):
            d_sec_jos.append(A[i][j])
print("Suma pe diagonala principala este:",sum(d_principala))
print("Suma pe diagonala secundara este:",sum(d_secundara))
print("Suma de sus a diagonalei princiale este:",sum(d_prin_sus))
print("Suma de jos a diagonalei princiale este:",sum(d_prin_jos))
print("Suma de sus a diagonalei secundare este:",sum(d_sec_sus))
print("Suma de jos a diagonalei secundare este:",sum(d_sec_jos))