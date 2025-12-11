import numpy as np

def get_x1(matriz, soluciones, x1):
    if np.linalg.det(matriz) == 0:
        print("El determinante es 0, por lo que no tiene inversa.")
    total = [0] * len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[:])):
            if i == j:
                continue
            total[i] += matriz[i][j] * x1[j]
        total[i] = (1 / matriz[i][i]) * (soluciones[i] - total[i])
    return total

def error(tol,xi,xf):
    validar = [False]*len(xi)
    for i in range(len(xi)):
        if abs(xi[i] - xf[i]) <= tol:
            validar[i] = True   
    return validar


"""
matriz = [[2.33, -1.4271], [13.1582, 12.21], ]
sol = [-33.4752, 142.0952]
xi = [1, 1]
tol = .01


xf = get_x1(matriz, sol, xi)
tabla = error(tol,xi,xf)
ite = 1
"""
if __name__ == '__main__':
    n = int(input("Ingresa el tamanio de la matriz: "))
    matriz = [[0 for _ in range(n)]for _ in range(n)]
    sol = []
    xi = [] 
    for a in range(n):
        for b in range(n):
            matriz[a][b] = float(input(f"Ingresa el valor del coeficiente a{a+1}{b+1} de la matriz: "))
        sol.append(float(input(f"Ingresa el valor de b{a+1} :")))
        xi.append(float(input(f"Ingresa el valor de x{a+1} inicial: ")))
    tol = float(input("Ingresa el valor de la tolerancia: "))
    ite = 1
    xf = get_x1(matriz,sol,xi)

    tabla = error(tol,xi,xf)


    for j in range(n):
        print(f"El valor de x{j} en la iteracion {ite} es de: {xf[j]}")
    print("\n\n\n")

    while (False in tabla):
        ite += 1
        xi = xf 
        xf = get_x1(matriz,sol,xi)
        tabla = error(tol,xi,xf)

    for j in range(n):
        print(f"El valor de x{j} en la iteracion {ite} es de: {xf[j]}")