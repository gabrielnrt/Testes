from pylab import plot, show, figure, xlabel, ylabel, legend, grid
from numpy import linspace, sqrt, array

def D(n,d):
    Diametro = 4*d/sqrt((n**2)-1)
    return Diametro

#nvetor = array([1.1, 1.2, 1.3, 1.4, 1.5])
nvetor = array([1.33, 1.50, 1.90, 1.36, 2.42])
d = linspace(0,10,1000)
figure(figsize=(7,6))
for N in nvetor:
    y = D(N,d)
    if N == 1.33:
        plot(d,y, label='$n_1$ = '+str(N)+' (Água)')
    elif N == 1.50:
        plot(d,y, label='$n_1$ = '+str(N)+ ' (Vidro)')
    elif N == 1.90:
        plot(d,y, label='$n_1$ = '+str(N)+ ' (Glicerina)')
    elif N == 1.36:
        plot(d,y, label='$n_1$ = '+str(N)+ ' (Álcool etílico)')
    elif N == 2.42:
        plot(d,y, label='$n_1$ = '+str(N)+' (Diamante)')
    #plot(d,y, label='$n_1$ = '+str(N))
xlabel('Distância (m)')
ylabel('Diâmetro (m)')
legend()
grid(True, linestyle='--')
show()    

#'''
figure(figsize=(7,6))
dvetor = array([0, 1, 2, 3, 4, 5])
n = linspace(1.1,10,1000)
for distancia in dvetor:
    y = D(n,distancia)
    plot(n,y, label='d = '+str(distancia)+' m')
xlabel('$n_1$')
ylabel('Diâmetro (m)')
legend()
grid(True, linestyle='--')
show()
#'''