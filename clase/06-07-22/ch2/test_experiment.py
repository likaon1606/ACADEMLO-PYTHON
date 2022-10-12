import cards
import pytest

def test_not_path_file():
    with pytest.raises(TypeError, match="Faltó el primer argumento"): # levanta la exepción porque no hay un tipo en cardsdb
        cards.CardsDB() #guardar en un archivo mis tarjetas
