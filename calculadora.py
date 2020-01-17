from sys import stdin
import math
import unittest

a = [3,-5]
b = [-6,-4]
ans = [0,0]

def rad_grados(num):
    return (180.0/math.pi)*num

def suma(a,b):
    ans=[0,0]
    ans[0] = a[0]+b[0]
    ans[1] = a[1]+b[1]
    return ans
    
def resta(a,b):
    ans=[0,0]
    ans[0] = a[0]-b[0]
    ans[1] = a[1]-b[1]
    return ans


def multiplicacion(a,b):
    ent = []
    ima = []
    ans=[0,0]
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

    #print(ent,ima)
    ans[0]=ent[0]+ent[1]
    ans[1]=ima[0]+ima[1]
    return ans

def division(a,b):
    ans=[0,0]
    z1 = a[0]*b[0] + a[1]*b[1]
    z2 = a[1]*b[0] - a[0]*b[1]
    z3 = b[0]**2 + b[1]**2

    ans[0] = z1/z3
    ans[1] = z2/z3
    return ans

def modulo(a):
    ans=[0,0]
    temp = a[0]**2 + a[1]**2
    ans[0] = temp**(1/2)
    return ans

def conjugado(a):
    ans=[0,0]
    ans[0] = a[0]
    ans[1] = a[1]*-1    
    return ans

def polarCartesiano(a):
    #Los angulos estan en radianes
    ans=[0,0]
    r = a[0]
    ang = a[1]
    ans[0] = r*(math.cos(ang))
    ans[1] = r*(math.sin(ang))
    return ans

def cartesianoPolar(a):
    ans=[0,0]
    ans[0] = (a[0]**2 + a[1]**2)**(1/2)
    ans[1] = math.atan(a[1]/a[0])
    return ans

def fase(a):
    ans=[0,0]
    ans[0] = math.atan2(a[1],a[0])
    return ans
    
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
    op = polarCartesiano([13,23])
    prettyPrinting(op)

main()
