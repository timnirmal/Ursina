import time
import multiprocessing
import os

def fun(ele):
    ele ** 1000

if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool(processes=4)

    os.system('python test1.py && python test2.py')

    pool.close()
    pool.join()
    end = time.time()
    print(end - start)

"""
input_list = [1000] * 1000000
n = 250000

start_time = time.time()

pool = multiprocessing.Pool(4)
result = pool.map(func=fun, iterable=input_list, chunksize=n)
pool.close()
pool.join()

end_time = time.time()
print(end_time - start_time)
"""

"""
    start = time.time()
    pool = multiprocessing.Pool(processes=4)
    for i in range(1, 1001):
        pool.apply_async(fun, (i,))
    pool.close()
    pool.join()
    end = time.time()
    print(end - start)
"""
