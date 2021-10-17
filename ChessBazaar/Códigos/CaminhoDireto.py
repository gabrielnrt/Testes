from pylab import plot, show, scatter, legend, grid, xlabel, ylabel
from numpy import linspace

gama = 0.6
valor = 50

def menor(x,y):
    if x<y:
        r = x
    else:
        r = y
    return r

def x2(x):
    X = 200
    mi = 0.4 #CUPOM DE DESCONTO DO CHESSBAZAAR
    
    if x>=X:
        retorno = (1-mi)*x
    else:
        retorno = x
        
    return retorno

def x3(x):
    if x>valor:
        retorno = (1+gama)*x
    else:
        retorno = x

    return retorno

p = [60, 49, 92.8, 49, 139, 278.39]
# p[0] é o preço do reykjavik
# p[1] é o preço do single staunton
# p[2] é o preço do desert gold
# p[3] é o preço do german knight
# p[4] é o preço do dubrovnik
# p[5] é o preço do sinquefield

CarrinhosPossiveis1 = [] # esse vai ser o eixo x da uscloser
TotalPelaUSCloser = []
CarrinhosPossiveis2 = [] # esse vai ser o eixo x da receita federal
TotalSemUSCloser = []
frete = 40

nReykjavik = [0, 1, 2, 3]
nSingleStaunton = [0, 1]  # NA VDD O SITE PERMITE COMPRAR ATÉ 3, MAS COMO O MODELO É FEIO,  ME LIMITO A  UMA QUANTIDADE.
nDesertGold = [0, 1, 2, 3, 4, 5]
nGermanKnight = [0, 1, 2]
nDubrovnik = [0, 1, 2, 3]
nSinquefield = [0, 1, 2, 3]

for i in nReykjavik:
    for j in nSingleStaunton:
        for k in nDesertGold:
            for l in nGermanKnight:
                for m in nDubrovnik:
                    for n in nSinquefield:
                        
                        carrinho = i*p[0] + j*p[1] + k*p[2] + l*p[3] + m*p[4] + n*p[5]
    
                        FreteTotal = frete*(i+j+k+l+m+n)
                    
                        a = FreteTotal + x2(carrinho) #Preço pela USCloser
                        b = x3(x2(carrinho))          #Preço indo pela Receita Federal

                        if menor(a,b)<=carrinho and carrinho>=0 and carrinho<=300:
                            if menor(a,b)==a:
                                CarrinhosPossiveis1.append(carrinho)
                                TotalPelaUSCloser.append(a)
                                
                                print("Carrinho USCloser:")
                                if i>0:
                                    print(i,"Reykjavik")
                                if j>0:
                                    print(j,"Single Satunton")
                                if k>0:
                                    print(k, "Desert Gold")
                                if l>0:
                                    print(l, "GermanKnight")
                                if m>0:
                                    print(m,"Dubrovnik")
                                if n>0:
                                    print(n,"Sinquefield")
                                print("Total Gasto (USD):", a, ", incluindo frete de", FreteTotal, "\n")
                                    
                            else:
                                CarrinhosPossiveis2.append(carrinho)
                                TotalSemUSCloser.append(b)
                                '''
                                print("Carrinho da Receita:")
                                if i>0:
                                    print(i,"Reykjavik")
                                if j>0:
                                    print(j,"Single Satunton")
                                if k>0:
                                    print(k, "Desert Gold")
                                if l>0:
                                    print(l, "GermanKnight")
                                if m>0:
                                    print(m,"Dubrovnik")
                                if n>0:
                                    print(n,"Sinquefield")
                                print("Total Gasto (USD):", b, ", onde o imposto foi de",b-x2(carrinho),"\n")
                                '''

                            # NA PRÁTICA, NA MAIORIA DOS CASOS É MAIS BARATO IMPORTAR DIRETO, E MESMO COM O IMPOSTO, TEMOS DESCONTO REAL PRÓXIMO DE 4%
                            # QUANDO SE COMPRA POUCOS MODELOS E ESTES SÃO MAIS CAROS (SINQUEFIELD E DUBROVNIK), COMPENSA USAR A USCLOSER

scatter(CarrinhosPossiveis1,TotalPelaUSCloser, label = "Total usando a USCloser")
scatter(CarrinhosPossiveis2,TotalSemUSCloser, label = "Total com a Receita Federal")

legend()
grid(True)
xlabel("Total no Carrinho (USD)")
ylabel("Total gasto (USD)")
show()

