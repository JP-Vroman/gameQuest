

# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 2
# Video link: https://www.youtube.com/watch?v=8LRI0RLKyt0
# Player movement
# © 2019 KidsCanCode LLC / All rights reserved.

# Week of march 23 - Lore
# Modularity, Github, import as, 

import pygame as pg
from pygame.sprite import Group
# from pg.sprite import Group
import random
from settings import *
from sprites import *
'''
importing game sprites and random function
Activating sprites and random 
'''

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
'''
Creates game windown and sets the measurments
INITIALIZES game clock
'''
    def new(self):
        # start a new game
        self.all_sprites = Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ground = Platform(0, HEIGHT-40, WIDTH, 40)
        plat1 = Platform(200, 400, 150, 20)
        plat2 = Platform(150, 300, 150, 20)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        self.all_sprites.add(plat1)
        self.platforms.add(plat1)
        self.all_sprites.add(plat2)
        self.platforms.add(plat2)
        # for plat in range(1,10):
        #     plat = Platform(random.randint(0, WIDTH), random.randint(0, HEIGHT), 200, 20)
        #     self.all_sprites.add(plat)
        #     self.platforms.add(plat)
        self.run()
'''
Creates player sprite within game window
Ground is added to the program
'''

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            # print("it collided")
            self.player.vel.y = 0
            self.player.pos.y = hits[0].rect.top+1
            

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
