def periocidad(arreglo,m):
    tempo = 0
    m = m - 1

    for i in arreglo:
        if arreglo.count(i) > 1:            
            tempo = arreglo.index(i,arreglo.index(i)+1)
            break

    if tempo == m:
        return 'Periocidad completa :{}'.format(tempo)

    else :
        arregloDF = []

        for i in range(m+1):
            if i in arreglo:
                pass
            else:                
                arregloDF.append(i)
        return arregloDF, 'Periocidad: {}'.format(tempo)
    
def GenConMix(Xo, limite, a, c, m):
    arrRES = []

    for i in range(limite):
        arrRES.append('')
    arrRES[0] = Xo

    for i in range(limite-1):
        arrRES[i+1] = (a*arrRES[i]+c)%m
    return arrRES


Xo = 15
limite = 25
a = 8
c = 16
m = 100

testGCM = GenConMix(Xo, limite, a, c, m)
testP= periocidad(GenConMix(Xo, limite, a, c, m),m)
print(testGCM)  #testeo de Generador mixto
print(testP)    #testeo de periocidad