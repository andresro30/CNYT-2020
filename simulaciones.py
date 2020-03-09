from calculadora import *

def canicasBooleanas(estado,canicas,clicks):
    for i in range(clicks):
        estado = productoVectorMatrizReal(estado,canicas)
    return estado

def rendijaProbabilistica(rendijas,objetivo,inicial,estado):
    if(len(inicial)!=objetivo or len(inicial[0])!=objetivo):
        return "La matriz de probabilidades debe ser proporcional a los objetivos"
    else:
        for i in range(rendijas):
            inicial = productoMatricesReales(inicial,inicial)
        return productoVectorMatrizReal(estado,inicial)

def rendijaProbabilistica(rendijas,objetivo,inicial,estado):
    if(len(inicial)!=objetivo or len(inicial[0])!=objetivo):
        return "La matriz de probabilidades debe ser proporcional a los objetivos"
    else:
        for i in range(rendijas):
            inicial = productoMatrices(inicial,inicial)
        return productoVectorMatrizReal(estado,inicial)
    
def main():
    est1 = [6,2,1,5,3,10]
    mat1 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
    #print(canicasBooleanas(est1,mat1,1))

    unmedio = 1/2
    untercio = 1/3
    mat = [[0,0,0,0,0,0,0,0],[unmedio,0,0,0,0,0,0,0],[unmedio,0,0,0,0,0,0,0],
           [0,untercio,0,1,0,0,0,0],[0,untercio,0,0,1,0,0,0],
           [0,untercio,untercio,0,0,1,0,0],[0,0,untercio,0,0,0,1,0],
           [0,0,untercio,0,0,0,0,1]]
    print(rendijaProbabilistica(2,8,mat,[1,0,0,0,0,0,0,0]))

    

main()
