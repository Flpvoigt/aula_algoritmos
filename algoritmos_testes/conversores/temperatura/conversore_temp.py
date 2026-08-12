from algoritmos_testes.utils.funcoes import converte_para_fahrenheit, converter_para_kelvin

def main():
    while True:
        try:
            temperatura = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = converte_para_fahrenheit(temperatura)
            kelvin = converter_para_kelvin(temperatura)
        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")
            continue
        
        print(fahrenheit)
        print(kelvin)

        if input("Deseja converter outra temperatura? (s/n): ").lower() != 's':
            print("Encerrando o programa de conversão de temperatura.")
            break


if __name__ == "__main__":
    main()

