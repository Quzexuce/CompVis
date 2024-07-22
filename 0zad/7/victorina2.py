import pickle

def next_line(file):
    """Возвращает следующую строку из файла, убирая символ новой строки."""
    line = file.readline()
    return line.strip()

def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    points = next_line(the_file)
    if points:
        points = int(points)
    return category, question, answers, correct, explanation, points

def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")

def display_high_scores():
    """Отображает таблицу рекордов."""
    try:
        with open("high_scores.dat", "rb") as file:
            high_scores = pickle.load(file)
        print("\nТаблица рекордов:")
        for score in high_scores:
            print(f"{score['name']} - {score['score']}")
    except FileNotFoundError:
        print("\nТаблица рекордов пока пуста.")

def save_high_score(name, score):
    """Сохраняет результат игрока в таблицу рекордов."""
    new_score = {'name': name, 'score': score}
    try:
        with open("high_scores.dat", "rb") as file:
            high_scores = pickle.load(file)
    except FileNotFoundError:
        high_scores = []

    high_scores.append(new_score)
    high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)[:5]  # Хранить только топ-5

    with open("high_scores.dat", "wb") as file:
        pickle.dump(high_scores, file)

def main():
    trivia_file = open("trivia.txt", "r", encoding="utf-8")
    title = next_line(trivia_file)
    welcome(title)
    display_high_scores()

    name = input("Введите ваше имя: ")
    score = 0

    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        print(category)
        print()
        print(question)
        for i in range(4):
            print(f"\t{i + 1} - {answers[i]}")
        
        # Получаем ответ
        user_answer = input("Ваш ответ: ")
        
        # Проверка ответа
        if user_answer == correct:
            print("\nПравильно!", end=" ")
            score += points
        else:
            print("\nНеправильно.", end=" ")
        
        print(explanation)
        print(f"Номинал вопроса: {points}")
        print(f"Ваш текущий счёт: {score}\n\n")
        
        category, question, answers, correct, explanation, points = next_block(trivia_file)
    
    trivia_file.close()
    
    print("Это был последний вопрос!")
    print(f"Ваш финальный счёт: {score}")
    save_high_score(name, score)

main()
