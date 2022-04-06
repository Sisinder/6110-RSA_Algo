print("-------Values Generation Algorithum----------")
import random
import textwrap
def prime(number):
    if number > 1:
    
        # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (number % i) == 0:
                return(0)
        else:
            return(1)
    
    else:
        return(0)


#greatest common division 
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


#Extended Euclidean Algorithm
def Euclidean(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = Euclidean(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)
 
#Multiplicative Inverse
def decrypt(e,phi):
    gcd,s,_=Euclidean(e,phi)
    if(gcd!=1):
        return None
    else:
        
        return s%phi


option=int(input("press 1 for new encryption \npress 2 for old encryption  \n option: "))

if(option==2):
    p= int(input("Enter a prime number for p : "))
    if prime(p)==1:
        q= int(input("Enter a prime number for q : "))
        if prime(q)==1:
            N= p*q
            print("Value of N = ",N)
            phi= (p-1)*(q-1)
            print("Value of phi(N) = ",phi)
            e=int(input("enter the encryption value :"))
            if(gcd(e,phi)==1):
                print("enter")
                        
        else:
            print("only one is prime")
    else:
        print("none is prime")
elif(option==1):
    i=0
    for j in range(100):
        if i==0:
            num=random.randint(65536,262144)
            if prime(num)==1:
                i=1
                p=num
                break
    print("p=",p)
    i=0
    for j in range(100):
        if i==0:
            num=random.randint(65536,262144)
            if num != p:
                if prime(num)==1:
                    i=1
                    q=num  
                    break 
    print("q=",q)
    N= p*q
    print("Value of N = ",N)
    phi= (p-1)*(q-1)
    print("Value of phi(N) = ",phi)
    for j in range(100):
        en=random.randint(2,phi)
        if gcd(en,phi)==1:
            e=en
            break
    print("e= ",e)


        #for d value
d=decrypt(e,phi)
print("d= ",d)