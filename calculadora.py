from sys import stdin
import math
import unittest


""" Números complejos """

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


""" Operaciones con Vectores y Matrices complejas"""

def verificarTipo(a,b):
    if(type(a)==tuple):
        return (a,b)
    else:
        return (b,a)


def sumaVectores(a,b):
    ans = [0]*len(a)
    if(len(a)!=len(b)):
        return "Las dimensiones de los vectores no son iguales"
    else:
        for i in range(len(a)):
            ans[i] = suma(a[i],b[i])
        return ans

def inversaVector(a):
    ans = [0]*len(a)
    for i in range(len(a)):
        ans[i] = (-1*(a[i][0]),-1*(a[i][1]))
    return ans

def multiplicacionVectores(a,b):
    c = verificarTipo(a,b)[0]
    v = verificarTipo(a,b)[1]
    ans = [0]*len(v)
    for i in range(len(v)):
        ans[i] = multiplicacion(c,v[i])
    return ans

def sumaMatrices(a,b):
    ans = [0]*len(a)
    if(len(a)!=len(b)):
        return "Las dimensiones de los vectores no son iguales"
    else:
        for i in range(len(a)):
            if(len(a[i])!=len(b[i])):
               return "Las dimensiones de los vectores no son iguales"
            else:
                ans[i] = sumaVectores(a[i],b[i])
        return ans

def inversaMatriz(a):
    ans = [0]*len(a)
    for i in range(len(a)):
        ans[i] = inversaVector(a[i])
    return ans

def multiplicacionMatrices(a,b):
    c = verificarTipo(a,b)[0]
    m = verificarTipo(a,b)[1]
    ans = [0]*len(a)    
    for i in range(len(m)):
        ans[i] = multiplicacionVectores(c,m[i])
    return ans

def traspuesta(a):
    ans = [[0]*len(a[0])]*len(a)
    print(ans)
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(i,j)
            ans[i][j] = a[j][i]
    return ans

def conjugadoMatriz(a):
    ans = [[0]*len(a[0])]*len(a)
    print(ans)
    for i in range(len(a)):
        for j in range(len(a[i])):
            ans[i][j] = conjugado(a[i][j])
    return ans
 
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
                print(str(round(c[1],2))+"i")

def radGrados(num):
    return (num/180)*math.pi

def gradRadi(num):
    return (num*180)/math.pi

def main():
    #op = sumaVectores([(1,2),(1,2),(3,5)],[(-2,2),(2,2),(4,10)])
    #op = multiplicacionVectores([(1,2),(3,4),(1,5)],(0,0))
    #op = multiplicacionVectores((1,1),[(1,2),(3,4),(1,5)])
    #op = sumaMatrices([[(1,1),(2,-3)],[(4,2),(2,4)]],[[(1,0),(1,0)],[(1,0),(1,0)]])
    #op = inversaMatriz([[(1,1),(2,-3)],[(4,2),(2,4)]])
    #op = multiplicacionMatrices([[(1,1),(2,-3)],[(4,2),(2,4)]],(1,1))
    #op = traspuesta([[(1,1),(2,-3)],[(4,2),(2,4)]])
    #op = conjugadoMatriz([[(1,2),(2,1)],[(1,-2),(2,-3)],[(3,4),(3,-1)]])
    op = conjugadoMatriz([[(1,1),(2,2)],[(1,1),(2,2)]])
    print(op)
    prettyPrinting(op)

main()
