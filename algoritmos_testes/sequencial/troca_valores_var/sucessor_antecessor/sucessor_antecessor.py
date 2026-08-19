from algoritmos_testes.utils.funcoes import mostrar_antecessor_sucessor

def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Erro: Por favor, insira apenas números inteiros válidos.")
            continue

        print(mostrar_antecessor_sucessor(numero))

        if input("Deseja verificar outro número? (s/n): ").lower() == 's':
            continue
        else:
            print("Encerrando o programa de antecessor e sucessor.")
            break

if __name__ == "__main__":
    main()