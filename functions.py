from objects import *

def Death():
    global window
    window.fill("#000000")
    window.blit(fimg, (350, 250))
    pg.display.update()
    print('comes in this function')

def movement():
    gerlie.movement()
    for wall in Wall.list:
        if wall.type == "move":
            wall.move()
    for enemy in Enemy.list:
        enemy.move()

def drawing():
    window.fill("#00ff7f")
    for Class in Classes[1:]:
        for object in Class.list:
            object.draw()
    gerlie.draw()
    pg.display.update()

def spawning():
    time = round(perf_counter(), 0)
    # Food
    if time % 5 == 0 and time != spawning.lastTimes[0]:
        x = randint(50, 750)
        y = randint(50, 550)
        Food.list.append(
            Food(x, y, fimg, window)
        )
        print("this food will give you", Food.list[-1].benefit, "health")
        spawning.lastTimes[0] = time
    # Wall
    if time % 10 == 0 and time != spawning.lastTimes[1]:
        print("A wall has spawned")
        x = randint(100, 700)
        y = randint(100, 500)
        Wall.list.append(
            Wall(x, y, fimg, window, choice(["move", "stand"]), randint(1, 3), choice("xy"))
        )
        print("This wall's damage is", Wall.list[-1].attack)
        spawning.lastTimes[1] = time
    #Enemy
    if time % 5 == 0 and time != spawning.lastTimes[2]:
        x = randint(50, 750)
        y = randint(50, 550)
        Enemy.list.append(
            Enemy(x, y, fimg, window, randint(1, 3))
        )
        # print("this food will give you", Food.list[-1].benefit, "health")
        spawning.lastTimes[2] = time

def Detection():
    gerlie.contact(alive)

spawning.lastTimes = [0, 0, 0]