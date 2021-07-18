import pygame,sys,random
pygame.init()

class Player:
    def __init__(self):
        self.height = 25
        self.width = 25
        self.image = pygame.image.load("cowboy hat.png")
        self.body = self.image.get_rect(center = (100,200))
        #pygame.Rect(400 / 2,400 / 2, self.width,self.height)
        self.x_speed = 0
        self.y_speed = 0

        #health
        self.health = 20
        self.r2 = pygame.Rect(self.body.centery - 5, self.body.centerx + 5, self.health, 5)

    def draw_move(self):
        self.body.x += self.x_speed
        self.body.y += self.y_speed
        if self.body.right >= 400:
            self.body.right = 400
        if self.body.left <= 0:
            self.body.left = 0
        if self.body.top <= 0:
            self.body.top = 0
        if self.body.bottom >= 400:
            self.body.bottom = 400

        screen.blit(self.image,self.body)
        #pygame.draw.rect(screen, (255, 255, 0), self.body)

    def health_stuff(self):
        global game_state
        if self.health <= 0:
            game_state = "over"
        if self.health > 0:
            self.r2.width = self.health
            self.r2.centerx,self.r2.centery = self.body.centerx,self.body.centery - 25
            pygame.draw.rect(screen, (0, 255, 0), self.r2,5)
class Bullet:
    def __init__(self):
        self.body = pygame.Rect(p1.body.centerx,p1.body.centery,10,10)
        self.direction = 0

    def check_border(self):
        global state
        if self.body.right >= 400 + 100:
            self.body.center = p1.body.center
            state = "ready"
        if self.body.left <= 0 - 100:
            self.body.center = p1.body.center
            state = "ready"
        if self.body.top <= 0 - 100:
            self.body.center = p1.body.center
            state = "ready"
        if self.body.bottom >= 400 + 100:
            self.body.center = p1.body.center
            state = "ready"

    def draw(self):
        if state == "fire":
            if self.direction == 1:
                self.body.y -= 10
            if self.direction == 2:
                self.body.x += 10
            if self.direction == 3:
                self.body.y += 10
            if self.direction == 4:
                self.body.x -= 10

            pygame.draw.rect(screen, (255,255,0),self.body)
class Enemy:
    def __init__(self):
        self.enemies = []
        self.health = 20
        self.speed = 2
        self.r2 = pygame.Rect(50,50, self.health, 5)
        self.n = 0
        self.ready = "ready"
        self.image = pygame.image.load("military.png")
        for enemy in range(random.randrange(50,100)):
            self.body = self.image.get_rect(center = (random.randrange(500, 700), random.randrange(40, 370)))
            #pygame.Rect(random.randrange(500, 700), random.randrange(40, 370), random.randrange(20, 70),random.randrange(20, 70))
            self.enemies.append(self.body)

        self.people_num = len(self.enemies)

        self.bullet = pygame.Rect(self.enemies[self.n].centerx,self.enemies[self.n].centery,10,10)

    def spawning(self):
        screen.blit(self.image,self.enemies[self.n])
        if self.health <= 0:
            self.num = random.randint(0,10)
            if self.num == 0 or 5:
                g.itrue = True
                g.i_r.center = self.enemies[self.n].center
            #   .pop() takes the index value as a parameter
            self.enemies.pop(self.n)
            self.people_num = len(self.enemies)
            self.health = 20
            g.score += 1
            self.n += 1

    def shooting(self):
        if self.enemies[self.n].centerx <= 400:
            self.ready = "fire"
        if self.ready == "fire":
            self.bullet.x -= 3
            if self.bullet.x <= 0:
                self.bullet.center = self.enemies[self.n].centerx, self.enemies[self.n].centery
            if self.bullet.colliderect(p1.body):
                p1.health -= 5
                self.bullet.center = self.enemies[self.n].centerx, self.enemies[self.n].centery

            pygame.draw.rect(screen,(255,255,0),self.bullet)


    def check_collision(self):
        global state
        if b1.body.colliderect(self.enemies[self.n]):
            state = "ready"
            b1.body.center = p1.body.center
            self.health -= 10

    def move(self):
        global game_state
        self.enemies[self.n].centerx -= self.speed
        if self.enemies[self.n].left <= 0:
            game_state = "over"

    def score_check(self):
        if g.score >= 20:
            self.speed += 1
        if g.score >= 40:
            self.speed += 1
        if g.score >= 60:
            self.speed += 1
        if g.score >= 80:
            self.speed += 1
        if g.score >= 100:
            self.speed += 1


    def health_col(self):
        if self.health <= 20:
            self.r2.width = self.health
            self.r2.centerx, self.r2.centery = self.enemies[self.n].centerx, self.enemies[self.n].centery - 30
            pygame.draw.rect(screen, (255, 0, 0), self.r2)
        if p1.body.colliderect(self.enemies[self.n]):
            self.enemies.pop(self.n)
            b1.body.center = p1.body.center
            p1.health -= 5
class Game:
    def __init__(self):
        #variables
        self.score = 0
        self.high_score = 0
        #score
        self.gs = font2.render(f"SCORE:{self.score}", False, (255, 255, 255), (0, 0, 0))
        self.gsr = self.gs.get_rect(center=(30, 10))
        self.numt = font2.render(f"LEFT:{e1.people_num}", False, (255, 255, 255), (0, 0, 0))
        self.numt_r = self.numt.get_rect(center=(30, 30))

        #trailer
        self.balon = pygame.image.load("air-hot-balloon.png")
        self.b_r = self.balon.get_rect(center = (500,200))
        self.t_T = font.render("PRESS SPACE TO BEGIN", False,(255,255,255),(0,0,0))
        self.tTr = self.t_T.get_rect(center = (200,200))


        #health_item
        self.itrue = False
        self.i = pygame.image.load("heart.png")
        self.i_r = self.i.get_rect(center = (200,200))

        #start
        self.game_S = font.render("PUBG 2D",False,(255,255,255))
        self.game_S2 = font.render("PUBG 2D", False, (255, 255, 255))
        self.game_SR = self.game_S.get_rect(center = (200, 200))
        self.game_S2R = self.game_S2.get_rect(center = (201, 201))
        self.begin = font.render("PRESS SPACE TO BEGIN",False,(255,255,255))
        self.begin_r = self.begin.get_rect(center = (200,250))

        #game over
        self.high_t = font.render(f"YOUR HIGH SCORE:{self.high_score}", False, (255, 255, 255), (0, 0, 0))
        self.hscore_r = self.high_t.get_rect(center=(200, 270))
        self.score_t = font.render(f"YOUR SCORE:{self.score}",False,(255,255,255),(0,0,0))
        self.score_r = self.score_t.get_rect(center = (200,290))
        self.over = font.render("GAME OVER",False,(255,255,255),(0,0,0))
        self.over_r = self.over.get_rect(center = (200,160))


    def game_over(self):
        self.high_t = font.render(f"YOUR HIGH SCORE:{self.high_score}", False, (255, 255, 255), (0, 0, 0))
        self.score_t = font.render(f"YOUR SCORE:{self.score}", False, (255, 255, 255), (0, 0, 0))
        screen.blit(self.score_t,self.score_r)
        screen.blit(self.high_t, self.hscore_r)
        screen.blit(self.over, self.over_r)

    def score_update(self):
        if self.high_score <= self.score:
            self.high_score = self.score
        self.gs = font2.render(f"SCORE:{self.score}", False, (255, 255, 255), (0, 0, 0))
        screen.blit(self.gs,self.gsr)

    def trailer(self):
        global player_r
        self.b_r.x -= 2
        if self.b_r.x <= 200:
            if self.b_r.x == 190:
                player_r.center = self.b_r.center
            if player_r.y >= 0:
                player_r.y += 2

            screen.blit(player, player_r)

        if self.b_r.left <= -100:
            screen.blit(self.t_T,self.tTr)


        screen.blit(self.balon,self.b_r)

    def show_people(self):
        self.numt = font2.render(f"LEFT:{e1.people_num}", False, (255, 255, 255), (0, 0, 0))
        screen.blit(self.numt,self.numt_r)



    def draw_health_item(self):
        if self.itrue:
            if p1.body.colliderect(self.i_r):
                p1.health += 5
                self.itrue = False
            screen.blit(self.i,self.i_r)


    def game_start(self):
        screen.blit(self.game_S, self.game_SR)
        screen.blit(self.game_S2, self.game_S2R)
        screen.blit(self.begin,self.begin_r)


#variables
state = "ready"
game_state = "game_start"
font = pygame.font.Font(None,30)
font2 = pygame.font.Font(None,20)

#objects
p1 = Player()
b1 = Bullet()
e1 = Enemy()
g = Game()

#screen
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
title = pygame.display.set_caption("PUBG CHALLENGE")
background = pygame.image.load("broken-brown-eyeshadow-powder-background.jpg").convert_alpha()
cloud = pygame.image.load("white-cloud-blue-sky.jpg").convert_alpha()

#trailer player and stuff
player = pygame.image.load("cowboy hat.png")
player_r = player.get_rect(center = (g.b_r.centerx,g.b_r.centery))



def game_loop():
    if game_state == "game_start":
        screen.fill((0,0,0))
        g.game_start()
    if game_state == "trailer":
        screen.blit(cloud,(0,0))
        g.trailer()

    if game_state == "in_game":
        # score
        g.score_update()
        #draw
        g.draw_health_item()
        p1.draw_move()
        b1.draw()
        e1.spawning()
        g.show_people()
        e1.shooting()
        #collision
        b1.check_border()
        e1.check_collision()
        e1.health_col()
        p1.health_stuff()
        #enemy move
        e1.move()
    if game_state == "over":
        screen.fill((0, 0, 0))
        g.game_over()


    pygame.display.update()
    clock.tick(60)
while True:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_w:
                #b1.direction = 1
            #if event.key == pygame.K_d:
                #b1.direction = 2
            #if event.key == pygame.K_s:
                #b1.direction = 3
            #if event.key == pygame.K_a:
                #b1.direction = 4

            if event.key == pygame.K_UP:
                p1.y_speed = -4
                if state == "ready":
                    b1.direction = 1
            if event.key == pygame.K_DOWN:
                p1.y_speed = 4
                if state == "ready":
                    b1.direction = 3
            if event.key == pygame.K_RIGHT:
                p1.x_speed = 4
                if state == "ready":
                    b1.direction = 2
            if event.key == pygame.K_LEFT:
                p1.x_speed = -4
                if state == "ready":
                    b1.direction = 4
            if event.key == pygame.K_SPACE:
                if game_state == "in_game":
                    if state == "ready":
                        state = "fire"
                        b1.body.center = p1.body.center
                else:
                    if game_state == "game_start":
                        game_state = "trailer"
                    elif game_state == "trailer":
                        game_state = "in_game"
                    elif game_state == "over":
                        game_state = "in_game"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p1.y_speed = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                p1.x_speed = 0


    game_loop()