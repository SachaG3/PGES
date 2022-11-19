from tkinter import * 
import urllib.request
fenetre = Tk()

fenetre.title("téléchargement")
fenetre.geometry("500x300")
label_title=Label(fenetre,text='Téléchargement vidéo',fg="black")
label_title.pack()

def lancer():
    print(a.get())
    print(b.get())
    print(c.get())
    for i in range(b.get()):
        if i<9:
            print(a.get()+'0'+str(i+1)+'.mp4',c.get()+'0'+str(i+1)+'mp4')
            urllib.request.urlretrieve(a.get()+'0'+str(i+1)+'.mp4',c.get()+'0'+str(i+1)+'.mp4')
        else :
            urllib.request.urlretrieve(a.get()+str(i+1)+'.mp4',c.get()+str(i+1)+'.mp4')
        

a=StringVar()
label=Label(fenetre,text="le lien sans l'épisode et le .mp4")
label.pack()
entree=Entry(fenetre,textvariable=a)
entree.pack()

b=IntVar()
label2=Label(fenetre,text="Entrée une valeur")
label2.pack()
entree2=Entry(fenetre,textvariable=b)
entree2.pack()

c=StringVar()
label3=Label(fenetre,text="Nom + S?? + EP ")
label3.pack()
entree3=Entry(fenetre,textvariable=c)
entree3.pack()

bouton = Button(fenetre,text="valider",command=lancer)
bouton.pack()



#bouton = Button(fenetre,text="valider",command=function)
#urllib.request.urlretrieve("http://86.236.221.156/Platinum%20End/S1/Platinum%20End%20S1E02.mp4","test.mp4")

