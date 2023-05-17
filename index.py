def exibir_tabuleiro(tabuleiro):
    print("-------------")
    for linha in tabuleiro:
        print("|", end="")
        for celula in linha:
            print(" " + celula + " ", end="|")
        print("\n-------------")

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        linha = int(input("Digite o número da linha (0-2): "))
        coluna = int(input("Digite o número da coluna (0-2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print("Jogador", jogador_atual, "venceu!")
            break

        if all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogar_jogo_da_velha()