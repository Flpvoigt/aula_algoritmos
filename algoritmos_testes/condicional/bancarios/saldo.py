from algoritmos_testes.utils.functions import saldo_conta_bancaria

def main():
    while True:
        try:
            saldo = float(input("Digite o limite de sua conta: R$ "))
            salario = float(input("Digite o valor do salário: R$ "))
            retirada = float(input("Digite o valor da retirada: R$ "))
        except(ValueError):
            print("insira apenas valores válidos")
            continue

        resultado = saldo_conta_bancaria(saldo, salario, retirada)
        print(resultado)

        if input("Deseja calcular mais algum saldo (s/n): ") != "s":
            break

if __name__ == "__main__":
    main()