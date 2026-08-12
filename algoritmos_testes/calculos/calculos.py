from algoritmos_testes.utils import funcoes

def main():
    while True:

        try:
            valor_1 = float(input("Digite o primeiro valor: "))
            valor_2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")
            continue

        operador = input("Digite o operador (+, -, *, /, **, sqrt): ").lower()

        if operador not in ['+', '-', '*', '/', '**', 'sqrt']:
            print("Erro: Operador inválido. Por favor, escolha entre +, -, *, /, ** ou sqrt.")
            continue
        
        if operador == 'sqrt':
            resultado = funcoes.raiz(valor_1,valor_2)
            print(f"O resultado da operação {operador}({valor_1}, {valor_2}) é: {resultado}")
        elif operador == '+':
            resultado = funcoes.soma(valor_1, valor_2)
            print(f"O resultado da operação {valor_1} {operador} {valor_2} é: {resultado}")
        elif operador == '-':
            resultado = funcoes.subtracao(valor_1, valor_2)
            print(f"O resultado da operação {valor_1} {operador} {valor_2} é: {resultado}")
        elif operador == '*':
            resultado = funcoes.multiplicacao(valor_1, valor_2)
            print(f"O resultado da operação {valor_1} {operador} {valor_2} é: {resultado}")
        elif operador == '/':
            resultado = funcoes.divisao(valor_1, valor_2)
            print(f"O resultado da operação {valor_1} {operador} {valor_2} é: {resultado}") #mudar para todos os tipos de divisao
        elif operador == '**':
            resultado = funcoes.potencia(valor_1, valor_2)
            print(f"O resultado da operação {valor_1} {operador} {valor_2} é: {resultado}")

if __name__ == "__main__":
    main()  