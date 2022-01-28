import threading

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # create thread
    th1 = threading.Thread(target=print_square, args=(10,))
    th2 = threading.Thread(target=print_cube, args=(10,))

    # start thread 1
    th1.start()
    # start thread 2
    th2.start()

    # wait until thread 1 is completely executed
    th1.join()
    # wait until thread 2 is completely executed
    th2.join()

    # both threads completely executed
    print("Done!")

    #print_cube(5)
    #print_square(5)
