from os import walk
import time
def trouver(repertoire):
    listeFichiers = []
    for (repertoir, sousRepertoires, fichiers) in walk(repertoire):
        listeFichiers.extend(fichiers)
    return(listeFichiers)

def verifie(element):
    return ".html" in element

def check_string(liste1):
    liste=[]
    liste2=[]
    for i in range(len(liste1)):
        with open('accueil.html') as f:
            if liste1[i] in f.read():
                liste.append(liste1[i])
            else:
                liste.append(liste1[i])
    return liste,liste2

def supp(liste):
    liste=check_string(liste)[1]
    f = open("accueil.html","r")
    lines = f.readlines()
    f.close
    f = open("accueil.html","w")
    for j in range(len(lines)):
        if j<10:
            f.write(lines[j])
        else:
            for j in range(len(liste)):
                if lines[j] != liste[j] :
                    f.write(lines[j])

    f.close
def teste(liste):
    liste1=[]
    for i in range(len(liste)):
        if verifie(liste[i])==True:
            liste1.append(liste[i])
    liste=check_string(liste1)[0]
    return liste


def main():
    a=teste(trouver(".\Accueil"))
    supp(trouver("."))
    for i in range(len(a)):
        fichier = open("accueil.html", "a")
        m = '<a href="web\\' + a[i]+'">'+a[i]+"</a><br>"
        fichier.write("\n")
        fichier.write(str(m))
        fichier.close()
    

while True:
    print("30 minute")
    main()
    time.sleep(1800)

