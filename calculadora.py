from sys import stdin
import math
import unittest


def suma(a,b):
    v1 = a[0]+b[0]
    v2 = a[1]+b[1]
    return (v1,v2)
    
def resta(a,b):
    v1 = a[0]-b[0]
    v2 = a[1]-b[1]
    return (v1,v2)

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
                
    v1 = ent[0]+ent[1]
    v2 = ima[0]+ima[1]
    return (v1,v2)

def division(a,b):
    z1 = a[0]*b[0] + a[1]*b[1]
    z2 = a[1]*b[0] - a[0]*b[1]
    z3 = b[0]**2 + b[1]**2

    v1 = z1/z3
    v2 = z2/z3
    return (v1,v2)

def modulo(a):
    temp = a[0]**2 + a[1]**2
    v1 = temp**(1/2)
    return (v1,"")

def conjugado(a):
    v1 = a[1]*-1    
    return (a[0],v1)

def polarCartesiano(a):
    #Los angulos estan en grados
    r = a[0]
    ang = radGrados(a[1])
    v1 = r*(math.cos(ang))
    v2 = r*(math.sin(ang))
    return (v1,v2)

def cartesianoPolar(a):
    v1 = (a[0]**2 + a[1]**2)**(1/2)
    v2 = gradRadi(math.atan(a[1]/abs(a[0])))
    return(v1,v2)

def fase(a):
    v1 = math.atan2(a[1],a[0])
    return (v1,"")
    
def prettyPrinting(c):
    if(c[1]==""):
        print(round(c[0],2))
    else:
        if(c[0]!=0):
            print(round(c[0],2),end="")
            if(c[1]>=0):
                print(" +",str(round(c[1],2))+"i")
            else:
                print("",str(round(c[1],2))+"i")
        else:
            if(c[1]==1):
                print("i")
            else:
                print(round(c[1],2)+"i")

def radGrados(num):
    return (num/180)*math.pi

def gradRadi(num):
    return (num*180)/math.pi

def main():
    op = polarCartesiano((13,23))
    prettyPrinting(fase((3,21)))
    prettyPrinting(fase((6,-76)))
    prettyPrinting(fase((5,16)))

main()
