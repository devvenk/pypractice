#python 2.7.12
# word count

def word_count(msg):
    if len(msg) <= 0:
        raise Exception('Invalid string passed.')

    wordcount = {}
    words = msg.split()
    for word in words:
        wordcount[word] = wordcount.get(word, 0) + 1

    return wordcount
    
def main():
    msg = 'This is an example of word count. This is going to be great to work on python'
    print word_count(msg)

if __name__ == '__main__':
    main()
