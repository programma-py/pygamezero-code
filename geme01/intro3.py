# コメント
import pgzrun

WIDTH = 500
HEIGHT = 200

alien = Actor('alien')
alien.topright = 0, 50

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
        alien.inflate(-10,-10)

def draw():
    screen.clear()
    alien.draw()

pgzrun.go()