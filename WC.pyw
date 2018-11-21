from tkinter import *
import tkinter.ttk as ttk
import time
import random
import os
from tkinter import filedialog as fd
import sys


window=Tk()

window.iconbitmap("C:\Windows\System32\certutil.exe")
window.title("Окно")
c2=Canvas(window,width=1212121,height=1221212121)
c2.pack()
window.geometry("470x500")

name=os.name

if name!="nt":
    wind=Tk()
    wind.title("Окно")
    l=Label(wind,text="ВНИМАНИЕ! Этот продукт написан под windows и некоторые фишки могут не поддерживаться на других системах (Mac os, Linux)",font="Bold 10")
    l.pack()

win=Tk()
win.iconbitmap("C:\Windows\System32\cmmon32.exe")
win.resizable(width="false",height="false")
win.geometry("550x500")
win.config(bg="#ceddff")
win.title("window creator")

ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")

c=Canvas(win,width=12121,height=21212121)

def red():
    c2.config(bg="red")
def blue():
    c2.config(bg="blue")
def green():
    c2.config(bg="green")
def yellow():
    c2.config(bg="yellow")
def skyblue():
    c2.config(bg="skyblue")
def purple():
    c2.config(bg="purple")

def reset():
    c2.config(bg="#f0eff0")

def custom():
    again=Tk()
    again.title("Ввести hex")
    again.iconbitmap("C:\Windows\System32\certutil.exe")
    again.resizable(width="false",height="false")
    again.geometry("167x27")

    cc=Canvas(width=80,height=1)
    tex=Text(again,width=20,height=1)
    tex.place(x=1,y=1)

    def smth():
        result=tex.get("1.0",END+'-1c')
        c2.config(bg=result)

    btn=Button(again,text="Задать цвет",command=smth)
    btn.place(x=90,y=1)


m=Menu(win)
win.config(menu=m)


def aboutproject():
     about=Tk()
     about.geometry("300x320")
     about.title("О программе")
     about.iconbitmap("C:\Windows\System32\certutil.exe")

     about.resizable(width="false",height="false")

     lab1=Label(about,text="Window",font="Bold 15")
     lab1.place(x=65,y=5)

     lab2=Label(about,text="Creator",font="Bold 15")
     lab2.place(x=145,y=30)

     ver=Label(about,text="Версия 1.0",font="Italic 10")
     ver.place(x=100,y=100)

     dev=Label(about,text="Разработчик: @root011")
     dev.place(x=100,y=150)

     con=Label(about,text="Связь:",font="Bold 20")
     con.place(x=100,y=200)

     vk=Label(about,text="vk.com/simple_vasya")
     instagram=Label(about,text="instagram.com/root011")
     telegram=Label(about,text="t.me/root011")

     vk.place(x=100,y=250)
     instagram.place(x=100,y=270)
     telegram.place(x=100,y=290)

def donate():
    d=Tk()
    d.geometry("700x30")
    d.resizable(width="false",height="false")
    lol=Label(d,text="Номер телефона: 89223048855, вк - vk.com/simple_vasya. Большое спасибо!")
    lol.pack()
    d.title("Поддержка")
    d.iconbitmap("C:\Windows\System32\cmmon32.exe")


color=Menu(win,tearoff=0)
subsize1=Menu(win,tearoff=0)

def exx(event):
    window.destroy()
    win.destroy()
    sys.exit()

def ex():
    window.destroy()
    win.destroy()
    sys.exit()


customm=Menu(m,tearoff=0)
over=Menu(customm,tearoff=0)
sm=Menu(m,tearoff=0)


other=Menu(sm,tearoff=0)
sm.add_cascade(label="Рамка",menu=over)

m.add_cascade(label="☼",menu=other)
other.add_command(label="О программе",command=aboutproject)
other.add_command(label="Поддержать разработчика",command=donate)
other.add_separator()
other.add_command(label="Выйти                                     Ctrl+E",command=ex)

m.add_cascade(label="Окно",menu=sm)

win.bind("<Control-e>",exx)

def reboot():
    window.destroy()
    window=Tk()

sm.add_cascade(label="Цвет окна", menu=color)
sm.add_cascade(label="Изменить размер окна",menu=subsize1)
sm.add_command(label="Удалить всё с окна",command=reboot)


def w100():
    w=100
    window.geometry("100x100")

def w200():
    w=100
    window.geometry("200x200")

def w300():
    w=100
    window.geometry("300x300")

def w400():
    w=100
    window.geometry("400x400")

def w500():
    w=100
    window.geometry("500x500")

def w600():
    w=100
    window.geometry("600x600")

def w700():
    w=100
    window.geometry("700x700")

def w800():
    w=100
    window.geometry("800x800")

def w900():
    w=100
    window.geometry("900x900")

def w1000():
    w=100
    window.geometry("1000x1000")

def w1100():
    w=100
    window.geometry("1100x1100")


subsize1.add_command(label="100x100   ",command=w100)
subsize1.add_command(label="200x200   ",command=w200)
subsize1.add_command(label="300x300   ",command=w300)
subsize1.add_command(label="400x400   ",command=w400)
subsize1.add_command(label="500x500   ",command=w500)
subsize1.add_command(label="600x600   ",command=w600)
subsize1.add_command(label="700x700   ",command=w700)
subsize1.add_command(label="800x800   ",command=w800)
subsize1.add_command(label="900x900   ",command=w900)
subsize1.add_command(label="1000x1000 ",command=w1000)
subsize1.add_command(label="1100x1100 ",command=w1100)

def title():
    d=Tk()
    d.title("Настройка заголовка")
    d.geometry("370x40")
    d.resizable(width="false",height="false")
    tit=Text(d,width=30,height=1)
    tit.place(x=0,y=0)

    factory=Label(d,text="Нажмите сюда и введите название для заголовка окна",foreground="gray")
    factory.place(x=0,y=0)

    def func(event):
        factory.place(x=232323, y=102002)
    factory.bind('<Button-1>',func)


    def activity():
        result=tit.get("1.0",END+'-1c')
        window.title(result)

    btn=Button(d,text="Установить",command=activity)
    btn.place(x=275,y=0)


def icon():
    ico=fd.askopenfilename()
    window.iconbitmap(ico)

def resize_width():
    window.resizable(width="false",height="true")
def resize_height():
    window.resizable(width="true",height="false")
def resize():
    window.resizable(width="false",height="false")
def size():
    window.resizable(width="true",height="true")

def overwritedirect():
    window.overrideredirect(0)

def antioverwritedirect():
    window.overrideredirect(1)


resiz=Menu(customm,tearoff=0)


over.add_command(label="Включить рамку",command=overwritedirect)
over.add_command(label="Выключить рамку",command=antioverwritedirect)

resiz=Menu(customm,tearoff=0)

sm.add_cascade(label="Ограничение по длине/высоте окна",menu=resiz)
resiz.add_command(label="Только высота",command=resize_width)
resiz.add_command(label="Только ширина",command=resize_height)
resiz.add_command(label="Нельзя расширять",command=resize)
resiz.add_command(label="Можно изменять размер",command=size)



sm.add_command(label="Установить заголовок",command=title)
sm.add_command(label="Установить иконку",command=icon)



color.add_command(label="Красный",command=red)
color.add_command(label="Синий",command=blue)
color.add_command(label="Зелёный",command=green)
color.add_command(label="Жёлтый",command=yellow)
color.add_command(label="Небесный",command=skyblue)
color.add_command(label="Пурпурный",command=purple)
color.add_command(label="Убрать цвет",command=reset)
color.add_command(label="Шестнадцатеричное значение",command=custom)




def label():
    new=Tk()
    new.title("Создать надпись")
    new.iconbitmap("C:\Windows\System32\certutil.exe")
    ca=Canvas(new,width=600,height=600)
    ca.pack()

    new.resizable(width="false",height="false")

    ca.config(bg="#ceddff")

    labelX=Label(new,text="X:",background="#ceddff")
    labelY=Label(new,text="Y:",background="#ceddff")
    labelX.place(x=5,y=30)
    labelY.place(x=5,y=50)
    #xt=x text
    #yt=y text
    labeltext=Label(new,text="Текст надписи:",background="#ceddff")
    labeltext.place(x=10,y=100)

    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)

    textfg=Text(new,width=20,height=2)
    textfg.place(x=100,y=300)

    label_fg=Label(new,text="Цвет текста:",background="#ceddff")
    label_fg.place(x=20,y=310)
    textfg.insert(1.0,"black")


    labeltext=Text(new,width=50,height=2)
    labeltext.place(x=100,y=100)

    font_size=Text(new,width=10,height=1)
    font_size.place(x=100,y=360)

    font_size.insert(1.0,"10")

    font_label=Label(new,text="Размер текста:",background="#ceddff")
    font_label.place(x=5,y=360)

    backg=Text(new,width=30,height=1)
    backg.place(x=170,y=450)

    backg.insert

    labelbg=Label(new,text="Фон текста",background="#ceddff")
    labelbg.place(x=1,y=450)

    choosefont=Listbox(new,height=3)
    choosefont.place(x=140,y=345)
    choosefont.insert(END,"Arial ","Bold ","Italic ")
    omglabel=Label(new,text="<- Шрифт",background="#ceddff")
    omglabel.place(x=270,y=360)





    def pack():
       textbackground=backg.get("1.0",END+'-1c')
       f=str()
       result = (choosefont.curselection())

       if result==(0,):
            f='"Arial"'
       elif result==(1,):
            f='"Bold"'
       elif result==(2,):
            f='"Italic"'

       sf=font_size.get("1.0",END+'-1c')
       res=str
       res=(f +" "+ sf)
       foreground=textfg.get("1.0",END+'-1c')
       xpos=xt.get("1.0",END+'-1c')
       ypos=yt.get("1.0",END+'-1c')
       text=labeltext.get("1.0",END+'-1c')
       lab1=Label(window,text=text,fg=foreground,bg=textbackground,font=res)
       lab1.place(x=xpos,y=ypos)
    btn=Button(new,width=30,height=2,activebackground="#4F79E0",activeforeground="white",text="Собрать",command=pack,background="#4F79E0",foreground="white")
    btn.place(x=100,y=500)


def button():
    new=Tk()
    new.title("Создать кнопку")
    new.iconbitmap("C:\Windows\System32\DevicePairingWizard.exe")
    ca=Canvas(new,width=600,height=500)
    ca.pack()
    labeltext=Label(new,text="Текст кнопки:",background="#ceddff")
    labeltext.place(x=10,y=100)

    new.resizable(width="false",height="false")

    ca.config(bg="#ceddff")
    button_text=Text(new,width=50,height=2)
    button_text.place(x=100,y=100)

    textfg=Text(new,width=20,height=2)
    textfg.place(x=115,y=150)
    fgtext=Label(new,text="Цвет текста кнопки:",background="#ceddff")
    fgtext.place(x=1,y=150)

    textbg=Text(new,width=20,height=2)
    textbg.place(x=100,y=200)
    bgtext=Label(new,text="Цвет кнопки:",background="#ceddff")
    bgtext.place(x=1,y=200)

    xttext=Label(new,text="X:",background="#ceddff")
    yttext=Label(new,text="Y:",background="#ceddff")
    xttext.place(x=5,y=30)
    yttext.place(x=5,y=50)

    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)



    button_width=Text(new,width=30,height=2)
    button_width.place(x=100,y=350)
    label_button_width=Label(new,text="Ширина кнопки",background="#ceddff")
    label_button_width.place(x=5,y=350)


    button_height=Text(new,width=30,height=2)
    button_height.place(x=100,y=400)
    label_button_height=Label(new,text="Длина кнопки",background="#ceddff")
    label_button_height.place(x=5,y=400)


    activefg=Text(new,width=30,height=2)
    activefg.place(x=200,y=300)
    labelfg=Label(new,text="Цвет текста кнопки при нажатии:",background="#ceddff")
    labelfg.place(x=5,y=300)

    activecol=Text(new,width=20,height=2)
    activecol.place(x=170,y=250)
    activecolor_label=Label(new,text="Цвет кнопки при нажатии:",background="#ceddff")
    activecolor_label.place(x=5,y=250)


    def pack():

       background=textbg.get("1.0",END+'-1c')
       foreground=textfg.get("1.0",END+'-1c')




       xpos=xt.get("1.0",END+'-1c')
       ypos=yt.get("1.0",END+'-1c')


       active2=activefg.get("1.0",END+'-1c')
       activecolor=activecol.get("1.0",END+'-1c')

       if activecolor=="":
        activecol.insert(1.0,background)

       if active2=="":
        activefg.insert(1.0,foreground)

       active2=activefg.get("1.0",END+'-1c')
       activecolor=activecol.get("1.0",END+'-1c')


       text_b=button_text.get("1.0",END+'-1c')

       width_=button_width.get("1.0",END+'-1c')
       height_=button_height.get("1.0",END+'-1c')

       btn1=Button(window,activebackground=activecolor,activeforeground=active2,width=width_,height=height_, text=text_b,fg=foreground,bg=background,)
       btn1.place(x=xpos,y=ypos)

    btn=Button(new,width=30,height=2,activebackground="#4F79E0",activeforeground="white",text="Собрать",command=pack,background="#4F79E0",foreground="white")
    btn.place(x=100,y=450)

def textplace():
    new=Tk()
    new.title("Создать текстовое поле")
    new.iconbitmap("C:\Windows\System32\DpiScaling.exe")
    c=Canvas(new,width=500,height=600)
    c.pack()
    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)
    c.config(bg="#ceddff")

    new.resizable(width="false",height="false")


    labelX=Label(new,text="X:",background="#ceddff")
    labelY=Label(new,text="Y:",background="#ceddff")
    labelX.place(x=5,y=30)
    labelY.place(x=5,y=50)

    labelText=Label(new,text="Текст поля:",background="#ceddff")
    labelText.place(x=10,y=100)

    labelFg=Label(new,text="Цвет текста:",background="#ceddff")
    labelFg.place(x=10,y=200)
    labelBg=Label(new,text="Цвет поля:",background="#ceddff")
    labelBg.place(x=10,y=300)

    textfg=Text(new,width=20,height=2)
    textfg.place(x=100,y=200)
    textbg=Text(new,width=20,height=2)
    textbg.place(x=100,y=300)

    textwidth=Text(new,height=2,width=33)
    textwidth.place(x=65,y=400)
    widthlabel=Label(new,text="Ширина:",background="#ceddff")
    widthlabel.place(x=3,y=400)

    textheight=Text(new,height=2,width=33)
    textheight.place(x=65,y=500)
    heightlabel=Label(new,text="Высота:",background="#ceddff")
    heightlabel.place(x=3,y=500)



    tbox_text=Text(new,width=30,height=2)
    tbox_text.place(x=100,y=100)
    def pack():
       width_=textwidth.get("1.0",END+'-1c')
       height_=textheight.get("1.0",END+'-1c')

       background=textbg.get("1.0",END+'-1c')
       foreground=textfg.get("1.0",END+'-1c')
       xpos=xt.get("1.0",END+'-1c')
       ypos=yt.get("1.0",END+'-1c')
       text=tbox_text.get("1.0",END+'-1c')


       text1=Text(window,width=width_,height=height_,fg=foreground,bg=background)
       text1.insert(1.0,text)
       text1.place(x=xpos,y=ypos)

    btn=Button(new,width=30,height=2,activebackground="#4F79E0",activeforeground="white",text="Собрать",command=pack,background="#4F79E0",foreground="white")
    btn.place(x=100,y=550)




def menu():
    new=Tk()
    new.title("Создать меню")
    new.iconbitmap("C:\Windows\System32\mobsync.exe")
    c=Canvas(new,width=700,height=600)
    c.pack()
    nameofbuttext=Text(new,width=50,height=1)
    nameofbuttext.place(x=170,y=100)

    c.config(bg="#ceddff")

    lab=Label(new,text="Текст пункта меню:",background="#ceddff")
    lab.place(x=5,y=100)

    new.resizable(width="false",height="false")

    addcommand=Text(new,width=50,height=1)
    addcommand.place(x=170,y=150)
    lab1=Label(new,text="Текст выпадающего меню",background="#ceddff")
    lab1.place(x=5,y=150)


    def pack():
        m=Menu(window)
        window.config(menu=m)

        m1=Menu(m,tearoff=0)

        nameofbut=nameofbuttext.get("1.0",END+'-1c')
        command_text=addcommand.get("1.0",END+'-1c')

        m.add_cascade(label=nameofbut,menu=m1)
        m1.add_command(label=command_text)

        def packagain():

            m1=Menu(m,tearoff=0)

            nameofbut=nameofbuttext.get("1.0",END+'-1c')
            command_text=addcommand.get("1.0",END+'-1c')

            m.add_cascade(label=nameofbut,menu=m2)
            m2.add_command(label=command_text)
        pack_again2=Button(new,activebackground="#4F79E0",activeforeground="white",text="Собрать",width=30,height=2,background="#4F79E0",foreground="white",command=packagain)
        pack_again2.place(x=100,y=550)



    pack_=Button(new,width=30,height=2,activebackground="#4F79E0",activeforeground="white",text="Собрать",command=pack,background="#4F79E0",foreground="white")
    pack_.place(x=100,y=550)


def checkbutton():
    new=Tk()
    new.geometry("600x600")
    new.resizable(width="false",height="false")
    new.title("Создать флажок")
    new.iconbitmap("C:\Windows\System32\charmap.exe")
    new.config(background="#ceddff")
    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)
    labelX=Label(new,text="X:",background="#ceddff")
    labelY=Label(new,text="Y:",background="#ceddff")
    labelX.place(x=5,y=30)
    labelY.place(x=5,y=50)

    text=Text(new,width=30,height=2)
    text.place(x=100,y=100)
    justlab=Label(new,text="Текст флажка:",background="#ceddff")
    justlab.place(x=5,y=100)

    lol=IntVar()

    def pack():
       xpos=xt.get("1.0",END+'-1c')
       ypos=yt.get("1.0",END+'-1c')

       just=text.get("1.0",END+'-1c')

       newone=Checkbutton(window,text=just,variable=lol)
       newone.place(x=xpos,y=ypos)
    btn=Button(new,text="Собрать",width=30,height=2,command=pack,activebackground="#4F79E0",activeforeground="white",fg="white",bg="#4F79E0")
    btn.place(x=150,y=200)

def listboxcreate():
    new=Tk()
    new.geometry("500x300")
    new.title("Создать список")
    new.iconbitmap("C:\Windows\System32\proquota.exe")
    ca=Canvas(new,width=600,height=600)
    ca.pack()

    new.resizable(width="false",height="false")

    ca.config(bg="#ceddff")
    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)

    text_of_part_of_listbox=Text(new,width=30,height=2)
    text_of_part_of_listbox.place(x=150,y=100)
    text_of_part_of_listbox_label=Label(new,text="Текст:",background="#ceddff")
    text_of_part_of_listbox_label.place(x=1,y=100)

    xttext=Label(new,text="X:",background="#ceddff")
    yttext=Label(new,text="Y:",background="#ceddff")
    xttext.place(x=5,y=30)
    yttext.place(x=5,y=50)

    def pack():
       xpos=xt.get("1.0",END+'-1c')
       ypos=yt.get("1.0",END+'-1c')

       textick=text_of_part_of_listbox.get("1.0",END+'-1c')
       newlist=Listbox(window)
       newlist.place(x=xpos,y=ypos)
       newlist.insert(END,textick)


       def packagain():
         textick2=text_of_part_of_listbox.get("1.0",END+'-1c')
         newlist.insert(END,textick2)
       pack_again2=Button(new,width=30,height=2,activebackground="#4F79E0",activeforeground="white",text="Создать новыый пункт меню",fg="white",bg="#4F79E0",command=packagain)
       pack_again2.place(x=150,y=250)


    btn=Button(new,text="Создать новый список",width=30,height=2,command=pack,activebackground="#4F79E0",activeforeground="white",fg="white",bg="#4F79E0")
    btn.place(x=150,y=200)

def progressbar_create():
        new=Tk()
        new.geometry("500x500")
        new.title("Создать прогрессбар")
        new.iconbitmap("C:\Windows\System32\proquota.exe")
        ca=Canvas(new,width=600,height=600)
        ca.pack()

        new.resizable(width="false",height="false")

        ca.config(bg="#ceddff")
        xt=Text(new,width=10,height=1)
        yt=Text(new,width=10,height=1)
        xt.place(x=20,y=30)
        yt.place(x=20,y=50)

        xttext=Label(new,text="X:",background="#ceddff")
        yttext=Label(new,text="Y:",background="#ceddff")
        xttext.place(x=5,y=30)
        yttext.place(x=5,y=50)



        checklength=Text(new,width=30,height=2)
        checklength.place(x=130,y=100)
        lab=Label(new,text="Длина прогрессбара",background="#ceddff")
        lab.place(x=5,y=100)

        def pack():
            xpos=xt.get("1.0",END+'-1c')
            ypos=yt.get("1.0",END+'-1c')





            lenn=checklength.get("1.0",END+'-1c')

            newprogress=ttk.Progressbar(window,length=lenn, mode="determinate")
            newprogress.place(x=xpos,y=ypos)


            def stop():
                newprogress.stop()
                start=ttk.Button(new,text="Запустить прогрессбар",command=start)
                start.place(x=200,y=300)

            def start():
                newprogress.start()

            stop=ttk.Button(new,text="Восстановить прогрессбар",command=stop)
            stop.place(x=200,y=350)

            start=ttk.Button(new,text="Запустить пргрессбар",command=start)
            start.place(x=200,y=300)

            def step(event):
                newprogress.step(2)

            newprogress.bind('<Button-1>',step)

        btn=Button(new,text="Собрать",width=30,height=2,activebackground="#4F79E0",activeforeground="white",fg="white",bg="#4F79E0",command=pack)
        btn.place(x=150,y=250)


def combobox():
    new=Tk()
    new.geometry("500x500")
    new.title("Создать ")
    new.iconbitmap("C:\Windows\System32\proquota.exe")
    ca=Canvas(new,width=600,height=600)
    ca.pack()

    new.resizable(width="false",height="false")

    ca.config(bg="#ceddff")
    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)

    xttext=Label(new,text="X:",background="#ceddff")
    yttext=Label(new,text="Y:",background="#ceddff")
    xttext.place(x=5,y=30)
    yttext.place(x=5,y=50)

    textofvalue=Text(new,width=30,height=2)
    textofvalue.place(x=220,y=100)
    value=Label(new,text="Текст пункта выпадающего списка:",background="#ceddff")
    value.place(x=1,y=100)



    def pack():


        xpos=xt.get("1.0",END+'-1c')
        ypos=yt.get("1.0",END+'-1c')

        textt=textofvalue.get("1.0",END+'-1c')


        VAL=[textt]
        newone=ttk.Combobox(window,value=VAL)
        newone.place(x=xpos,y=ypos)

        def packagain():

            xpos=xt.get("1.0",END+'-1c')
            ypos=yt.get("1.0",END+'-1c')

            textt2=textofvalue.get("1.0",END+'-1c')
            VAL2=[textt2]

            newone=ttk.Combobox(window,value=VAL + VAL2)
            newone.place(x=xpos,y=ypos)


    btn=Button(new,text="Собрать",width=30,height=2,activebackground="#4F79E0",activeforeground="white",fg="white",bg="#4F79E0",command=pack)
    btn.place(x=150,y=400)



def radiobutton():
    new=Tk()
    new.geometry("600x600")
    new.resizable(width="false",height="false")
    new.title("Создать радиобатон")
    new.iconbitmap("C:\Windows\System32\charmap.exe")
    new.config(background="#ceddff")
    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)
    labelX=Label(new,text="X:",background="#ceddff")
    labelY=Label(new,text="Y:",background="#ceddff")
    labelX.place(x=5,y=30)
    labelY.place(x=5,y=50)

    var=BooleanVar()

    text=Text(new,width=30,height=2)
    text.place(x=100,y=100)
    justlab=Label(new,text="Текст флажка:",background="#ceddff")
    justlab.place(x=5,y=100)



    def pack():
       xpos=xt.get("1.0",END+'-1c')
       ypos=yt.get("1.0",END+'-1c')

       txt=text.get("1.0",END+'-1c')

       newone=Radiobutton(window,text=txt,variable=var,value=0)
       newone.place(x=xpos,y=ypos)
    btn=Button(new,text="Собрать",width=30,height=2,command=pack,activebackground="#4F79E0",activeforeground="white",fg="white",bg="#4F79E0")
    btn.place(x=150,y=200)


def tbutton():
    new=Tk()
    new.title("Создать красивую кнопку")
    new.iconbitmap("C:\Windows\System32\DevicePairingWizard.exe")
    ca=Canvas(new,width=600,height=500)
    ca.pack()
    labeltext=Label(new,text="Текст кнопки:",background="#ceddff")
    labeltext.place(x=10,y=100)

    new.resizable(width="false",height="false")

    ca.config(bg="#ceddff")
    button_text=Text(new,width=50,height=2)
    button_text.place(x=100,y=100)

    xttext=Label(new,text="X:",background="#ceddff")
    yttext=Label(new,text="Y:",background="#ceddff")
    xttext.place(x=5,y=30)
    yttext.place(x=5,y=50)

    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)


    def pack():
       xpos=xt.get("1.0",END+'-1c')
       ypos=yt.get("1.0",END+'-1c')
       text_b=button_text.get("1.0",END+'-1c')

       btn1=ttk.Button(window,text=text_b)
       btn1.place(x=xpos,y=ypos)

    btn=ttk.Button(new,text="Собрать",command=pack)
    btn.place(x=100,y=150)

def scale():
    new=Tk()
    new.title("Создать полосу прокрутки")
    new.iconbitmap("C:\Windows\System32\cliconfg.exe")
    ca=Canvas(new,width=600,height=350)
    ca.pack()

    new.resizable(width="false",height="false")

    ca.config(bg="#ceddff")
    button_text=Text(new,width=50,height=2)
    button_text.place(x=100,y=100)

    xttext=Label(new,text="X:",background="#ceddff")
    yttext=Label(new,text="Y:",background="#ceddff")
    xttext.place(x=5,y=30)
    yttext.place(x=5,y=50)

    xt=Text(new,width=10,height=1)
    yt=Text(new,width=10,height=1)
    xt.place(x=20,y=30)
    yt.place(x=20,y=50)

    leng=Text(new,width=30,height=2)
    leng.place(x=100,y=100)
    lenglab=Label(new,text="Длина:",bg="#ceddff")
    lenglab.place(x=20,y=100)

    def packhor():
        lengthh=leng.get("1.0",END+'-1c')

        xpos=xt.get("1.0",END+'-1c')
        ypos=yt.get("1.0",END+'-1c')

        newone=ttk.Scale(window,length=lengthh,orient="horizontal")
        newone.place(x=xpos,y=ypos)

    def packver():
        lengthh=leng.get("1.0",END+'-1c')

        xpos=xt.get("1.0",END+'-1c')
        ypos=yt.get("1.0",END+'-1c')

        newone=ttk.Scale(window,length=lengthh,orient="vertical")
        newone.place(x=xpos,y=ypos)

    btn=Button(new,text="Собрать горизонтальную полосу",width=30,height=2,activebackground="#4F79E0",activeforeground="white",fg="white",bg="#4F79E0",command=packhor)
    btn.place(x=100,y=250)

    btn1=Button(new,text="Собрать вертикальную полосу",width=30,height=2,activebackground="#4F79E0",activeforeground="white",fg="white",bg="#4F79E0",command=packver)
    btn1.place(x=100,y=300)



lab1=Label(win,text="Выберите элемент",width=20,height=5,bg="#ceddff",font="Arial 20")
lab1.place(x=110,y=-29)


lab_button=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать надпись",fg="white",bg="#4F79E0",width=30,height=2,command=label)
lab_button.place(x=50,y=150)

btn_button=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать кнопку",fg="white",bg="#4F79E0",width=30,height=2,command=button)
btn_button.place(x=50,y=200)

tbox_button=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать текстовое поле",fg="white",bg="#4F79E0",width=30,height=2,command=textplace)
tbox_button.place(x=50,y=250)

menubutton=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать меню",fg="white",bg="#4F79E0",width=30,height=2,command=menu)
menubutton.place(x=50,y=300)

checkb_button=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать флажок",fg="white",bg="#4F79E0",width=30,height=2,command=checkbutton)
checkb_button.place(x=50,y=350)

scaleButton=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать полосу прокрутки",fg="white",bg="#4F79E0",width=30,height=2,command=scale)
scaleButton.place(x=160,y=400)

listbutton=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать список",fg="white",bg="#4F79E0",width=30,height=2,command=listboxcreate)
listbutton.place(x=275,y=150)

progresstbutton=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать шкалу загрузки",fg="white",bg="#4F79E0",width=30,height=2,command=progressbar_create)
progresstbutton.place(x=275,y=200)

comboboxb=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать выпадающий список",fg="white",bg="#4F79E0",width=30,height=2,command=combobox)
comboboxb.place(x=275,y=250)

radiob=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать радиобатоны",fg="white",bg="#4F79E0",width=30,height=2,command=radiobutton)
radiob.place(x=275,y=300)

ttkbutton=Button(win,activebackground="#4F79E0",activeforeground="white",text="Создать красивую кнопку",fg="white",bg="#4F79E0",width=30,height=2,command=tbutton)
ttkbutton.place(x=275,y=350)




mainloop()

#   335(!) Строчек кода, неколько дней упорного труда и куча ошибок во время выполнения (вместе с утраченными нервами).
#   Как же я сейчас рад это писать, но хорошо, что я возможно помогу другим программистам. В дальнейшем буду добавлять другие функции. Всем добра, пойду отдохну ;)
#   Поправочка: после написания этого текста я просидел ещё три часа и рад представить вам этот проект, и теперь строчек почти 500(!!!).

#   Для связи:
#      TELEGRAM: t.me/root011
#      VK: vk.com/simple_vasya
#   :D

#29.06.2018
#Это 999 строчка! Я никогда раньше не писал такие большие проекты! ФИГЕТЬ!
#ТАМ ТАМ ТАМТАМТАМ ТАМТАМТАМТАМТАМТАМ У НАС ЮБИЛЕЙ!
