import pygame
import time

pygame.init()

class Color:
    black = (0,0,0)
    white =(255,255,255)
    red =(255,0,0)
    blue = (0,0,255)
    yellow = (255,255,0)
class Rocket:
    def __init__(self,x,y,color):
        self.w = 15
        self.h = 60
        self.x = x 
        self.y = y
        self.color = color
        self.speed = 15
        self.score = 0
        self.y_change = 0
        self.area = pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])

    def show(self):
        self.area = pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])

    def move(self,b):
        self.y += self.y_change * self.speed

        if self.y < b.y:
            self.y += self.speed

        elif self.y > b.y:
            self.y -= self.speed

        if b.x > Game.width / 2 and b.x_dir > 0:
                if b.y > self.y:
                    self.y_change = 1

                if b.y < self.y:
                    self.y_change = -1
                    
        if self.y < 0:
            self.y = 0
        if self.y > Game.height - self.h:
            self.y = Game.height - self.h
        


class Ball :
    def __init__(self):
        self.r = 10
        self.x = Game.width // 2
        self.y = Game.height // 2
        self.speed = 15
        self.color = Color.yellow
        self.x_dir = 1
        self.y_dir = 1
        self.area = pygame.draw.circle(Game.screen,self.color,[self.x,self.y],self.r)

    def show(self):
        self.area = pygame.draw.circle(Game.screen,self.color,[self.x,self.y],self.r)

    def move(self):
        
        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir

        if self.y < 10 :
            self.y_dir *= -1

        if self.y > Game.height -10:
            self.y_dir *= -1

        

        
    def new(self):
        self.x = Game.width /2
        self.y = Game.height /2
        time.sleep(1)
        


class Game:
    width = 700
    height = 400
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Ping pong')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("calibri",100)

    fps = 30

    @staticmethod
    def play():
        
        me = Rocket(10,Game.height/2 , Color.red)
        cpu = Rocket(Game.width - 25 ,Game.height/2 , Color.blue)
        ball = Ball()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    
                if event.type == pygame.MOUSEMOTION:
                    me.y = pygame.mouse.get_pos()[1]

                    if me.y > Game.height - me.h:
                        me.y = Game.height - me.h

            ball.move()
            cpu.move()

            if ball.x < 0:
                cpu.score += 1
                ball.new()
            elif ball.x > Game.width:
                me.score += 1
                ball.new()

            if ball.area.colliderect(me.area) :
                ball.x_dir *= -1
                ball.x = 20 + me.w


            if ball.area.colliderect(cpu.area):
                ball.x_dir *= -1
                ball.x = Game.width - cpu.w - 20
                



            Game.screen.fill(Color.black)
            pygame.draw.rect(Game.screen,Color.white,(0,0,Game.width,Game.height),8)
            pygame.draw.aaline(Game.screen,Color.white,[Game.width/2 , 0],[Game.width/2,Game.height])
            me.show()
            cpu.show()
            ball.show()

            score1 = Game.font.render(str(me.score),True,Color.white)
            score2 = Game.font.render(str(cpu.score),True,Color.white)
            Game.screen.blit(score1,[Game.width /2 - 100 , Game.height /3])
            Game.screen.blit(score2,[Game.width /2 + 100 , Game.height /3])
            pygame.display.update()
            Game.clock.tick(Game.fps)

if __name__ == "__main__":
    Game.play()

