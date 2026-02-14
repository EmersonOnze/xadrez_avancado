from tabuleiro import Tabuleiro
from jogo import Jogo
from pecas.torre import Torre

tabuleiro = Tabuleiro()

# Exemplo: colocar duas torres
tabuleiro.colocar_peca(Torre("branco"), 0, 0)
tabuleiro.colocar_peca(Torre("preto"), 7, 7)

jogo = Jogo(tabuleiro)

print("Xadrez Avançado - Fundamentos e Técnicas")

while True:
    print(f"\nTurno: {jogo._turno}")
    origem = input("Origem (linha,coluna): ")
    destino = input("Destino (linha,coluna): ")

    lo, co = map(int, origem.split(","))
    ld, cd = map(int, destino.split(","))

    jogo.jogar((lo, co), (ld, cd))
