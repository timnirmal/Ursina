import datetime as dt
from multiprocessing import Process, current_process
import sys


def f(name):
    print('{}: hello {} from {}'.format(
        dt.datetime.now(), name, current_process().name))
    sys.stdout.flush()


if __name__ == '__main__':
    worker_count = 8
    worker_pool = []
    for _ in range(worker_count):
        p = Process(target=f, args=('bob',))
        p.start()
        worker_pool.append(p)
    for p in worker_pool:
        p.join()  # Wait for all of the workers to finish.

    # Allow time to view results before program terminates.
    a = input("Finished")  # raw_input(...) in Python 2.
