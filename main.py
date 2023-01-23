from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import googletrans
from googletrans import *

root = Tk()
root.title("Translang")
root.geometry('1080x400')

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    text_ = text1.get(1.0,END)
    t1 = Translator()
    trans_text = t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)

image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

imagelogo= PhotoImage(file="icon1.png")
logo_img = Label(root,image=imagelogo,height=50,width=600)
logo_img.place(x=290,y=335)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()


combo1 = ttk.Combobox(root,values=languageV,font="Candara",state='r')
combo1.place(x=110, y=20)
combo1.set("English")

label1=Label(root,text='English',font='Verdana',bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=110, y=50)


f = Frame(root,bg="#CBFFFD",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1= Text(f,font='Candara',bg="#EDF1F1",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1 =Scrollbar(f)
scrollbar1.pack(side="right",fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



combo2 = ttk.Combobox(root,values=languageV,font='Candara', state='r')
combo2.place(x=730, y=20)
combo2.set("Select Language")

label2=Label(root,text='English',font='Verdana',bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=730, y=50)

f1 = Frame(root,bg="#CBFFFD",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2 = Text(f1,font='Candara',bg="#EDF1F1",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2 =Scrollbar(f1)
scrollbar2.pack(side="right",fill='y')
scrollbar2.configure(command=text1.yview)
text2.configure(yscrollcommand=scrollbar2.set)


translate=Button(root,text="TRANSLATE",font="Candara", activebackground="purple",cursor='hand2',bd=5,bg='#5CFEB5',fg="#F9D828",command=translate_now)
translate.place(x=475,y=250)


label_change()

root.configure(bg='white')
root.mainloop()