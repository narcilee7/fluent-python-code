"""
1.1 一摞Python风格的纸牌

主要展示学习__getitem__和__len__
"""
import collections

Card = collections.namedtuple('card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 切分为数组
    suits = 'spades diamonds clubs hearts'.split( )

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
deck = FrenchDeck()

# print(len(deck))
# print(deck)
# beer_deck = Card('7', 'diamonds')
# print(Card)

# print(beer_deck)
print(deck[0])

print(deck[1])

print(deck[2])

print(deck[3])

print(deck[4])