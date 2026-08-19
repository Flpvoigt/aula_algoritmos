from algoritmos_testes.utils.functions import alternativas

while True:
    try:
        x = float(input("Digite o primeiro valor: "))
        y = float(input("Digite o segundo valor: "))
    except(ValueError):
        print("Digite um valor valido")
        continue
    print("Escolha uma das alternativas")

    alternativas()

    print()
    escolha = input("Digite aqui: ")

    match escolha:
        case "+":
            print(f"seu resultado é", x + y)
        case "-":
            print(f"seu resultado é", x - y)
        case "/":
            print(f"seu resultado é {x / y:.2f}")
        case "*":
            print(f"seu resultado é", x * y)
        case "**":
            print(f"seu resultado é {x ** y:.2f}")

    if input("Deseja calcular novamente (s/n): ") != "s":
        break
    