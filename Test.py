import math
import random

def fermat_primality_test(num, max_iter):
    random.seed()
    for i in range(0,max_iter):
        a = random.randint(2,num-1)
        print('a=',a,end=' ')
        print('gcd=',math.gcd(a,num),end=' ')
        print('pow(a,num-1,num)= ',pow(a,num-1,num),end=' ')
        if math.gcd(a,num) > 1:
            print("Not coprime")
            return False
        elif pow(a,num-1,num) != 1:
            print("Not prime")
            return False
        print();
    return True
   
##num = int(input("num: " ))
##max_iter = int(input("max-iter: "))


def generate_prime():
    notPrime = 1
    num_bits = int(input("num_bits: " ))
    while notPrime:
        n=num_bits//2
        num = random.getrandbits(n)
        print(num)
        notPrime = int(input("NP: " ))
##        if fermat_primality_test(num, 5):
##            return num
##    print("TODO: must be completed")


generate_prime()
##num_bits = int(input("num_bits: " ))
##print("Got prime:",generate_prime(num_bits))

