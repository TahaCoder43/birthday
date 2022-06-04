# make more types of emenies
# make the game playable, too many enemies, make a way to kill them, small place to move
# make an entire map
# adjust the speed issue of the game
# start adding the pictures

# have to add the alive property to the player itself
# have to add a health property which would increase as the player it foods and decrease as the player gets attacked hy
# enemies or walls
# once health property is added add enemies into the game


from functions import *


while running:
	for events in pg.event.get():
		if events.type == pg.QUIT:
			running = False
		if events.type == pg.KEYDOWN:
			if events.key in (pg.K_DOWN, pg.K_s):
				gerlie.yc = speed
			elif events.key in (pg.K_UP, pg.K_w):
				gerlie.yc = -speed
			elif events.key in (pg.K_RIGHT, pg.K_d):
				gerlie.xc = speed
			elif events.key in (pg.K_LEFT, pg.K_a):
				gerlie.xc = -speed
		if events.type == pg.KEYUP:
			if events.key in (pg.K_DOWN, pg.K_s, pg.K_UP, pg.K_w):
 				gerlie.yc = 0
			if events.key in (pg.K_RIGHT, pg.K_d, pg.K_LEFT, pg.K_a):
				gerlie.xc = 0
	if gerlie.alive:
		movement()
		spawning()
		drawing()
		Detection()
	else:
		Death()