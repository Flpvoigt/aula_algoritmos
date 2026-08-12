from algoritmos_testes.utils import funcoes
import math

def main():
    operadores = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: math.pow(x, y)
    }
    while True:

        try:
            valor_1 = float(input("Digite o primeiro valor: "))
            valor_2 = float(input("Digite o segundo valor: "))
            operador = input("Digite o operador (+, -, *, /, **, sqrt): ").lower()
        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")
            continue

        funcao_escolhida = operadores.get(operador, lambda x, y: None)

        if operador == 'sqrt':
            resultado = funcoes.raiz(valor_1,valor_2)
            print(f"O resultado da operação {operador}({valor_1}, {valor_2}) é: {resultado}")
        elif operador == '/':
            resultado = funcoes.divisao(valor_1, valor_2)
            print(f"O resultado da operação {valor_1} {operador} {valor_2} é: {resultado}") #mudar para todos os tipos de divisao

        else:
            resultado = funcao_escolhida(valor_1, valor_2)
            print(f"O resultado da operação {valor_1} {operador} {valor_2} é: {resultado}")

if __name__ == "__main__":
    main()  