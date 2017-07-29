#python 2.7.12

def convert_to_tuple(mylist):

    try:
        if not isinstance(mylist, list):
            raise Exception('Invalid input. The function accepts only list type as an argument.')

        if len(mylist) <= 0:
            raise Exception('Empty list is passed to the function.')

        count = len(mylist)
        new_list = []
        for item in xrange(0, count, 2):
            new_list.append((item, item+1))
        
        print new_list
    except Exception as e:
        raise e

def convert_to_tuple_list_comp(mylist):

    try:
        if not isinstance(mylist, list):
            raise Exception('Invalid input. The function accepts only list type as an argument.')

        if len(mylist) <= 0:
            raise Exception('Empty list is passed to the function.')

        count = len(mylist)
        new_list = [ (item, item+1) for item in xrange(1, count, 2)]
        
        print new_list
    except Exception as e:
        raise e
        
mlist = [1,2,3,4,5,6]

def main():
    try:
        convert_to_tuple_list_comp(mlist)
    except Exception as e:
        print 'Error occurred while converting list to tuple. Error: {0}'.format(e.message)
    
if __name__ == '__main__':
    main()