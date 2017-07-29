def is_prime(num):
    #print 'checking for number {0}'.format(num)
    prime = True
    
    for i in xrange(2, num):
        #print "{0} divide {1}. {2}".format(i, num, num % i)
        
        if num % i == 0:
            prime = False
            break
    
    #print 'Number {0} = Prime: {1}'.format(num, prime)
    return prime
    
def count_primes(counter):
    if counter <= 0:
        return
    
    mycount = 0
    primes = []
    
    for n in xrange(1,500):
        #print n
        if is_prime(n): 
            #print 'Appending {0}'.format(n)
            primes.append(n)
        
        print ('Length: {0}, counter: {1}'.format(len(primes), counter))    
        if len(primes) == counter:
            break
            
    print primes

count_primes(1000)

