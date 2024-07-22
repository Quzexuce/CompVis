import random

# Константы
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('h', 'd', 'c', 's')
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

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
        if len(self.cards) == 0:
            self.refill_deck()
        return self.cards.pop()

    def refill_deck(self):
        print("Карт в колоде недостаточно. Перетасовываем новую колоду.")
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'A':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return ', '.join([str(card) for card in self.cards]) + f" (value: {self.value})"

def take_bet(chips):
    while True:
        try:
            bet = int(input(f"Сколько вы хотите поставить? У вас есть {chips} фишек: "))
            if bet > chips:
                print(f"Извините, ваша ставка не может превышать {chips} фишек.")
            elif bet <= 0:
                print("Ставка должна быть положительным числом.")
            else:
                return bet
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def hit(deck, hand):
    hand.add_card(deck.deal_card())

def hit_or_stand(deck, hand):
    while True:
        try:
            move = input("Вы хотите взять карту или остановиться? (введите 'y' или 'n'): ").lower()
            if move == 'y':
                hit(deck, hand)
            elif move == 'n':
                return False
            else:
                print("Извините, введите 'y' для взятия карты или 'n' для остановки.")
                continue
            return True
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def show_some(player, dealer):
    print("\nКарты дилера:")
    print("<карта скрыта>")
    print(dealer.cards[1])
    print("\nКарты игрока:", *player.cards, sep='\n')

def show_all(player, dealer):
    print("\nКарты дилера:", *dealer.cards, sep='\n')
    print("Значение карт дилера =", dealer.value)
    print("\nКарты игрока:", *player.cards, sep='\n')
    print("Значение карт игрока =", player.value)

def player_busts(player, dealer, chips):
    print("Игрок проиграл!")
    chips -= 1

def player_wins(player, dealer, chips):
    print("Игрок выиграл!")
    chips += 1

def dealer_busts(player, dealer, chips):
    print("Дилер проиграл!")
    chips += 1

def dealer_wins(player, dealer, chips):
    print("Дилер выиграл!")
    chips -= 1

def push(player, dealer):
    print("Ничья! Ставка возвращена.")

def main():
    chips = 100  # начальные фишки

    while True:
        print("\nДобро пожаловать в Блэк-джек!")

        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        bet = take_bet(chips)

        show_some(player_hand, dealer_hand)

        playing = True
        while playing:
            playing = hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, chips)
            else:
                push(player_hand, dealer_hand)

        print(f"\nУ вас осталось {chips} фишек.")
        new_game = input("Хотите сыграть еще раз? (y/n): ").lower()
        if new_game != 'y':
            print("Спасибо за игру!")
            break

main()
