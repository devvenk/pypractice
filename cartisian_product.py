def cartisian_product(mlist1, mlist2):
    try:
        if not isinstance(mlist1, list) or not isinstance(mlist2, list):
            raise Exception('Invalid input. The function accepts only list types as an argument.')

        if len(mlist1) <= 0 or len(mlist2) <= 0:
            raise Exception('Empty lists is passed to the function.')

        new_list = [(x, y) for x in mlist1 for y in mlist2]
        
        print new_list
    except Exception as e:
        raise e


mlist = ['a','b','c','d']
mlist1 = ['x','y','z']

def main():
    try:
        cartisian_product(mlist, mlist1)
    except Exception as e:
        print 'Error occurred while converting list to tuple. Error: {0}'.format(e.message)
    
if __name__ == '__main__':
    main()
