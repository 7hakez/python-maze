from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a ] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w ] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
 
        
class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x ,self.rect.y))


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform. scale(image.load("background.jpg"), (win_width, win_height))

player = Player("hero.png", 5, win_height - 80, 4)
monster = Enemy("monster.png",  win_width - 200, 280, 4)
final = GameSprite("treasure.png", win_width - 120, win_height - 80, 0)

w1 = Wall(255,255,255,0,1,1000,10)
w2 = Wall(255,255,255,70,200,525,10)
w3 = Wall(255,255,255,370,200,10,3800)
w4 = Wall(255,255,255,0,300,200,10)
w5 = Wall(255,255,255,300,100,10,100)
w6 = Wall(255,255,255,150,0,10,100)
w7 = Wall(255,255,255,170,420,200,10)
game = True  
finish = False
clock = time.Clock()
FPS = 75

mixer.init()
mixer.music.load("jungles.mp3")
mixer.music.play()       

money = mixer.Sound("money.mp3")
kick = mixer.Sound("kick.mp3")

font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN!", True, (193, 111, 255))
lose = font.render("YOU LOSE", True, (255,0,150))

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        player.reset()

        monster.update()
        monster.reset()

        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
        finish = True
        window.blit(lose,(200,200))
        kick.play()
    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win,(200,200))
        money.play()
    display.update()
    clock.tick(FPS)