#python 2.7.12
    
def main():
    msg = 'This is an example of word count. This is going to be great to work on python'
    #print word_count(msg)
    ids  = [1, 2, 3, 4, 5]
    names = ['Cisco', 'Intel', 'Samsung', 'Nutanix', 'Philips']

    #print zip(ids, names)
    co_dict = {}

    for my_id, name in zip(ids, names):
        co_dict[my_id] = name

    print co_dict

    my_dict = { my_id:name for my_id, name in zip(ids, names) if name != 'Philips'}
    print my_dict

    nums = [1,1,3,4,4,5,5,6,7,8,8,9,2,2]
    myset = set()
    for n in nums:
        myset.add(n)

    print myset

    mset = {n for n in nums}
    print mset

if __name__ == '__main__':
    main()
