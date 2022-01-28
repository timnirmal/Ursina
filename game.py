from ursina import *


def update():
    # player.position = mouse.position
    # player.x = mouse.x
    player.x += held_keys['d'] * 0.1
    player.x -= held_keys['a'] * 0.1
    player.y += held_keys['e'] * 0.1
    player.y -= held_keys['q'] * 0.1
    player.z += held_keys['w'] * 0.1
    player.z -= held_keys['s'] * 0.1

    player.rotation_x += held_keys['r'] * 5
    player.rotation_y += held_keys['f'] * 5
    player.rotation_z += held_keys['t'] * 5

    # move player with mouse
    player.position = mouse.position
    player.x = mouse.x
    player.y = mouse.y

    # cube.rotation_x += 0.25
    # cube.rotation_y += 0.25


if __name__ == '__main__':
    app = Ursina()
    # cube = Entity(model='cube', scale=2, color=color.red)
    # player = Entity(model='cube', scale=2, color=color.green)
    player = Entity(model='Objects/dragon.obj', scale=2, color=color.green)

    app.run()
