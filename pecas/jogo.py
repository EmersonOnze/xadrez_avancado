class Jogo:
    def __init__(self, tabuleiro):
        self._tabuleiro = tabuleiro
        self._turno = "branco"

    def alternar_turno(self):
        self._turno = "preto" if self._turno == "branco" else "branco"

    def jogar(self, origem, destino):
        try:
            self._tabuleiro.mover(origem, destino)
            self.alternar_turno()
        except ValueError as erro:
            print("Erro:", erro)
