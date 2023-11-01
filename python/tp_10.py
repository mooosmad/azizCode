##EXO1
##1
def calcul(x0, y0, i, j):
    
    y= y0 - j
    x= x0 - i

    result = abs(x0-i)+abs(y0- j)
    return result

##2
def affiche(x):
    if x==0:
        print("bravo")
    elif x==-1:
        print("paresseux")
    elif x==1:
        print("c'est chaud")
    elif x==2:
        print("c'est tiède")
    
    elif x==3:
        print("c'est froid")

    else:
        print("c'est très froid")





##3

def saisie(x0,y0):
     ligne= 0
     v=int(input("saisir une ligne (ou '-1'pour abandonner):"))
     if ligne!= v:
          print("colonne")
     else:
         print("-1")

     if ligne_colonne= v:
         return v
     else:
         return calcul( x0, y0, ligne , colonne)
         

    

   
    
