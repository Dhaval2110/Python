# this program is basic implementation of threading

# Global imports
import threading
from datetime import datetime


#Function calls
def print_cube(num):
    print("Cube: {}".format(num * num * num))


def print_square(num):
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating thread
    ct=datetime.now()

    t1 = threading.Thread(target=print_square, args=(100,))
    t2 = threading.Thread(target=print_cube, args=(100,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    et=datetime.now()
    print(et-ct)

    new_ct=datetime.now()
    print_square(100)
    print_cube(100)
    new_et=datetime.now()
    print(new_ct-new_et)
