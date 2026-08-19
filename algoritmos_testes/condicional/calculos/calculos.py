from algoritmos_testes.utils.functions import custo_oportunidade

def main():
    while True:
        try:
            valor1 = float(input("Digite o valor do produto A: "))
            valor2 = float(input("Digite o valor do produto B: "))
        except:
            print("Digite um valor válido")
            continue

        oportunidade = custo_oportunidade(valor1, valor2)
        print(oportunidade)

        if input("Deseja calcular mais algu produto? (s/n): ") != "s":
            continue
    
if __name__ == "__main__":
    main()