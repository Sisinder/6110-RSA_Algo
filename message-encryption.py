print("-------Message Encryption Algorithum----------")
N=int(input("Enter the value of N: "))
e=int(input("Enter the value of encryption"))
a=input("Enter the message ")

        # Conversion of Text to hex to decimal

a = [a[i:i+3] for i in range(0, len(a), 3)]
print(a)
a = [b.encode('utf-8') for b in a]
a = [b.hex() for b in a]
print(a)
#a = ['0x'+b for b in a]
print(a)
a=[int(b,16) for b in a]
print(a)
print(a[1])
print(len(a))

        #msg encryption
encrypted=[pow(b,e,N) for b in a ]
print("encrypted=",encrypted)