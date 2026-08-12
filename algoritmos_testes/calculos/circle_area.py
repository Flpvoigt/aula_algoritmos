import math
from algoritmos_testes.utils.funcoes import calcular_area_circulo

def main():
    while True:
        try:
            raio = float(input("Digite o raio do círculo: "))
        except ValueError:
            print("Erro: Por favor, insira um número válido para o raio.")
            continue

        resultado = calcular_area_circulo(raio)
        print(resultado)
        
        if raio < 0:
            print("Erro: O raio não pode ser negativo. Por favor, insira um valor positivo.")
            continue

        if input("Deseja tentar novamente? (s/n): ").lower() != 's':
            print("Encerrando o programa.")
            break


if __name__ == "__main__":
    main()