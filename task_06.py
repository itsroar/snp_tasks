from enum import Enum


# вместо проверок if player1 == 'R' and player2 == 'S'...,
# будем переводить каждую фигуру в число, по которому можно будет понять, кто из игроков выиграл.
# присваиваем каждой фигуре номера 0, 1, 2...
# присваиваем каждой фигуре последовательность бит, где i-ый бит равен единице <=> эта фигура бьёт i-ую фигуру.
# для удобства заведём свой Enum, чтобы можно было сразу сравнить выбор игроков.
# https://docs.python.org/3/library/enum.html#when-to-use-new-vs-init
class BaseLogic(bytes, Enum):
    def __new__(cls, index, mask):
        obj = bytes.__new__(cls, [index])
        obj._value_ = index
        obj.mask = mask
        return obj

    def __lt__(self, other):
        assert type(self) == type(other)
        return self.mask & (1 << other.value) == 0

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other


class FigureSet(BaseLogic):
    # (номер фигуры, последовательность бит)
    r = (0, 0b100)
    p = (1, 0b001)
    s = (2, 0b010)


# при таком подходе можно удобно расширить набор фигур, и можно определить несколько проигрывающих элементов.
# я застал такой набор: камень, ножницы, бумага, карандаш, огонь, вода, и бутылка лимонада, и железная рука.
# я часто воду показывал)
# наобум подобрал последовательности
class ExtendedFigureSet(BaseLogic):
    r = (0, 0b01001100)
    p = (1, 0b00000001)
    s = (2, 0b01001010)
    pen = (3, 0b01000010)
    f = (4, 0b11001110)
    w = (5, 0b10011111)
    b = (6, 0b00100010)
    ih = (7, 0b01001111)


class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(choices, figure_set: BaseLogic = FigureSet) -> str:
    if len(choices) != 2:
        raise WrongNumberOfPlayersError

    # перегрузить бы квадратные скобки для Figure, но не знаю как
    try:
        for p in choices:
            if figure_set[p[1].lower()] is None:
                raise NoSuchStrategyError
    except KeyError:
        raise NoSuchStrategyError

    winner_id = 0 if figure_set[choices[0][1].lower()] >= figure_set[choices[1][1].lower()] else 1
    return f"{choices[winner_id][0]} {choices[winner_id][1]}"
