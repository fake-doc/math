def primes_upto(n):
    primes=[1]
    for k in range(2,n+1):
        i = 2
        isPrime=True
        while i <=k and isPrime:
            if i ==k:
                primes+=[k]
            if k%i==0:
                isPrime = False
            i+=1
