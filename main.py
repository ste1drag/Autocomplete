from tkinter import *
import sys


def lexicographic_sort(lista):
    lista.sort(key=lambda x:x[0])
    return lista

def weight_sort(lista):
    lista.sort(key=lambda x:x[1],reverse=True)
    return lista

def sort_first_r(lista,r):
    lista.sort(key=lambda x:x[0][0:len(r)])

def binarna_pretraga(uzorak,lista):
    l=0
    r=len(lista)-1
    while l<=r:
        m=(r-l)/2+l
        m=int(m)
        if lista[m][0][0:len(uzorak)]==uzorak:
            return lista[m]
        elif lista[m][0][0:len(uzorak)]<uzorak:
            l=m+1
        elif lista[m][0][0:len(uzorak)]>uzorak:
            r=m-1
    return -1



f=open(sys.argv[1])

lista=[]

for linija in f:
    text=linija.split()
    if len(text)<2:
        continue
    text[0]=int(text[0])
    if len(text)>2:
        for i in range(2,len(text)):
            text[1]+=" "+text[i]
    torka=(text[1],text[0])
    lista.append(torka)

print(lista)


#s=input()
s=input()
pom_lista=lista
bin_lista=[]
lexicographic_sort(pom_lista)
x=binarna_pretraga(s,pom_lista)
while x!=-1:
    bin_lista.append(x)
    pom_lista.remove(x)
    x=binarna_pretraga(s,pom_lista)





root=Tk()

root.title("Autocomplete me")
root.geometry("700x300")
Label(root).grid(row=0,column=0)
Label(root).grid(row=0,column=1)
Label(root).grid(row=0,column=2)
Label(root).grid(row=0,column=3)
Label(root).grid(row=0,column=4)
Label(root).grid(row=0,column=5)
Label(root).grid(row=1,column=0)
Label(root).grid(row=1,column=1)
Label(root).grid(row=1,column=2)
Label(root).grid(row=1,column=3)
l1=Label(root,text="Search query:",bg="white",fg="black").grid(row=1,column=4)
Label(root).grid(row=1,column=5)
te=Entry(root,width=70)
te.grid(row=1,column=6)
Label(root).grid(row=1,column=7)
Label(root).grid(row=1,column=8)


def prikaziSugestije():
    exit()


Button(root,text='Search Google', command=prikaziSugestije).grid(row=1,column=9)
Label(root).grid(row=2,column=0)
Label(root).grid(row=2,column=1)
Label(root).grid(row=2,column=2)
Label(root).grid(row=2,column=3)
var1=IntVar()
Checkbutton(root, text="Show weights", variable=var1).grid(row=2, column=4)
root.mainloop()












