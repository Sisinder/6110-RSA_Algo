print("-------Sigining Text Algorithum----------")
N=int(input("Enter the value of N: "))
e=int(input("Enter the value of decryption: "))
a=input("Enter the message: ")

        # Conversion of Text to hex to decimal

a = [a[i:i+3] for i in range(0, len(a), 3)]
print("Message in Chunks: ",a)
a = [b.encode('utf-8') for b in a]
a = [b.hex() for b in a]
print("Hexadecimal values: ",a)
#a = ['0x'+b for b in a]
a=[int(b,16) for b in a]
print("Decimal Values: ",a)

        #msg encryption
sign=[pow(b,e,N) for b in a ]
print("Signed-text: ",sign)