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

def rendijaCuantica(rendijas,objetivo,inicial,estado):
    if(len(inicial)!=objetivo or len(inicial[0])!=objetivo):
        return "La matriz de probabilidades debe ser proporcional a los objetivos"
    else:
        for i in range(rendijas):
            inicial = productoMatrices(inicial,inicial)
        return productoVectorMatriz(estado,inicial)

"""  
def main():
    
main()
"""
