from algoritmos_testes.utils.functions import recebe_notas

def main():
    while True:
        try:
            nota1 = float(input("Insira a primeira nota do aluno: "))
            nota2 = float(input("Insira a primeira nota do aluno: "))
        except(ValueError):
            print("Digite uma nota válida")
            continue

        Media_final = recebe_notas(nota1, nota2)

        if Media_final < 7:
            print("Reprovado")

        else:
            print("Aprovado")

        if input("Deseja calcular outra media (s/n): ").lower() != "s": 
            break

if __name__ == "__main__":
    main()


