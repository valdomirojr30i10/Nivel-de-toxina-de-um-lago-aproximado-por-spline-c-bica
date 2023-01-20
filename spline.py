import numpy as np
import eliminacao_gaussiana as EG
# Função criada com a finalidade de se encontrar os coeficientes a,b,c e d de
# uma spline cubica. Tendo cada função spline o formato a*x**3+b*x**2+c*x+d
def encontra_coef_S3(x,y):
    n = len(x)
    h = np.zeros(n-1)
    # Definindo os passos 'h' da spline cubica (distancia entre as coordenadas
    # 'x' de cada ponto):
    for i in range(n-1):
        h[i] = x[i+1]-x[i]
    
    # Obtendo os coeficientes b[n] da spline cubica:
    A = np.zeros((n,n))
    B = np.zeros(n)
    A[0,0] = 1
    A[-1,-1] = 1
    for i in range(1,n-1):
        A[i,i] = 2*(h[i-1]+h[i])    
        A[i,i-1] = h[i-1]
        A[i,i+1] = h[i]
        B[i] = 3*(((y[i+1]-y[i])/h[i]) - ((y[i]-y[i-1])/h[i-1])) 
    
    b = EG.elim_gaussiana(A, B)
    
    # Obtendo os coeficientes a[n] e c[n] da spline cubica:
    n-=1
    a = np.zeros(n)
    c = np.zeros(n)

    for i in range(n):
        a[i] = (b[i+1]-b[i])/(3*h[i])
        c[i] = ((y[i+1]-y[i])/h[i]) - ((h[i]/3)*(2*b[i]+b[i+1]))
    d = y
    return a,b,c,d

x = np.array([0, 0.5, 1, 1.5, 2],dtype = np.float32)
y = np.array([3.4422, 2.2302, -0.8228, -4.6133, -9.0841], dtype=np.float32)

x1 = np.array([1,2,4,5], dtype=np.float32)
y1 = np.array([1,4,2,3], dtype=np.float32)
def uma_spline(a,b,c,d,i,x):
    return lambda t: a[i]*((t-x[i])**3) + b[i]*((t-x[i])**2) + c[i]*(t-x[i]) + d[i]

# encontra_coef_S3(x, y)
# Função responsavel por gerar um vetor de pequenas funções que contenham 
# as splines cubicas, que devem ser utilizadas de forma que respeite os 
# intervalos corretos
def gera_S3(x,y):
    # Cria uma lista de funções splines
    S = []
    # obtem os vetores com coeficientes das splines cubicas
    a,b,c,d = encontra_coef_S3(x, y)
    # A quantidade de splines possiveis dependerá de quantos intervalos podem
    # ser formados, e este valor sera: (numero_de_pontos - 1)
    for i in range(len(x)-1):
        # print("Funcao gerada: {}x3 + {}x2 + {}x + {}".format(a[i],b[i],c[i],d[i]))
        S.append(uma_spline(a, b, c, d, i, x))
   
    return S

# S = gera_S3(x1, y1)
# print(S[0](2))
