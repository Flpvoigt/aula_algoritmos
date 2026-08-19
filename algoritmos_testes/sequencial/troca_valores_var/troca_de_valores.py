from algoritmos_testes.utils.funcoes import trocar_com_pythonico, trocar_com_auxiliar, identificar_tipo

def main():
    while True:
        try:
            valor_1 = identificar_tipo(input("Digite o primeiro valor: "))
            valor_2 = identificar_tipo(input("Digite o segundo valor: "))
        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")
            continue
        
        print(f"variavel 1: ({valor_1}), variavel 2: ({valor_2})")

        if input("Deseja trocar os valores? (s/n): ").lower() == 's':
            print(trocar_com_pythonico(valor_1, valor_2))

            while input("Deseja trocar os valores novamente? (s/n): ").lower() == 's':
               valor_1, valor_2 =trocar_com_auxiliar(valor_1, valor_2)
               print(f"variavel 1: ({valor_1}), variavel 2: ({valor_2})")
            
            if input("deseja continuar no sistema? (s/n): ").lower() != 's':
                break
        else:
            print("Encerrando o programa de troca de valores.")
            continue

if __name__ == "__main__":
    main()