from threading import Thread
import multiprocessing

from ursina import *
import mediapipe
import cv2

spd = 0.1

app = Ursina()

player = Entity(model='cube', scale=2, color=color.red)


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
        ret, img = cap.read()

        cv2.imshow('frame', img)  # Show the frame
        rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
            break


cap = cv2.VideoCapture(0)

# thread
# t1 = Thread(target=run_game)
# t2 = Thread(target=run_cv)


if __name__ == '__main__':
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    app.run()


    #p1 = multiprocessing.Process(target=run_game)
    p2 = multiprocessing.Process(target=run_cv)

    #p1.start()
    p2.start()


    p2.join()

    # run_cv()
    # run_game()

    # cv2.imshow('frame', img)  # Show the frame
    # app.run()

    cap.release()
    cv2.destroyAllWindows()


