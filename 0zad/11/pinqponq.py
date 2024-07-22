from superwires import games
import random

# Константы игры
ШИРИНА_ЭКРАНА = 800
ВЫСОТА_ЭКРАНА = 600
ЦВЕТ_ФОНА = (0, 0, 0)  # Черный
ЦВЕТ_РАКЕТКИ = (255, 255, 255)  # Белый
ЦВЕТ_ШАРИКА = (255, 0, 0)  # Красный
РАЗМЕР_РАКЕТКИ = (100, 10)
РАЗМЕР_ШАРИКА = 15
СКОРОСТЬ_ШАРИКА = [5, 5]
СКОРОСТЬ_РАКЕТКИ = 10

# Создаем экран
games.init(screen_width=ШИРИНА_ЭКРАНА, screen_height=ВЫСОТА_ЭКРАНА, fps=60)

# Определяем ракетку и шарик
class Ракетка(games.Sprite):
    def __init__(self):
        super().__init__(image=games.load_image("rectangle.png", transparent=False), x=ШИРИНА_ЭКРАНА // 2, y=ВЫСОТА_ЭКРАНА - 30)
        self.width = РАЗМЕР_РАКЕТКИ[0]
        self.height = РАЗМЕР_РАКЕТКИ[1]

    def update(self):
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= СКОРОСТЬ_РАКЕТКИ
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += СКОРОСТЬ_РАКЕТКИ

        # Оставляем ракетку внутри экрана
        if self.x < self.width // 2:
            self.x = self.width // 2
        if self.x > ШИРИНА_ЭКРАНА - self.width // 2:
            self.x = ШИРИНА_ЭКРАНА - self.width // 2

class Шарик(games.Sprite):
    def __init__(self):
        super().__init__(image=games.load_image("circle.png", transparent=False), x=ШИРИНА_ЭКРАНА // 2, y=ВЫСОТА_ЭКРАНА // 2)
        self.width = self.height = РАЗМЕР_ШАРИКА
        self.dx = СКОРОСТЬ_ШАРИКА[0]
        self.dy = СКОРОСТЬ_ШАРИКА[1]

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Отскок от верхней и нижней стенок
        if self.y <= 0 or self.y >= ВЫСОТА_ЭКРАНА - self.height:
            self.dy = -self.dy

        # Отскок от боковых стенок
        if self.x <= 0 or self.x >= ШИРИНА_ЭКРАНА - self.width:
            self.dx = -self.dx

        # Проверка на столкновение с ракеткой
        if (self.y + self.height >= ракетка.y - ракетка.height // 2 and 
            self.x + self.width >= ракетка.x - ракетка.width // 2 and 
            self.x <= ракетка.x + ракетка.width // 2):
            self.dy = -self.dy

        # Проверка, упал ли шарик за пределы экрана
        if self.y > ВЫСОТА_ЭКРАНА:
            games.screen.quit()  # Завершение игры

# Создаем ракетку и шарик
ракетка = Ракетка()
шарик = Шарик()

# Добавляем их на экран
games.screen.add(ракетка)
games.screen.add(шарик)

# Запускаем основной игровой цикл
games.screen.mainloop()
