from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

A = 6.5
AlphaFrente = 19.7
AlphaTraseiro = 15.45

def n(alpha,C): #### n = 1/M
    return alpha*A/C

def grafico(x,y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    Y = intercept + slope*x
    SLOPE = round(slope,2)
    INTERCEPT = round(intercept,2)
    
    plt.figure(figsize=(7,6))
    plt.scatter(x,y, label='Pontos Coletados')
    #plt.scatter(y,x, label='Pontos Coletados')
    plt.plot(x,Y, color='green', label='R.L. Y = A.X + B com A = ' +str(SLOPE)+' e B = '+str(INTERCEPT))
    #plt.plot(Y,x, color='green', label='R.L. Y = A.X + B com A = ' +str(SLOPE)+' e B = '+str(INTERCEPT))
    plt.grid(True)
    #plt.xlabel('$d_0$ (cm)')
    plt.xlabel('1/M')
    #plt.ylabel('1/M')
    plt.ylabel('$d_0$ (cm)')
    plt.legend(loc='lower right')
    plt.show()
    
## CAMERA SELFIE
d0F = np.array([12, 16, 20, 24, 29, 32, 36, 40, 43, 52])
CF  = np.array([4, 2.8, 2.3, 2, 1.9, 1.7, 1.2, 1.1, 0.9, 0.6])
nF = n(AlphaFrente,CF)
grafico(nF,d0F)


## CAMERA TRASEIRA
d0T = np.array([11, 15, 19, 23, 25, 29, 31, 36, 39, 43])
CT = np.array([4.5, 3.2, 2.5, 2, 2.8, 1.7, 1.4, 1.1, 1, 0.9])
nT = n(AlphaTraseiro,CF)
grafico(nT,d0T)