from __future__ import annotations

from enum import Enum, auto

class Suit(Enum):
    HEART = auto()
    DIAMOND = auto()
    CLUBS = auto()
    SPADES = auto()

class Rank:
    __value: int

    def __init__(self, value: int) -> None:
        self.__value: int = value

    def max(self, rank2: Rank) -> Rank:
        if self.__value > rank2.__value:
            return self
        else:
            return rank2

ACE = Rank(14)
KIND = Rank(13)
QUEEN = Rank(12)
JACK = Rank(11)
TEN = Rank(10)
NINE = Rank(9)
EIGHT = Rank(8)
SEVEN = Rank(7)
SIX = Rank(6)

class Card:
    suit: Suit
    rank: Rank
    def __init__(self, suit: Suit, rank: Rank) -> None:
        self.suit = suit
        self.rank = rank

def main() -> None:
    print("Lecture 2!")
    suit: Suit = Suit.DIAMOND
    rank1 = TEN
    rank2 = JACK
    strongest = rank1.max(rank2)
    print(strongest == JACK)

if __name__ == "__main__":
    main()
