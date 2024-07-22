from superwires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)

class Chef(games.Sprite):
    """ Повар, который перемещает сковороду влево и вправо """
    image = games.load_image("chef.png")

    def __init__(self):
        """ Инициализация повара """
        super(Chef, self).__init__(image=Chef.image,
                                   x=games.screen.width/2,
                                   bottom=games.screen.height)
        self.score = games.Text(value=0, size=25, color=color.white,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """ Перемещает повара влево и вправо по нажатию клавиш """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 5
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 5

        # Ограничение движения повара в пределах экрана
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

    def catch(self):
        """ Поймать падающий арбуз """
        self.score.value += 10
        self.score.right = games.screen.width - 10

class Waterlemon(games.Sprite):
    """ Падающий арбуз """
    image = games.load_image("арбуз.png")
    speed = 1

    def __init__(self, x, y=90):
        super(Waterlemon, self).__init__(image=Waterlemon.image, x=x, y=y, dy=Waterlemon.speed)

    def update(self):
        """ Проверка, не пойман ли арбуз поваром """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                if isinstance(sprite, Chef):
                    self.handle_collide()
                    sprite.catch()

    def end_game(self):
        """ Завершение игры """
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)

    def handle_collide(self):
        """ Действия при столкновении с поваром """
        self.destroy()

def increase_difficulty():
    """ Увеличивает сложность игры со временем """
    Waterlemon.speed += 0.1

def create_waterlemon():
    """ Создание нового арбуза """
    x = random.randrange(0, games.screen.width)
    new_waterlemon = Waterlemon(x=x)
    games.screen.add(new_waterlemon)

def main():
    """ Основная игровая функция """
    wall_image = games.load_image("1.jpeg", transparent=False)
    games.screen.background = wall_image

    the_chef = Chef()
    games.screen.add(the_chef)

    # Создание новой пиццы каждые 2 секунды
    games.screen.add_timer(create_waterlemon, 2000)

    # Увеличение сложности каждые 10 секунд
    games.screen.add_timer(increase_difficulty, 10000)

    games.screen.mainloop()

if __name__ == "__main__":
    main()

