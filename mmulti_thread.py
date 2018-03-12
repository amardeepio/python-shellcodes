import threading
import time


num =1



no_of_thread = 10


def print_name(x):

    print("threads %d sleeps for 8 seconds  " % x )
    time.sleep(8)

    print("threads %d started" % x)



for x in range(no_of_thread):

    thread1= threading.Thread(target=print_name ,args=(x,))
    thread1.start()