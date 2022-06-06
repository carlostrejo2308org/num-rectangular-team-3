def periocidad(arreglo=[],m=int):
    semilla = arreglo[0]
    completo=[]
    for i in  range (1,len(arreglo)):

        if semilla == arreglo[i]:
            print("Periocidad ",i+1) 
            if m < arreglo[i-1]:#Si m es menor al número anterior en donde termino la semilla 
                                #daremos por hecho que está incompleta.
                    x = range(arreglo[i-1]+1) #Con range obtendremos todos los numeros 
                    completo=[list(x)]#Para pasar el range a un arreglo, lo pasamos a una lista.
            print(completo)
            break
        
                  


def main():
    arreglo = [2, 3, 4, 9, 10, 16, 2, 3, 4]
    m = 6
    fun = periocidad(arreglo,m)
    

if __name__ == "__main__":
    main() 