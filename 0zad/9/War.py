import random

# Константы
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('h', 'd', 'c', 's')
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

def play_war(players):
    deck = Deck()
    player_cards = {}

    for player in players:
        card = deck.deal_card()
        if card:
            player_cards[player] = card
            print(f"{player} тянет {card}.")
        else:
            print("Недостаточно карт в колоде. Перезапускаем игру.")
            return

    winner = max(player_cards, key=lambda p: VALUES[player_cards[p].rank])
    print(f"\n{winner} выигрывает раунд с {player_cards[winner]}!\n")

def main():
    players = []
    num_players = int(input("Сколько игроков будет участвовать? "))

    for i in range(num_players):
        player_name = input(f"Введите имя игрока {i + 1}: ")
        players.append(player_name)

    play_again = "y"
    while play_again.lower() == "y":
        play_war(players)
        play_again = input("Хотите сыграть еще раз? (y/n): ")

    print("Спасибо за игру!")

if __name__ == "__main__":
    main()

input("\n\nНажмите Enter, чтобы выйти.")
