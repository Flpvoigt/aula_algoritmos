from utils.funcoes import calcular_media

def main():
    while True:
        try:
            n1 = float(input("Digite a primeira nota: "))
            n2 = float(input("Digite a segunda nota: "))
            n3 = float(input("Digite a terceira nota: "))

        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")
            continue
    
        media_ponderada, media = calcular_media(n1, n2, n3)

        print(f"A média ponderada é: {media_ponderada:.2f}")
        print(f"A média aritmética é: {media:.2f}")

        resp = input("Deseja calcular novamente? (s/n): ")
        if resp.lower() != 's':
            break

if __name__ == "__main__":
    main()