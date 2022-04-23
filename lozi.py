
import arcade
Width=300
Height=300

class Game(arcade.Window):
    def __init__(self):
        super().__init__(Width, Height, 'tamrin11')
        arcade.set_background_color(arcade.color.WHITE)
        
        self.blue=arcade.load_texture('barg.png')
        self.red=arcade.load_texture('images.png')
    def on_draw(self):
      arcade.start_render()
      j=0
      for a in range(10):
        i=0
        if a%2==0:
            for s in range(10):
                arcade.draw_lrwh_rectangle_textured(i,j+2,25,25,self.red)
                arcade.draw_lrwh_rectangle_textured(i+25,j,30,30,self.blue)
                i+=54
        elif a%2==1:
            for s in range(10):
                arcade.draw_lrwh_rectangle_textured(i,j,30,30,self.blue) 
                arcade.draw_lrwh_rectangle_textured(i+30,j+2,25,25,self.red)
                i+=54          
        j+=27
        
game=Game()
arcade.run()