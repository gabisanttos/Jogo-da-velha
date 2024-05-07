def exibir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        for j, elemento in enumerate(linha):
            print(elemento, end='')
            if j < 2:
                print(' | ', end='')
        print()
        if i < 2:
            print('-' * 9)

def fazer_jogada(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = jogador

def verificar_vencedor(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != ' ':
            return linha[0]
    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != ' ':
            return tabuleiro[0][coluna]
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        # Caso não haja um vencedor
        return None

def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

def jogar_jogo_da_velha():
    tabuleiro = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
    jogador_atual = 'X'
    vencedor = None

    while not vencedor:
        exibir_tabuleiro(tabuleiro)
        linha = int(input("Digite a linha da sua jogada (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna da sua jogada (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == ' ':
            fazer_jogada(tabuleiro, linha, coluna, jogador_atual)
            vencedor = verificar_vencedor(tabuleiro)

        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print("O jogador", vencedor, "venceu!")
        elif tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!") 
            break 
        
        jogador_atual = alternar_jogador(jogador_atual) 

def alternar_jogador(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

jogar_jogo_da_velha()
