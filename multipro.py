from multiprocessing import Process, Pipe
import os


def loop_a():
    while 1:
        os.system("python game.py")


def loop_b():
    while 1:
        parent_conn, child_conn = Pipe()
        p = Process(target=f, args=(child_conn,))
        p.start()
        print(parent_conn.recv())  # prints "Hello"
        os.system("python MouseController.py")


if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()
