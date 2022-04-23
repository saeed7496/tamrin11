
import arcade
import random
import time
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITTEL='snak game'
class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__('apple.jpg')
        self.width=25
        self.height=25
        self.center_x=random.randint(50, SCREEN_WIDTH-50)
        self.center_y=random.randint(50, SCREEN_HEIGHT-50)
    
class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color=arcade.color.BARBIE_PINK
        self.width=15
        self.height=15   
        self.center_x=400
        self.center_y=300
        self.change_x=1
        self.change_y=0
        self.speed=2
        self.body=[]
        self.size=14
    def draw(self):
        for i in range(len(self.body)):
            arcade.draw_circle_filled(self.body[i][0],self.body[i][1],5,self.color)
    
    def eat(self,e):
        if e=='apple':
            self.size+=1
            self.speed+=0.015
            self.body.append([self.center_x,self.center_y])
        elif e=='pear':
            self.size+=2
            self.speed+=0.015
            for j in range(2):
                self.body.append([self.center_x,self.center_y])
        elif e=='pue':
            self.speed+=0.2
            

    def move(self):
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed
        self.body.append([self.center_x,self.center_y])
        if len(self.body)>self.size:
            self.body.pop(0)
class Pue(arcade.Sprite):
    def __init__(self):
        super().__init__('Poop-emoji.jpg')
        self.width=25
        self.height=25
        self.center_x=random.randint(50,SCREEN_WIDTH-50)
        self.center_y=random.randint(50,SCREEN_HEIGHT-50)

class Pear(arcade.Sprite):
        def __init__(self):
            super().__init__('pear.jpg')
            self.width=25
            self.height=25
            self.center_x=random.randint(50, SCREEN_WIDTH-50)
            self.center_y=random.randint(50, SCREEN_HEIGHT-50)

class Score(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.number=1
        self.record=1
    def draw(self):
        arcade.draw_text('record: '+str(self.record),SCREEN_WIDTH-100,SCREEN_HEIGHT-20,arcade.color.BLACK,10)
        arcade.draw_text('score: '+str(self.number),SCREEN_WIDTH/100,SCREEN_HEIGHT-20,arcade.color.BLACK,10)
class GameOver(arcade.Sprite):
    def __init__(self):
        super().__init__()
    def draw(self):
        arcade.draw_text('GAME OVER',250,250,arcade.color.RED,40)
        arcade.exit()

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITTEL)
        self.background_image=arcade.load_texture(':resources:images/tiles/water.png')
        self.gameover_flag=0
        self.t1=time.time()
        self.t_pue=time.time()
        self.t_pear=time.time()
        self.snake=Snake()
        self.apple=Apple()
        self.pue=Pue()
        self.pear=Pear()
        self.score=Score()
        self.gameover=GameOver()
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background_image)
        if SCREEN_WIDTH<self.snake.center_x or self.snake.center_x<0 or  SCREEN_HEIGHT<self.snake.center_y or self.snake.center_y<0 or self.gameover_flag==1:
            self.gameover.draw()
        self.apple.draw()
        self.pue.draw()
        self.pear.draw()
        self.snake.draw()
        self.score.draw()
    def on_update(self, delta_time: float):
        self.snake.move()
        self.t2=time.time()
        if self.t2 - self.t1 >10:
            self.apple=Apple()
            self.t1=time.time()
        if self.t2 - self.t_pue>9:
            self.pue=Pue()
            self.t_pue=time.time()
        if self.t2 - self.t_pear >12:
            self.pear=Pear()
            self.t_pear=time.time()
        
        if arcade.check_for_collision(self.apple,self.snake):
            self.snake.eat('apple')
            self.score.number+=1
            self.apple=Apple()
       
        if arcade.check_for_collision(self.pue,self.snake):
            self.snake.eat('pue')
            self.score.number-=1
            self.pue=Pue()
        if arcade.check_for_collision(self.pear,self.snake):
            self.snake.eat('pear')
            self.score.number+=2
            self.pear=Pear()

        if self.score.number>self.score.record:
            self.score.record=self.score.number
        
        if self.score.number==0:
            self.gameover_flag=1

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0
        elif symbol==arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
        elif symbol==arcade.key.UP:
            self.snake.change_y=1
            self.snake.change_x=0
        elif symbol==arcade.key.DOWN:
            self.snake.change_y=-1
            self.snake.change_x=0
s=Game()
arcade.run()