# Decorators in python

import logging

log_file_name = 'example.log'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG)

def logger(func):
    def wrapper(*arg, **kwargs):
        logging.info('Entering function: {0}'.format(func.__name__))
        ret = func(arg, kwargs)
        logging.info('Exiting function: {0}'.format(func.__name__))
        return ret

    return wrapper

@logger
def my_function(x,y):
    print 'Hello world..'

def main():
    my_function()

if __name__ == '__main__':
    main()
