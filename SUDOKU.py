tamanho_da_grade = 9
tamanho_da_subgrade = 3

def imprimir_grade(grade):
    for i, linha in enumerate(grade):
        if i % tamanho_da_subgrade == 0 and i != 0:
            print("-" * (tamanho_da_grade * 2 + 3))
        linha_formatada = ""
        for j, celula in enumerate(linha):
            if j % tamanho_da_subgrade == 0 and j != 0:
                linha_formatada += "| "
            linha_formatada += str(celula) if celula != 0 else " "
            linha_formatada += " "
        print(linha_formatada)

def verificar_solucao(grade):
    for i in range(tamanho_da_grade):
        if not (verificar_linha(grade, i) and verificar_coluna(grade, i) and verificar_subgrade(grade, i)):
            return False
    return True

def verificar_linha(grade, linha):
    numeros = set()
    for num in grade[linha]:
        if num in numeros:
            return False
        if num != 0:
            numeros.add(num)
    return True

def verificar_coluna(grade, coluna):
    numeros = set()
    for i in range(tamanho_da_grade):
        num = grade[i][coluna]
        if num in numeros:
            return False
        if num != 0:
            numeros.add(num)
    return True

def verificar_subgrade(grade, subgrade):
    numeros = set()
    inicio_linha = (subgrade // tamanho_da_subgrade) * tamanho_da_subgrade
    inicio_coluna = (subgrade % tamanho_da_subgrade) * tamanho_da_subgrade
    for i in range(tamanho_da_subgrade):
        for j in range(tamanho_da_subgrade):
            num = grade[inicio_linha + i][inicio_coluna + j]
            if num in numeros:
                return False
            if num != 0:
                numeros.add(num)
    return True

def verificar_espacos(grade):
    """Função para verificar se ainda há espaços em branco na grade."""
    for linha in grade:
        if 0 in linha:
            return True  # Ainda há espaços em branco
    return False  # Todos os espaços estão preenchidos

def jogar():
    grade = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    while True:
        imprimir_grade(grade)
        linha = input("Digite a linha (0-8): ")
        coluna = input("Digite a coluna (0-8): ")
        valor = input("Digite o valor (1-9): ")
        if linha.isdigit() and coluna.isdigit() and valor.isdigit():
            linha = int(linha)
            coluna = int(coluna)
            valor = int(valor)
            if linha < 0 or linha >= tamanho_da_grade:
                print("Linha inválida! Use números entre 0 e 8.")
                continue
            if coluna < 0 or coluna >= tamanho_da_grade:
                print("Coluna inválida! Use números entre 0 e 8.")
                continue
            if valor < 1 or valor > 9:
                print("Valor inválido! Use números entre 1 e 9.")
                continue
            if grade[linha][coluna] == 0:
                grade[linha][coluna] = valor
                if not verificar_espacos(grade):
                    if verificar_solucao(grade):
                        print("Parabéns! Você resolveu o Sudoku!")
                    else:
                        print("A solução está completa, mas incorreta.")
                    break
            else:
                print("Essa posição já está preenchida.")
        else:
            print("Entrada inválida! Por favor, insira números válidos.")

if __name__ == "__main__":
    jogar()
