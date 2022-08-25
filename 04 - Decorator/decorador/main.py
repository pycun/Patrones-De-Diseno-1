from cafe import Cafe, Latte, Frappucino
from decoradores import CremaBatida, Leche

def ver_detalle(cafe: Cafe) ->None:
    print(f"{cafe.get_descripcion()} cuesta {str(cafe.calcular_costo())}")


if __name__ == "__main__":
    cafe01 = Latte()
    cafe01 = CremaBatida(Leche(Leche(Leche(CremaBatida(cafe01)))))

    cafe02 = Frappucino()
    cafe02 = Leche(CremaBatida(Leche(CremaBatida(cafe02))))

    ver_detalle(cafe01)
    ver_detalle(cafe02)