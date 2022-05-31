import pygame as pg
from random import randint, choice
from time import perf_counter

pg.init()
running = True
speed = 1
window = pg.display.set_mode((800, 600))
Grave = []
alive = [True]
health = [0]
class Object:
    def __init__(self, x, y, img, canvas, otype, contacts=[], xc="None", yc="None"):
        self.x = x
        self.y = y
        self.img = img
        self.canvas = canvas
        self.eliminated = False
        self.otype = otype

        if not (xc == "None" and yc == "None"): 
            self.xc = xc
            self.yc = yc
            def movement(self):
                self.x += self.xc
                self.y += self.yc
            self.movement = lambda: movement(self)

    def draw(self):
        self.canvas.blit(self.img, (self.x, self.y))
    
    def elimination(self):
        self.eliminated = True
        index = self.otype.list.index(self)
        self.otype.list.pop(index)
        Grave.append(self)


class Player(Object):
    def __init__(self, x, y, xc, yc, img, canvas, contacts, health, vulnerability):
        super().__init__(x, y, img, canvas, Player, contacts, xc, yc)
        self.contacts = contacts
        self.alive = True
        self.health = health
        self.lastDamage = 0
    def contact(self, alive):
        for contact in self.contacts[0]:
            for object in contact.list:
                if ((self.x - 30) < object.x < (self.x + 30)) and ((self.y - 30) < object.y < (self.y + 30)):
                    object.elimination()
                    if object.otype == Food:
                        self.health += object.benefit
                        print("your medican health is ", self.health)
        for contact in self.contacts[1]:
            for object in contact.list:
                if ((self.x - 30) < object.x < (self.x +30)) and ((self.y - 30) < object.y < (self.y + 30)):
                    self.damage(object)
    def damage(self, attacker):
        if attacker.lastDamage + attacker.attackSpeed < perf_counter():
            attacker.lastDamage = perf_counter()
            self.health -= attacker.attack
            print("your medical health", self.health)
            if self.health <= 0:
                self.alive = False

class Food(Object):
    def __init__(self, x, y, img, canvas):
        super().__init__(x, y, img, canvas, Food)
        self.type = randint(1, 6)
        self.benefit = (1/3) * self.type


class Enemy(Object):
    def __init__(self, x, y, img, canvas, attackSpeed):
        super().__init__(x, y, img, canvas, Enemy)
        self.speed = randint(1, 6) / 10
        self.attack = self.speed
        self.attackSpeed = attackSpeed
        self.lastDamage = 0
        self.type = choice("singleDirectional", "multiDirectional", "shooters")
        if self.type == "multiDirectional":
            def move(self):
                if gerlie.x > self.x:
                    self.x += self.speed
                else:
                    self.x -= self.speed
                if gerlie.y > self.y:
                    self.y += self.speed
                else:
                    self.y -= self.speed
        elif self.type == "singleDirectional":
            def move(self):
                if gerlie.x > self.x:
                    self.x += self.speed
                elif gerlie.x < self.x:
                    self.x -= self.speed
                elif gerlie.y > self.y:
                    self.y += self.speed
                else:
                    self.y -= self.speed


class Wall(Object):
    def __init__(self, x, y, img, canvas, type, attackSpeed, direction=None):
        super().__init__(x, y, img, canvas, Wall)
        self.initial_x = x
        self.initial_y = y
        self.type = type
        self.attackSpeed = attackSpeed
        self.lastDamage = 0
        if type == "move":
            self.movement = randint(70, 120)
            self.speed = randint(1, 3) / 10
            self.attack = self.speed * self.movement / 10
            def move(self):
                if direction == "x":
                    self.x += self.speed
                    if ((self.initial_x - self.movement) > self.x) or (self.x > (self.initial_x + self.movement)):
                        self.speed *= -1
                if direction == "y":
                    self.y += self.speed
                    if ((self.initial_y - self.movement) > self.y) or (self.y > (self.initial_y + self.movement)):
                        self.speed *= -1
            self.move = lambda: move(self)
        else:
            self.attack = 2

Classes = [Player, Food, Enemy, Wall]
Food.list = []
Wall.list = []
Enemy.list = []

gimg = pg.image.load("C:/Users/taham/Downloads/used.png")
fimg = pg.image.load("D:/Taha/programs/python/projects/images/real_enemy.png")
gerlie = Player(100, 100, 0, 0, gimg, window, [[Food], [Wall, Enemy]], 10, 1)