import threading
import MySQLdb

from time import sleep

def print_num():
    global dead
    print 'print_num'
    j = 0
    for i in xrange(100):
        j = j + i
    print threading.current_thread()

    print j
    
    print 'Thread executing'
    while(dead):
        print 'Thread executing..'

def main():
    global dead 
    dead = False
    mythread = threading.Thread(target=print_num)
    mythread.start()

    print mythread.is_alive()
    # print threading.active_count()
    # print threading.enumerate()
    # print threading.current_thread()
    sleep(10)
    dead = True
    print mythread.is_alive()


if __name__ == '__main__':
    main()
