from .peca import Peca

class Torre(Peca):
    def movimentos_validos(self, posicao, tabuleiro):
        linha, coluna = posicao
        movimentos = []

        direcoes = [(1,0), (-1,0), (0,1), (0,-1)]

        for dl, dc in direcoes:
            l, c = linha + dl, coluna + dc

            while tabuleiro.dentro_limite(l, c):
                if tabuleiro.posicao_ocupada(l, c):
                    if tabuleiro.peca_em(l, c).cor != self.cor:
                        movimentos.append((l, c))
                    break

                movimentos.append((l, c))
                l += dl
                c += dc

        return movimentos
