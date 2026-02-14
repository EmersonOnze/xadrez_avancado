from abc import ABC, abstractmethod

class Peca(ABC):
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @abstractmethod
    def movimentos_validos(self, posicao, tabuleiro):
        pass
