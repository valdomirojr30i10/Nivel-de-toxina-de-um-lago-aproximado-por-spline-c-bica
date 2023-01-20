import spline
import numpy as np
from matplotlib import pyplot as plt

# Dados necessarios para o trabalho
Ano = np.array([2006,2008,2010,2012,2014,2016,2018,2020], dtype = np.float64)
Concentracao = np.array([12.0,12.7,13.0,15.2,18.2,19.8,24.1,28.1],dtype = np.float64)

# Dados sem informacoes de 2010 e 2012
Ano_ = np.array([2006,2008,2014,2016,2018,2020], dtype = np.float64)
Concentracao_ = np.array([12.0,12.7,18.2,19.8,24.1,28.1],dtype = np.float64)

# 1.1. Faça a uma interpolação com Spline Cúbica com condições de contorno
# livres.
def interpolacao(Ano,Concentracao):
    S = spline.gera_S3(Ano, Concentracao)
    return S

# 1.2. Use a interpolação para prever o valor da concentração da toxina em
# 2022.
def prever(S,intervalo,ano):
    return (S[intervalo](ano))

# 1.3. Faça um grafico do problema:
def plot_spline(S,x,y):
    # plt.axis([2004,2025,10,35])  
    plt.grid()
    for i in range(len(S)):
        f = S[i]
        X = np.linspace(x[i],x[i+1],200)
        Y = [f(k) for k in X]
        plt.plot(X,Y, color='green')    
    for i in range(len(S)+1):
        # Dados originais serao pontos marcados com a cor azul
        plt.plot(x[i],y[i], 'o', color='blue')
    
# Função que plota a localização da previsão como um ponto vermelho, e traça 
# uma curva do ultimo dado original ate a previsao
def plot_previsao(ano,previsao,f,x):
    plt.plot(ano, previsao, 'o', color='red') 
    X = np.linspace(x[-1],ano,200)
    Y = [f(k) for k in X]
    plt.plot(X,Y,color = 'purple')   
    plt.show()
    

# Função que efetua chamada das demais funções
def main(Ano,Concentracao):    
    S = interpolacao(Ano, Concentracao)
    previsao = prever(S,-1,2022)
    plot_spline(S, Ano,Concentracao)
    print("Previsao para o ano de 2022:", previsao)
    plot_previsao(2022, previsao,S[-1],Ano)


# Interpolação de Spline sem usar os dados originais de 2010 e 2012
def plot_suspeita(A1,A2,C1,C2,plot_intersecao = True):
    # S1 = interpolacao(A1, C1)
    S2 = interpolacao(A2, C2)
    previsao = prever(S2,-1,2022)
    plot_spline(S2, A2, C2)
    # plot_spline(S,A1,C1) '''descomente para plotar'''
    
    print("\n\n\nPrevisao para o ano de 2022 sem dados de 2010 e 2012:", previsao)
    plot_previsao(2022, previsao,S2[-1],A2)
    previsao = prever(S2,1,2010)
    print("\n\nPrevisao para 2010: {:.3f}, Valor original: {:.3f}".format(previsao,C1[2]))
    previsao = prever(S2,1,2012)
    print("Previsao para 2012: {:.3f}, Valor original: {:.3f}".format(previsao,C1[3]))
   
    
    
main(Ano, Concentracao)
plot_suspeita(Ano, Ano_, Concentracao, Concentracao_)