import threading
import time

def producer_thread():
    global exit_event

    while(True):
        print 'Waiting for exit event..'
        exit_event.wait(10)
        
def consumer_thread():
    global exit_event

    while(True):
        print 'Waiting for exit event..'
        exit_event.wait(10)

def main():
    t1 = threading.Thread()
if __name__ == '__main__':
    main()