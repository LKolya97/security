import random
def expt(b, n):
    if n==0:
        return 1
    return b*expt(b, n-1)
def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
        return r

def MillerRabin(n, s):  
    for j in range(1, s + 1):
            a = random.randint(1, n - 1)
            b = toBinary(n - 1)
            d = 1
            for i in range(len(b) - 1, -1, -1):
                x = d
                d = (d * d) % n
                if d == 1 and x != 1 and x != n - 1:
                    return True # Составное
                if b[i] == 1:
                    d = (d * a) % n
                    if d != 1:
                        return True # Составное
    return False # Простое

def simpleNum():
    alp="0123456789"
    S="1"
    i=0
    while i<12:
        S=S+str(random.randint(0,1))
        i+=1
    S=S+"1"
    num=0
    i=0
    while i<len(S):
        num=num+int(S[len(S)-1-i])*(expt(2,i))
        i+=1
    print("Проверяем число ", num)
    f=open('numbers.txt','r')
    symb=f.read(1)
    S=""
    while symb:
     if alp.find(symb)!=-1:
        S=S+symb
     elif S!="":
        a=num%int(S)
        if a==0:
            return 0
        S=""
     symb=f.read(1)  
    f.close()
    i=0
    while i<5:
       if MillerRabin(num, 16)==True:
           print(-1)
       i+=1
    return num
# Используемые числа
sharedPrime=0
while sharedPrime==0:
 sharedPrime = simpleNum()#p
sharedBase = 5    # g
 
aliceSecret = 6     # a
bobSecret = 15      # b

print( "Числа, известные всем:")
print( "Известная степень: " , sharedPrime )
print( "Известная база:  " , sharedBase )
 
# Алиса посылает Бобу A = g^a mod p
A = (sharedBase**aliceSecret) % sharedPrime
print( "Алиса посылает в открытый канал: " , A )
 
# Боб посылает Алисе B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print( "Боб посылает в открытый канал: ", B )

print( "Вычисленный секретный код:" )
# Алиса высчитывает секрет: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print( "Секрет, высчитанный Алисой: ", aliceSharedSecret )
 
# Боб высчитывает секрет: s = A^b mod p
bobSharedSecret = (A**bobSecret) % sharedPrime
print( "Секрет, высчитанный Бобом: ", bobSharedSecret )


