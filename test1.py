from multiprocessing import Process, Pipe
from time import sleep


def f(child_conn):
    while True:
        msg = "Hello"
        child_conn.send(msg)
        # child_conn.close()
        # print("Parent is waiting for child to send message")
        sleep(1)