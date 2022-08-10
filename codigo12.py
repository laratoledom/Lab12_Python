M = []
L = int(input())
for a in range(L):
    M.append(input().split())
linha, coluna = (int(i) for i in input().split())
fim = 0
while fim != 1:
    posicao = M[linha][coluna]
    if posicao == "*":
        print('Jayce conseguiu chegar em Piltover')
        fim = 1
    elif posicao == "#" or posicao == ".":
        print('Jayce nao conseguiu chegar em Piltover')
        fim = 1
    elif 0 > linha > len(linha) or 0 > coluna > len(M[0]):
        print('Jayce nao conseguiu chegar em Piltover')
        fim = 1
    else:
        if posicao == "N":
            anterior_aoportal = "N"
            M[linha][coluna] = "."
            linha = linha - 1
        elif posicao == "S":
            anterior_aoportal = "S"
            M[linha][coluna] = "."
            linha = linha + 1
        elif posicao == "L":
            anterior_aoportal = "L"
            M[linha][coluna] = "."
            coluna = coluna + 1
        elif posicao == "O":
            anterior_aoportal = "O"
            M[linha][coluna] = "."
            coluna = coluna - 1
        else:
            portal = M[linha][coluna]
            portal_saida = []
            M[linha][coluna] = "@"
            i = 0
            while i < len(M):
                j = 0
                while j < len(M[0]):
                    if M[i][j] == portal:
                        portal_saida.append(i)
                        portal_saida.append(j)
                    j = j + 1
                i = i + 1
            M[linha][coluna] = portal
            linha = portal_saida[0]
            coluna = portal_saida[1]
            if anterior_aoportal == "N":
                linha = linha - 1
            elif anterior_aoportal == "S":
                linha = linha + 1
            elif anterior_aoportal == "L":
                coluna = coluna + 1
            else:
                coluna = coluna - 1
