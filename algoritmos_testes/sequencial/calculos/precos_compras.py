from algoritmos_testes.utils.functions import valor_lucro_venda 

def main():
    while True:
        try:
            valor_compra = float(input("Digite o valor de compra: "))
            valor_venda = float(input("Digite o percentual de lucro (%): "))
        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")
            continue

        resultado = valor_lucro_venda(valor_compra, valor_venda)
        print(resultado)

        if input("Deseja calcular outro lucro? (s/n): ").lower() != 's':
            print("Encerrando o programa de cálculo de lucro.")
            break

if __name__ == "__main__":
    main()