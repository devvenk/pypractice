import threading
import re

class Message(object):
    def __init__(self, priority, message):
        self.priority = priority
        self.message = message

messages = []

def producer_thread1():
    #global lock
    #lock.acquire()

    try:
        for i in xrange(0, 50000):
            msg = Message(i, 'Log Alert {0}'.format(i))
            messages.append(msg)
    finally: pass
        #lock.release()
    print 'Producer 1 ended..'

def producer_thread2():
    #global lock
    #lock.acquire()

    try:
        for i in xrange(50000, 100000):
            msg = Message(i, 'Log Alert {0}'.format(i))
            messages.append(msg)
    finally: pass
        #lock.release()
    print 'Producer 2 ended..'

def consumer_thread():
    #global lock
    #lock.acquire()

    try:
        f = open('results.txt','a+')
        for msg in messages:
            f.write('Priority: {0}, Message: {1}\n'.format(msg.priority, msg.message))
        messages[:] = []
        f.close()
    finally: pass
        #lock.release()

    print 'Consumer 1 ended..'

def read_file():

    with open('results.txt','r') as f:
        for message in f:
            print '{0}'.format(message)

def parse_file():
    pg = re.compile(r'\d{1,5}')
    numbers = []
    with open('results.txt','r') as f:
        for message in f:
            val = pg.findall(message)
            for v in val:
                numbers.append(v)

    #print numbers
    print len(numbers)

def parse_log(log_file_name = 'sample_log.txt'):

    #error_log = open('errorLog.txt','w')

    pg = re.compile(r'Error\s*Code:\s\d{1}')
    #pg = re.compile(r'wwn-pool')
    with open(log_file_name, 'r') as f:
        for message in f:
            val = pg.search(message)
            if(val): 
                #print message
                #error_log.write(message)
                print '{0}'.format(val.group(0))
    #error_log.close()

def main():
    #global lock
    #lock = threading.Lock()

    p1 = threading.Thread(target=producer_thread1)
    p2 = threading.Thread(target=producer_thread2)
    c1 = threading.Thread(target=consumer_thread)

    p1.start()
    p2.start()
    c1.start()
    p1.join()
    p2.join()
    c1.join()
    # read_file()
    parse_file()
    # parse_log()

    import os
    os.remove('results.txt')

if __name__ == '__main__':
    main()

