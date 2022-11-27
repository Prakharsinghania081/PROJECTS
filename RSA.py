#RSA PROJECT

import random

def prime_number_check(value , checktimes): #old code
    def expmod(b, e, m):
        def squ(x):
            return x*x
        if (e == 0): #Assert A: if e == 0 then C (return 1)
            return 1
        elif (e%2 == 0): #Assert B: if e%2 == 0 then D (squ(expmod(b,e/2,m)) % m)
            return squ(expmod(b,e/2,m)) % m
        else: #Assert C: Not A and Not B 
            return ((b%m) * expmod(b,e-1,m)) % m 

    def fermat_test(n): #x = defingin fermat test 
        a = random.randint(2,n-1) #Assert D: a is a random integer generated
        return (expmod(a,n,n) == a)

    def prime(n, q):
        failed = False #Assert E: failed = false
        while (q != 0 and (not failed)): #Assert F: while q is not equal 0 and not E 
            failed = not fermat_test(n) # Assert G: failed is not x
            q = q-1 # assert: reducing the count of q by 1 each loop 
        return (q == 0)

    return prime(value, checktimes)

#The above code has been taken directly from lecture notes and assertions are specified. 
#Now we generate random numbers and then check of the number is prime or not.  
def generate_random_prime():
    signal  = False  #initilaise signal as false 
    while (signal  == False ): #check if signal is false 
        prime_num = random.randint(0,999) #generate random numbers 
        #for fast processing, I have taken small range, you can try with bigger
        signal  = prime_number_check(prime_num ,8) #here signal can acquire true or false value    
    return prime_num
#I have macm1, hence able to run huge codes. Please reduce randint, if your system is not bulding. 

p = 0
q = 0 #initialise p and q as 0 

while(p == q):
    p = generate_random_prime() #assert: p is a random prime
    q = generate_random_prime() #assert: q is a random prime
    n = p * q #n is the product of co-prime numbers p and q. 
    r = (p-1)*(q-1) 

#egcd and extended_euclid and inv has been taken from lecture note and prof class.

def egcd(e,r): #Professor 
    while(r!=0): #assert: follow the following steps until r is equal to zero
        e,r=r,e%r #assert: when r is zero, return e 
    return e

 
def extended_euclid(m,n):  #Professor
    if n == 0: #assert: if n is zero 
        return (m,1,0)
    else:
        q = m // n #assert q is m div n
        r = m % n # assert r is m mod n 
        (g,u,v) = extended_euclid(n,r)
    return (g,v,u-q*v)

def inv(e,m):
    (g,x,y) = extended_euclid(e,m)
    if (g != 1): #assert M: if g is not 1 
        return (0) 
    else: #assert if not M 
        return(x % m)


for i in range(1,r):  # you can chnage the number if your system does not support large numbers
    if(egcd(i,r)==1):
        e=i
        if (e > 500):
            break

d = inv(e,r)
public = (e,n) #public conversion key. Will be used to encrypt messages 
private = (d,n) # private conversion key, will be used to decrypt messages  

def encrypt(pk, plaintext):    #professor 
    key, n = pk #assert n as the key specified 
    cipher = [(ord(char) ** key) % n for char in plaintext] 
    return cipher #returns cipher codes 

def decrypt(pk_1, ciphertext):    #professor 
    key, n = pk_1   
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain) #returns original word. 

User_input_statement  = "Prakhar gets extracredit"
cipher_text= encrypt(public,User_input_statement) 
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypt(private,cipher_text))

