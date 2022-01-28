from multiprocessing import Process
import os


def loop_a():
    while 1:
        os.system("python game.py")


def loop_b():
    while 1:
        os.system("python MouseController.py")


if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()
