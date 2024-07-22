from superwires import games, color
import random

games.init(screen_width=800, screen_height=600, fps=60)

class Player(games.Sprite):
    image = games.load_image("player.png")

    def __init__(self):
        super(Player, self).__init__(image=Player.image,
                                     x=games.mouse.x,
                                     bottom=games.screen.height - 10)
        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_collision()

    def check_collision(self):
        for falling_object in self.overlapping_sprites:
            self.end_game()

    def end_game(self):
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)

class FallingObject(games.Sprite):
    image = games.load_image("Waterlemon.png")

    def __init__(self, x, y=90, dy=5):
        super(FallingObject, self).__init__(image=FallingObject.image,
                                            x=x, y=y, dy=dy)

    def update(self):
        if self.top > games.screen.height:
            self.destroy()

def create_falling_object():
    if len(games.screen.get_all_sprites(FallingObject)) < 6:
        x = random.randint(0, games.screen.width)
        dy = random.randint(2, 6)
        new_object = FallingObject(x=x, dy=dy)
        games.screen.add(new_object)

def main():
    player = Player()
    games.screen.add(player)

    
    games.screen.timer_every(interval=0.5, action=create_falling_object)

    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()

if __name__ == "__main__":
    main()
