print("-------Orginal Text Algorithum----------")


N=int(input("Enter the value of N: "))
d=int(input("Enter the value of Encryption:"))
c=input("enter the Sigined text: ")
    


arr = c.split(", ") 
arr = list(map(int,arr))

dcryption=[pow(b,d,N) for b in arr ]

he=[hex(a) for a in dcryption]
print("decimal to hexa = ",he)
deci = [temp[2:] for temp in he]
org= [bytes.fromhex(temp).decode("utf-8") for temp in deci]
print("hexadecimal to text = ",org) 
s = "".join(org)
print("orginal text = ",s)
