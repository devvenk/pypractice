def combine_list(mlist1, mlist2):
    try:
        if not isinstance(mlist1, list) or not isinstance(mlist2, list):
            raise Exception('Invalid input. The function accepts only list types as an argument.')

        if len(mlist1) <= 0 or len(mlist2) <= 0:
            raise Exception('Empty lists is passed to the function.')

        if len(mlist1) != len(mlist2):
            raise Exception('Length of both the list must be equal..')

        new_list = [(x, y) for x in mlist1 for y in mlist2 if x!= y]
        
        print new_list
    except Exception as e:
        raise e

def combine_list_regular(mlist1, mlist2):
    try:
        if not isinstance(mylist1, list) or not isinstance(mlist2, list):
            raise Exception('Invalid input. The function accepts only list types as an argument.')

        if len(mlist1) <= 0 or len(mlist2) <= 0:
            raise Exception('Empty lists is passed to the function.')

        if len(mlist1) != len(mlist2):
            raise Exception('Length of both the list must be equal..')

        new_list = []

        for x in mlist1:
            for y in mlist2:
                if x != y:
                    new_list.append((x,y))
        
        print new_list
    except Exception as e:
        raise e

mlist = [1,2,3,4,5,6]
mlist1 = [11,12,13,14,15,16]

def main():
    try:
        combine_list_regular(mlist, mlist1)
    except Exception as e:
        print 'Error occurred while converting list to tuple. Error: {0}'.format(e.message)
    
if __name__ == '__main__':
    main()
