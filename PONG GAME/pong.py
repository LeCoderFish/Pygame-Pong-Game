import pygame as pg
import random

class App():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1000,600))
        self.pad1=Pad(self.screen,0,pg.K_a,pg.K_d)
        self.pad2=Pad(self.screen,990,pg.K_LEFT,pg.K_RIGHT)
        self.ball=Ball(self.screen)
        
        self.font = pg.font.SysFont('Bauhaus 93', 60)
        self.score=[0,0]
        
        quit=False
        while quit==False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit=True
                self.pad2.move(event)
                self.pad1.move(event)
            self.screen.fill((0,0,0))
            
            pg.draw.line(self.screen, (50,50,50), (500,0), (500,1000),20)
            self.ball.move(self.pad1.rect,self.pad2.rect,self.score)
            self.ball.draw()
            self.pad1.draw()
            self.pad2.draw()     
            
            a=self.font.render(str(self.score[0]), True, (255,255,255))
            b=self.font.render(str(self.score[1]), True, (255,255,255))
            self.screen.blit(a,(630,50))
            self.screen.blit(b,(350,50))
            
                
            pg.display.update()                             
        
class Pad():
    def __init__(self,screen,position,up,down):
        self.up=up
        self.down=down
        self.screen=screen
        self.pos=[position,250]
        self.speed=0
        self.rect = pg.Rect(self.pos[0],self.pos[1],10,100)  
    def move(self,event):
        if event.type==pg.KEYDOWN:
            if event.key==self.up:   
                self.speed=-0.2      
            if event.key==self.down:
                self.speed=0.2
        if event.type==pg.KEYUP:
            if event.key==self.up and self.speed==-0.2:   
                self.speed=0      
            if event.key==self.down and self.speed==0.2:
                self.speed=0
                
    def draw(self):
        if self.pos[1]+self.speed>0 and self.pos[1]+self.speed<500:
            self.pos[1]=self.pos[1]+self.speed
        self.rect = pg.Rect(self.pos[0],self.pos[1],10,100)   
        pg.draw.rect(self.screen, (255,255,255), self.rect)
    
class Ball():
    def __init__(self,screen):
        self.screen=screen
        self.pos=[500,250]
        self.speed=[random.choice([0.2,-0.2]),random.choice([0.2,-0.2])]
        self.rect=pg.Rect(self.pos[0],self.pos[1],20,20)
    
        
    def move(self,pad1,pad2,score):
        if self.pos[1]<0:
            self.speed[1]=0.2
        if self.pos[1]>580:
            self.speed[1]=-0.2
        if pg.Rect.colliderect(pad1,self.rect):
            self.speed[0]=0.5
        if pg.Rect.colliderect(pad2,self.rect):
            self.speed[0]=-0.5
            
        if self.pos[0]<-1000:
            self.pos=[500,250]
            self.speed=[random.choice([0.2,-0.2]),random.choice([0.2,-0.2])]
            score[0]+=1
            
        if self.pos[0]>2000:
            self.pos=[500,250]
            self.speed=[random.choice([0.2,-0.2]),random.choice([0.2,-0.2])]
            score[1]+=1
            
        self.pos[0]=self.pos[0]+self.speed[0]
        self.pos[1]=self.pos[1]+self.speed[1]
        
        
    def draw(self):
        self.rect=pg.Rect(self.pos[0],self.pos[1],20,20)
        pg.draw.rect(self.screen, (255,255,255), ((self.pos),(20,20)))
        
App()

