def main():
    listaA = ["Manzana", "Pera", "Melocotón"]
    listaB = ["Kiwi", "Sandía", "Melón"] 
    listaA.extend(listaB)
    print(listaA[-1])

    tupla = (3,5,7)
    print(tupla[0])

    inicio = int(input("Inicio: "))
    final = int(input("Final: "))
    salto = int(input("Rango: "))

    rango = range(inicio,final,salto)
    print(rango)

    
if __name__ == "__main__":
    main()

