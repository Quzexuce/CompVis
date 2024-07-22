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

class Player:
    def __init__(self, name, chips=100):
        self.name = name
        self.chips = chips
        self.bet = 0
        self.hand = Hand()

    def place_bet(self):
        while True:
            try:
                bet = int(input(f"{self.name}, сколько вы хотите поставить? У вас есть {self.chips} фишек: "))
                if bet > self.chips:
                    print(f"Извините, ваша ставка не может превышать {self.chips} фишек.")
                elif bet <= 0:
                    print("Ставка должна быть положительным числом.")
                else:
                    self.bet = bet
                    self.chips -= bet
                    return
            except ValueError:
                print("Пожалуйста, введите корректное число.")

    def win_bet(self):
        self.chips += 2 * self.bet
        self.bet = 0

    def lose_bet(self):
        self.bet = 0

    def push_bet(self):
        self.chips += self.bet
        self.bet = 0

def hit(deck, hand):
    hand.add_card(deck.deal_card())

def hit_or_stand(deck, player):
    while True:
        try:
            move = input(f"{player.name}, вы хотите взять карту или остановиться? (введите 'y' или 'n'): ").lower()
            if move == 'y':
                hit(deck, player.hand)
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
    print(dealer.hand.cards[1])
    print("\nКарты игрока:", *player.hand.cards, sep='\n')

def show_all(player, dealer):
    print("\nКарты дилера:", *dealer.hand.cards, sep='\n')
    print("Значение карт дилера =", dealer.hand.value)
    print("\nКарты игрока:", *player.hand.cards, sep='\n')
    print("Значение карт игрока =", player.hand.value)

def player_busts(player, dealer):
    print(f"{player.name} проиграл!")
    player.lose_bet()

def player_wins(player, dealer):
    print(f"{player.name} выиграл!")
    player.win_bet()

def dealer_busts(player, dealer):
    print("Дилер проиграл!")
    player.win_bet()

def dealer_wins(player, dealer):
    print("Дилер выиграл!")
    player.lose_bet()

def push(player, dealer):
    print("Ничья! Ставка возвращена.")
    player.push_bet()

def play_blackjack():
    num_players = int(input("Сколько игроков будет участвовать? "))
    players = [Player(input(f"Введите имя игрока {i + 1}: ")) for i in range(num_players)]

    while True:
        print("\nДобро пожаловать в Блэк-джек!")

        deck = Deck()
        dealer = Player("Дилер")

        for player in players:
            player.hand = Hand()
            player.place_bet()

        dealer.hand = Hand()
        for _ in range(2):
            for player in players:
                player.hand.add_card(deck.deal_card())
            dealer.hand.add_card(deck.deal_card())

        for player in players:
            show_some(player, dealer)
            playing = True
            while playing:
                playing = hit_or_stand(deck, player)
                show_some(player, dealer)
                if player.hand.value > 21:
                    player_busts(player, dealer)
                    break

        while dealer.hand.value < 17:
            hit(deck, dealer.hand)

        show_all(players[0], dealer)  # Show all cards for the first player to avoid redundancy

        for player in players:
            if player.hand.value <= 21:
                if dealer.hand.value > 21:
                    dealer_busts(player, dealer)
                elif dealer.hand.value > player.hand.value:
                    dealer_wins(player, dealer)
                elif dealer.hand.value < player.hand.value:
                    player_wins(player, dealer)
                else:
                    push(player, dealer)

        players = [player for player in players if player.chips > 0]
        if not players:
            print("У всех игроков закончились фишки. Игра окончена.")
            break

        print("\nТекущие фишки игроков:")
        for player in players:
            print(f"{player.name}: {player.chips} фишек")

        new_game = input("Хотите сыграть еще раз? (y/n): ").lower()
        if new_game != 'y':
            print("Спасибо за игру!")
            break


play_blackjack()

input("\n\nНажмите Enter, чтобы выйти.")
