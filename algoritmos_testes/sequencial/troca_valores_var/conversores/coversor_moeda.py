from algoritmos_testes.utils import funcoes

def main():
    while True:
        try:
            valor_real = float(input("Digite o valor em reais (R$): "))
        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")
            continue

        moeda = input("Digite a moeda para conversão (USD, EUR, GBP): ").upper()

        if moeda not in ['USD', 'EUR', 'GBP']:
            print("Erro: Moeda inválida. Por favor, escolha entre USD, EUR ou GBP.")
            continue

        elif moeda == 'USD':
            resultado = funcoes.converter_real_para_dolar(valor_real)
            print(resultado)
        elif moeda == 'EUR':
            resultado = funcoes.converter_real_para_euro(valor_real)
            print(resultado)
        elif moeda == 'GBP':
            resultado = funcoes.converter_real_para_libra(valor_real)
            print(resultado)

        resposta = input("Deseja realizar outra conversão? (s/n): ").lower()
        if resposta != 's':
            break

if __name__ == "__main__":
    main()
