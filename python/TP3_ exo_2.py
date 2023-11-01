##for n in range(10):
##    print("bonjour",n+1)

##som=0
##for p in range(1,101):
##    som+= p**2
##print(som)

##som=0
##for p in range(64):
##    som+= 2**p
##print(som)

a= int(input("entrez un entier 1"))
b=int(input("entrez un entier 3"))
som=0
if a>b:
    for p in range(b,a+1):
        som+= p**3    
else:
     for p in range(a,b+1):
         som+= p**3   
print("la somme des cubes des entiers compris entre 1 et 3",som)
    
