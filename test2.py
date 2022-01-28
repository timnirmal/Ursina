from multiprocessing import Process, Queue, Pipe
from time import sleep

from test1 import f

if __name__ == '__main__':
    while True:
        parent_conn, child_conn = Pipe()
        p = Process(target=f, args=(child_conn,))
        p.start()
        print(parent_conn.recv())  # prints "Hello"
        # print("Parent")
        sleep(1)
