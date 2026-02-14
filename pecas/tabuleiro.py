class Tabuleiro:
    def __init__(self):
        self._grade = [[None for _ in range(8)] for _ in range(8)]

    def dentro_limite(self, linha, coluna):
        return 0 <= linha < 8 and 0 <= coluna < 8

    def posicao_ocupada(self, linha, coluna):
        return self._grade[linha][coluna] is not None

    def peca_em(self, linha, coluna):
        return self._grade[linha][coluna]

    def colocar_peca(self, peca, linha, coluna):
        self._grade[linha][coluna] = peca

    def mover(self, origem, destino):
        lo, co = origem
        ld, cd = destino

        peca = self._grade[lo][co]

        if peca is None:
            raise ValueError("Não há peça na origem")

        movimentos = peca.movimentos_validos(origem, self)

        if destino not in movimentos:
            raise ValueError("Movimento inválido")

        self._grade[ld][cd] = peca
        self._grade[lo][co] = None
