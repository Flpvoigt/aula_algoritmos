from algoritmos_testes.utils.functions import calculos_bimestrais
def main():

    while True:
        try:
            valor1= float(input("Insira a primeira nota: "))
            valor2= float(input("Insira a primeira nota: "))
        except(ValueError):
            print("Insira um valor valido")
            continue

        resposta = calculos_bimestrais(valor1, valor2)
        print(resposta)

        
        if input("Deseja tentar novamente? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()