from algoritmos_testes.utils.functions import verificar_temperatura

def main():
    while True:
        try:
            temperatura = float(input("Quantos graus está fazendo em sua cidade?: "))
        except(ValueError):
            print("Digite um valor válido")
            continue

        conversao = verificar_temperatura(temperatura)
        print(conversao)

        if input("Deseja digitar mais alguma temperatura?: ").lower() != "s":
            continue

if __name__ == "__main__":
    main()