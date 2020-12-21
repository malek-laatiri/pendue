def dead(nbreTries):
    if nbreTries == 0:
        print("              ")
    if nbreTries == 1:
        print(" _|_          ")
    if nbreTries == 2:
        print("  |           ")
        print("  |           ")
        print(" _|_          ")

    if nbreTries == 3:
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print(" _|_          ")
    if nbreTries == 4:
        print("  __          ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print(" _|_          ")
    if nbreTries == 5:
        print("  ____ __     ")
        print("  |   |       ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print(" _|_          ")
    if nbreTries == 6:
        print("  ____ __     ")
        print("  |   |       ")
        print("  |   0       ")
        print("  |           ")
        print("  |           ")
        print(" _|_          ")
    if nbreTries == 7:
        print("  ____ __     ")
        print("  |   |       ")
        print("  |   0       ")
        print("  |   |       ")
        print("  |           ")
        print(" _|_          ")
    if nbreTries == 8:
        print("  ____ __     ")
        print("  |   |       ")
        print("  |   0       ")
        print("  |  /|       ")
        print("  |           ")
        print(" _|_          ")
    if nbreTries == 9:
        print("  ____ __     ")
        print("  |   |       ")
        print("  |   0       ")
        print("  |  /|\      ")
        print("  |           ")
        print(" _|_          ")
    if nbreTries == 10:
        print("  ____ __     ")
        print("  |   |       ")
        print("  |   0       ")
        print("  |  /|\      ")
        print("  |  /        ")
        print(" _|_          ")
    if nbreTries == 11:
        print("  ____ __     ")
        print("  |   |       ")
        print("  |   0       ")
        print("  |  /|\      ")
        print("  |  / \      ")
        print(" _|_          ")

def testStr(ch):#test sur le long de chaine a chercheé
    if (len(ch)<3 or len(ch)>10):
        return False
    else:
        return True

def countStr(c,ch):#recherche le nombre de char c dans un chaine ch
    n=0
    for i in ch:
        if(c==i):
            n+=1
    return n


if __name__ == "__main__":
    nbreTries=0;
    test=False
    strGuess=[]
    strPrintGuess=""
    win=False
    ch=''
    while(test==False):
        strOriginal=input("mot=> ")
        test=testStr(strOriginal)
        if(test == False):
            print("un mot de 3 à 10 lettres")
    for i in strOriginal:
        strGuess.append(i)
        strPrintGuess+="_"
    new = list(strPrintGuess)

    print("Le jeu commence...")
    print(strPrintGuess)


    while(nbreTries<11 and win==False):
        testChoix=False
        while(testChoix==False):
            choix=input("Votre choix: ")
            if(len(choix)<0 or len(choix)>1):
                print('erreur de choix,il doit un seul caractere')
            else:
                testChoix=True

        if(choix in strGuess):
            for x in range(len(strGuess)):
                if(choix==strGuess[x]):
                    new[x]=choix
                    ''.join(new)
            print(new)
            if(countStr("_",new)==0):
                win=True
        else:
            nbreTries+=1
            dead(nbreTries)
            
    if(win):
        print("Vous avez gagné !!!")
    else:
        print("Perdu")
        print("Solution {}".format(strOriginal))


    

