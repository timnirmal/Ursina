import multiprocessing
from ursina import *
import mediapipe
import cv2
import pyautogui

spd = 0.1

app = Ursina()

player = Entity(model='cube', scale=2, color=color.red)

cap = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands()
mpDraw = mediapipe.solutions.drawing_utils  # For drawing landmarks

id8_positions = []
id4_positions = []
id12_positions = []
position_list = []

def update():
    player.x += held_keys['d'] * 0.1
    player.x -= held_keys['a'] * 0.1
    player.y += held_keys['e'] * 0.1
    player.y -= held_keys['q'] * 0.1
    player.z += held_keys['w'] * 0.1
    player.z -= held_keys['s'] * 0.1

    player.rotation_x += held_keys['r'] * 5
    player.rotation_y += held_keys['f'] * 5
    player.rotation_z += held_keys['t'] * 5


def run_game():
    while True:
        print('running')


def run_cv():
    while True:
        print('running')


if __name__ == '__main__':

    p2 = multiprocessing.Process(target=run_cv)
    p2.start()
    p2.join()

    print('done')
    app.run()

    cap.release()
    cv2.destroyAllWindows()
