from tkinter import *
import sys
import webbrowser


import numpy as np

def rastojanje(A,B):
    n = len(A)
    m = len(B)
    matrix = np.zeros((n + 1, m + 1))
    for i in range(n + 1):
        matrix[i][0] = i
    for j in range(m + 1):
        matrix[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x = matrix[i - 1][j] + 1
            y = matrix[i][j - 1] + 1
            if A[i - 1] == B[j - 1]:
                z = matrix[i - 1][j - 1]
            else:
                z = matrix[i - 1][j - 1] + 1
            matrix[i][j] = min(x, y, z)
    return int(matrix[n][m])

def lexicographic_sort(lista):
    lista.sort(key=lambda x:x[0])
    return lista

def weight_sort(lista):
    lista.sort(key=lambda x:x[1],reverse=True)
    return lista

def sort_first_r(lista,r):
    lista.sort(key=lambda x:x[0][0:r])

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




f=open(sys.argv[1],encoding="utf-8")


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




#s=input()


n1=sys.argv[2]
br=int(n1)





root=Tk()

root.title("Autocomplete me")
root.geometry("700x300")
Label(root).grid(row=0,column=0)
Label(root).grid(row=0,column=1)
Label(root).grid(row=0,column=2)
Label(root).grid(row=0,column=3)
Label(root).grid(row=0,column=4)
Label(root).grid(row=0,column=5)
Label(root).grid(row=0,column=6)
Label(root).grid(row=0,column=7)
Label(root).grid(row=0,column=8)
Label(root).grid(row=1,column=0)
Label(root).grid(row=1,column=1)
Label(root).grid(row=1,column=2)
Label(root).grid(row=1,column=3)
l1=Label(root,text="Search query:",bg="white",fg="black").grid(row=1,column=4)

sv=StringVar()


def callback(sv,lista,br):
    a=sv.get().strip()
    pom_lista = lista[:]
    bin_lista = []
    lexicographic_sort(pom_lista)
    x = binarna_pretraga(a, pom_lista)
    while x != -1:
        bin_lista.append(x)
        pom_lista.remove(x)
        x = binarna_pretraga(a, pom_lista)

    #if len(bin_lista) == 0:
     #   for el in lista:
      #      if rastojanje(el[0][0:len(a)], a) < 2:
       #         bin_lista.append(el)

    i = 0
    l = Listbox(root, width=40)
    l.grid(row=2, column=5)
    weight_sort(bin_lista)
    if len(bin_lista) == 0 or len(a) == 0:
        l.delete(0, END)


    else:
        for list in bin_lista:
            if i == br:
                break
            if var1.get()==1:
                l.insert(END,list[0]+" "+str(list[1]).rjust(50))
            else:
                l.insert(END,list[0])
            i += 1

    def CurSelet(evt):
        try:
            value = str((l.get(l.curselection())))
            pom=""
            for c in value:
                if not c.isdecimal():
                    pom+=c
            sv.set(pom)
        except(TclError):
            pass




    l.bind('<<ListboxSelect>>', CurSelet)



te = Entry(root, textvariable=sv, width=40)

def Klik():
    webbrowser.open("www.google.com/search?q=" + te.get())

Button(root, text='Search Google', command=Klik).grid(row=1, column=8)






lexicographic_sort(lista)


sv.trace("w", lambda name, index, mode, sv=sv: callback(sv,lista,br))

te.grid(row=1,column=5)
Label(root).grid(row=1,column=6)
Label(root).grid(row=1,column=7)






Label(root).grid(row=2,column=0)
Label(root).grid(row=2,column=1)
Label(root).grid(row=2,column=2)
var1=IntVar()
Checkbutton(root, text="Show weights", variable=var1).grid(row=6, column=3)
Label(root).grid(row=7,column=3)
Label(root).grid(row=8,column=3)
Label(root).grid(row=9,column=3)
Label(root).grid(row=10,column=3)
Label(root).grid(row=11,column=3)





root.mainloop()











