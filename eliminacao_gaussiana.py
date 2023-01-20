import numpy as np
# Funcao que efetua o pivoteamento de uma matriz 'A', conforme a matriz solucao
# 'b' dada. Retorna as matrizes 'A' e 'b', sendo 'A' uma matriz triangular supe
# rior e 'b' a matriz solucao de 'A'.
def eliminacao_gaussiana(A,b):
    m,n = A.shape
    assert(m == n), "Matriz 'A' não é quadrada"

    for k in range(n):
        if ((k-1) != n):
            for i in range(k+1,n):
                m = (A[i,k]/A[k,k])
                A[i,k] = 0.0
                
                b[i] -= m*b[k]
                for j in range(k+1,n):
                    A[i,j] -= m*A[k,j]
    return A,b

# Dado um sistema linear, do qual 'A' seja uma matriz triangular superior, 
# efetua a substituicao regressiva de forma a se obter a resposta para
# o sistema linear 
def substituicao_regressiva(A,b):
    m,n = A.shape
    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1,n-1]
    for i in range(n-1,-1,-1):
        s = 0.0
        for j in range(i+1,n):
            s += (A[i,j]*x[j])
            
        x[i] = ((b[i]-s)/A[i,i])
    return x       
def elim_gaussiana(A,b):
    A,b = eliminacao_gaussiana(A,b)
    EG = substituicao_regressiva(A,b)
    return EG
