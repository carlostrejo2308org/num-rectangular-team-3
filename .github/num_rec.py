
def periocidad(arreglo,m):
    # m = maximo
    for i in  range (1,len(arreglo)):
        semilla = arreglo[0]

        if semilla == arreglo[i]:
            print("Periocidad ",i)
            break
                  


def main():
    arreglo = [2, 3, 4, 9, 10, 16, 2, 3, 4]
    m = 6
    fun = periocidad(arreglo,m)


if __name__ == "__main__":
    main() 