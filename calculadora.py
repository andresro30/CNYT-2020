from sys import stdin

a = [3,5]
b = [-6,-4]
ans = [0,0]

def suma(a,b):
    ans[0] = a[0]+b[0]
    ans[1] = a[1]+b[1]
    
def resta(a,b):
    ans[0] = a[0]-b[0]
    ans[1] = a[1]-b[1]



def multiplicacion(a,b):
    ent = []
    ima = []
    for i in range(len(a)):
        for j in range(len(b)):    
            if(i==0 and j==0):
                ent.append(a[i]*b[j])
            elif(i==0 and j==1):
                ima.append(a[i]*b[j])
            elif(i==1 and j==0):
                ima.append(a[i]*b[j])
            else:
                ent.append(-1*(a[i]*b[j]))

    print(ent,ima)
    ans[0]=ent[0]+ent[1]
    ans[1]=ima[0]+ima[1]

def division(a,b):
    z1 = a[1]**2 + b[1]**2
    z2 = a[0]*a[1] + b[0]*b[1]
    z3 = a[1]*b[0] - a[0]*b[1]

    ans[0] = z2/z1
    ans[1] = z3/z1
    print(ans)


def modulo(a):
    temp = a[0]**2 + a[1]**2
    ans[0] = temp**(1/2)

def prettyPrinting(c):
    if(c[1]==0):
        print(c[0])
    elif(c[0]!=0):
        print(c[0],end="")
        if(c[1]>=0):
            print(" +",str(c[1])+"i")
        else:
            print("",str(c[1])+"i")

    else:
        if(c[1]==1):
            print("i")
        else:
            print(str(c[1])+"i")

def main():
    #suma(a,b)
    #multiplicacion(a,b)
    #division(a,b)
    modulo(a)
    prettyPrinting(ans)
main()
