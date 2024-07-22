import random

def display_board(board):
    """Вывод игрового поля на экран."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def is_winner(board, player):
    """Проверяет, выиграл ли игрок."""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
                   (0, 4, 8), (2, 4, 6))            # диагонали
    for row in WAYS_TO_WIN:
        if all(board[cell] == player for cell in row):
            return True
    return False

def minimax(board, depth, is_maximizing, computer, human):
    """Алгоритм Минимакс."""
    if is_winner(board, computer):
        return 1
    if is_winner(board, human):
        return -1
    if all(space != ' ' for space in board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer
                score = minimax(board, depth + 1, False, computer, human)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = human
                score = minimax(board, depth + 1, True, computer, human)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def computer_move(board, computer, human):
    """Ход компьютера, использующий стратегию Минимакс."""
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer
            score = minimax(board, 0, False, computer, human)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    print("Я выберу поле номер", best_move)
    return best_move

def human_move(board, human):
    """Запрашивает ход у игрока."""
    move = None
    while move not in range(9) or board[move] != ' ':
        move = ask_number("Ваш ход. Выберите поле (0-8): ", 0, 9)
        if board[move] != ' ':
            print("Это поле уже занято. Выберите другое.")
    return move

def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low, high):
        response = input(question)
        if response.isdigit():
            response = int(response)
            if response not in range(low, high):
                print(f"Пожалуйста, введите число в диапазоне от {low} до {high}.")
        else:
            print("Пожалуйста, введите корректное число.")
    return response

def main():
    print("Добро пожаловать в игру 'Крестики-нолики'!")
    board = [' '] * 9
    computer = 'O'
    human = 'X'
    display_board(board)

    first_move = ask_number("Кто будет ходить первым? (1 - человек, 2 - компьютер): ", 1, 3)

    if first_move == 2:
        current_turn = 'computer'
    else:
        current_turn = 'human'

    while True:
        if current_turn == 'human':
            move = human_move(board, human)
            board[move] = human
            if is_winner(board, human):
                display_board(board)
                print("Поздравляю! Вы победили!")
                break
            current_turn = 'computer'
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
            if is_winner(board, computer):
                display_board(board)
                print("Компьютер победил!")
                break
            current_turn = 'human'
        
        display_board(board)

        if all(space != ' ' for space in board):
            print("Ничья!")
            break

main()
