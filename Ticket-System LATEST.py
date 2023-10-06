from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import tkinter as Tk
import datetime
import time

########################################################################
########################################################################
########################################################################

db = sqlite3.connect(':memory:')
db = sqlite3.connect('Tickets5',timeout=10)

cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tickets(id INTEGER PRIMARY KEY, movie TEXT,cinema TEXT, date TEXT,  time TEXT, payment TEXT, 
                                       name TEXT, email TEXT, mobile TEXT, passport TEXT, adult INTEGER, children INTEGER,
                                       oku INTEGER, senior INTEGER, popcorn INTEGER, drinks INTEGER, seating TEXT,price REAL)
''')
global logined
logined=False
class OtherFramelogin(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='hotpink3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)
      text=Label(self, text="Login System")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'light slate blue')
      text.place(x=240, y=20)

    #----------------------------------------------------------------------
  def OpenInFramelogin(self):
      """"""
      self.hide()
      subFrame = OtherInFramelogin(self)
      
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
########################################################################
########################################################################

class OtherInFramebirth(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='hotpink3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)
      text=Label(self, text="Birthday promotions")
      text.config(font=('Britannic Bold',30))
      text.config(fg = 'royal blue')
      text.place(x=120, y=20)

      load = Image.open("birthday.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=80)

      load = Image.open("BIRTHDAY1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=250, y=90)

      load = Image.open("BIRTHDAY2.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=400)

      text=Label(self, text="Members who have an account get a 90% discount \nfor ticket purchases and 50% discount for food or \nsnacks purchases on their birthday month wIth IC.")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'royal blue', anchor='w')
      text.place(x=30, y=280)

      

    #----------------------------------------------------------------------
 
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
########################################################################
########################################################################
########################################################################

class OtherInFramesnack(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='hot pink', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)
      text=Label(self, text="Snack promotions")
      text.config(font=('Britannic Bold',30))
      text.config(fg = 'PaleVioletRed3')
      text.place(x=140, y=20)

      load = Image.open("pop1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=90)

      load = Image.open("snack.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=250, y=90)

      load = Image.open("pop2.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=400)

      text=Label(self, text="Buy 5 packs of popcorn to get a 60% discount \nvoucher to buy other snacks in infinity cinema.")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'PaleVioletRed4', anchor='w')
      text.place(x=50, y=310)
  
    #----------------------------------------------------------------------
 
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
########################################################################
########################################################################

class OtherInFramecast(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='plum3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)
      text=Label(self, text="Cast Meetup")
      text.config(font=('Britannic Bold',38))
      text.config(fg = 'royal blue')
      text.place(x=170, y=20)

      load = Image.open("cast1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=90)

      load = Image.open("cast2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=250, y=100)

      load = Image.open("cast3.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=400)

      text=Label(self, text="Everyone who buys a ticket at Infinity Cinema\n gets a chance to take a photo with the cast \n invited in a lucky draw once a year in June.")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'PaleVioletRed4', anchor='w')
      text.place(x=50, y=310)
      
    
    #----------------------------------------------------------------------
 
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
########################################################################
########################################################################
########################################################################

class OtherFramePro(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)

      load = Image.open("text2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=-50, y=-50)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='hotpink3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
      btn = Tk.Button(self, text="Birthday", command=self.OpenInFramebirth,bg='light pink', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=50,y=120)

      btn = Tk.Button(self, text="Snack", command=self.OpenInFramesnack,bg='thistle', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=250,y=120)

      btn = Tk.Button(self, text="Cast Meetup", command=self.OpenInFramecast,bg='plum2', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=450,y=120)

      load = Image.open("birthday.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=30, y=200)

      load = Image.open("pop1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=220, y=200)

      load = Image.open("cast.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=420, y=200)
      
     # print(self.original_frame.text)
      text=Label(self, text="Promotions")
      text.config(font=('Britannic Bold',40))
      text.config(bg = 'white',fg = 'violet red')
      text.place(x=180, y=20)

    #----------------------------------------------------------------------
  def OpenInFramebirth(self):
      """"""
      self.hide()
      subFrame = OtherInFramebirth(self)

  def OpenInFramesnack(self):
      """"""
      self.hide()
      subFrame = OtherInFramesnack(self)

  def OpenInFramecast(self):
      """"""
      self.hide()
      subFrame = OtherInFramecast(self)

      
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
class OtherInFrameJoh(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='orchid3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("Johnny.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("je1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="Johnny English")
      text.config(font=('Britannic Bold',30))
      text.config(fg = 'IndianRed2')
      text.place(x=160, y=20)

      text=Label(self, text="Director  :  Peter Howitt")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'maroon')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        :  Rowan Atkinson, Ben Miller, Greg Wise")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'maroon')
      text1.place(x=245, y=130)

      text2=Label(self, text="Synopsis :  Pascal Sauvage, a villain intent on stealing")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=155)

      text2=Label(self, text="                  Britain's Crown Jewels, has murdered the ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=175)

      text2=Label(self, text="                  country's top undercover agents, and ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=195)

      text2=Label(self, text="                  mediocre spy Johnny English is ordered to")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=215)

      text2=Label(self, text="                  prevent further mayhem. But even with help")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=235)

      text2=Label(self, text="                  from quick-thinking sidekick Bough, the")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=255)

      text2=Label(self, text="                  goofy agent lands himself in one precarious")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=275)

      text2=Label(self, text="                  situation after another. ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 89 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'maroon')
      text3.place(x=245, y=328)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'maroon')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : October 14 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'maroon')
      text6.place(x=350, y=430)

      text7=Label(self, text="Distributor     : Universal Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'maroon')
      text7.place(x=350, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=RFinNxS5KN4) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'maroon')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentJoh(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Johnny English', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))



  def onClose(self):
      self.destroy()
      self.original_frame.show()


class ProfileSetting(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)
        text = Label(self, text="Profile Setting")
        text.config(font=('Arial Black', 30))
        text.place(x=150, y=10)
        text2 = Label(self, text="Name")
        text2.config(font=('Arial Black', 15))
        text2.place(x=100, y=110)
        text3 = Label(self, text="E-mail")
        text3.config(font=('Arial Black', 15))
        text3.place(x=100, y=210)
        text4 = Label(self, text="Mobile No")
        text4.config(font=('Arial Black', 15))
        text4.place(x=100, y=310)
        text5 = Label(self, text="IC/Passport")
        text5.config(font=('Arial Black', 15))
        text5.place(x=100, y=410)


        global name
        name = Entry(self, textvariable='name', font=('Arahoni', 20))
        name.place(x=100, y=160)
        global email
        email = Entry(self, textvariable='email', font=('Arahoni', 20))
        email.place(x=100, y=260)
        global mobile
        mobile = Entry(self, textvariable='mobile', font=('Arahoni', 20))
        mobile.place(x=100, y=360)
        global passport
        passport = Entry(self, textvariable='passport', font=('Arahoni', 20))
        passport.place(x=100, y=460)

        nextbtn = Button(self, text="Next",command=self.OpenInFrameTicket,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)

    def hide(self):
        self.withdraw()

    def OpenInFrameTicket(self):
        """"""
        self.hide()
        subFrame = TicketSelection(self)
        namedata=name.get()
        emaildata=email.get()
        mobiledata=mobile.get()
        passportdata=passport.get()
        cursor.execute('''UPDATE tickets SET name = ?, email = ?, mobile = ?, passport = ? WHERE id = ?''',
                       (namedata,emaildata,mobiledata,passportdata,cursor.lastrowid))


class PaymentJur(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("jur - Copy.jpg")
        load.resize((100, 160)).save('jur - Copy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Johny English")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)


class PaymentNun(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("nun.jpg")
        load.resize((100, 160)).save('nun.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="The Nun")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)

class PaymentJoh(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("je.jpg")
        load.resize((100, 160)).save('je.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Johnny English")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)

class PaymentIT(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("itit.jpg")
        load.resize((100, 160)).save('itit.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="IT")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)

class PaymentNAP(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("nappy.jpg")
        load.resize((100, 160)).save('nappy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Nappily Ever After")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)

class PaymentLA(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("lala.png")
        load.resize((100, 160)).save('lala.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="La La Land")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)

class PaymentARRIVAL(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("arrival.jpg")
        load.resize((100, 160)).save('arrival.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Arrival")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)

class PaymentPHO(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("darky.jpg")
        load.resize((100, 160)).save('darky6+'
                                     '3.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Dark Phoenix")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)

class PaymentBlack(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("blackblack.jpg")
        load.resize((100, 160)).save('blackblack.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Black Panther")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)

class PaymentSMA(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("smallsmall.jpg")
        load.resize((100, 160)).save('smallsmall.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Smallfoot")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)


class PaymentBlind(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("blind.jpg")
        load.resize((100, 160)).save('blind.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="The Blind Side")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)


class PaymentW(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("W - Copy.jpg")
        load.resize((100, 160)).save('W - Copy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Wonder")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)


class PaymentPre(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("pre - Copy.jpg")
        load.resize((100, 160)).save('pre - Copy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="The Predator")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)


class PaymentJL(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("jl - Copy.jpg")
        load.resize((100, 160)).save('jl - Copy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Movie Title")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Inside Out")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['place', 'date', 'time', 'pay']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('SELECT CINEMA')

        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')

        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Wednesday 17/10/18', 'Thursday 18/10/18', 'Friday 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('SELECT DATE')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('SELECT TIME')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Credit Card/ Debit Card', 'PayPal', 'E-Voucher']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Next", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = ProfileSetting(self)


class FinalPayment(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)

        cursor.execute('''SELECT movie,cinema,date,time,adult,children,oku,senior,popcorn,drinks,seating FROM tickets WHERE id = ?''',(cursor.lastrowid,))
        alldata=cursor.fetchone()

        text = Label(self, text="Payment")
        text.config(font=('Arial Black', 15))
        text.place(x=10, y=10)
        text2 = Label(self, text="CINEMA")
        text2.config(font=('Arial Black', 10))
        text2.place(x=10, y=50)
        text3 = Label(self, text="MOVIE TITLE")
        text3.config(font=('Arial Black', 10))
        text3.place(x=10, y=70)
        text4 = Label(self, text="TIME")
        text4.config(font=('Arial Black', 10))
        text4.place(x=10, y=90)
        text5 = Label(self, text="DATE")
        text5.config(font=('Arial Black', 10))
        text5.place(x=10, y=110)
        #text6 = Label(self, text="SEATS SELECTED")
        #text6.config(font=('Arial Black', 10))
        #text6.place(x=10, y=130)
        text7 = Label(self, text="QUANTITY")
        text7.config(font=('Arial Black', 10))
        text7.place(x=300, y=200)
        text8 = Label(self, text="PRICE")
        text8.config(font=('Arial Black', 10))
        text8.place(x=500, y=200)
        text9 = Label(self, text="Adult")
        text9.config(font=('Arial Black', 10))
        text9.place(x=10, y=230)
        text10 = Label(self, text="Children")
        text10.config(font=('Arial Black', 10))
        text10.place(x=10, y=260)
        text11 = Label(self, text="OKU")
        text11.config(font=('Arial Black', 10))
        text11.place(x=10, y=290)
        text12 = Label(self, text="Senior")
        text12.config(font=('Arial Black', 10))
        text12.place(x=10, y=320)
        text13 = Label(self, text="Popcorn")
        text13.config(font=('Arial Black', 10))
        text13.place(x=10, y=370)
        text14 = Label(self, text="Drinks")
        text14.config(font=('Arial Black', 10))
        text14.place(x=10, y=400)

        global discount
        discount=None
        ntext2 = Label(self, text=alldata[1])
        ntext2.config(font=('Arial Black', 10))
        ntext2.place(x=400, y=50)
        ntext3 = Label(self, text=alldata[0])
        ntext3.config(font=('Arial Black', 10))
        ntext3.place(x=400, y=70)
        ntext4 = Label(self, text=alldata[3])
        ntext4.config(font=('Arial Black', 10))
        ntext4.place(x=400, y=90)
        ntext5 = Label(self, text=alldata[2])
        ntext5.config(font=('Arial Black', 10))
        ntext5.place(x=400, y=110)
        #ntext6 = Label(self, text=alldata[10])
        #ntext6.config(font=('Arial Black', 10))
        #ntext6.place(x=400, y=130)
        ntext7 = Label(self, text=str(alldata[4]))
        ntext7.config(font=('Arial Black', 10))
        ntext7.place(x=332, y=230)
        ntext9 = Label(self, text=str(alldata[5]))
        ntext9.config(font=('Arial Black', 10))
        ntext9.place(x=332, y=260)
        ntext8 = Label(self, text="RM13.50")
        ntext8.config(font=('Arial Black', 10))
        ntext8.place(x=495, y=230)
        ntext10 = Label(self, text=str(alldata[6]))
        ntext10.config(font=('Arial Black', 10))
        ntext10.place(x=332, y=290)
        ntext11 = Label(self, text=str(alldata[7]))
        ntext11.config(font=('Arial Black', 10))
        ntext11.place(x=332, y=320)
        ntext12 = Label(self, text="RM8.00")
        ntext12.config(font=('Arial Black', 10))
        ntext12.place(x=495, y=260)
        ntext13 = Label(self, text="RM8.00")
        ntext13.config(font=('Arial Black', 10))
        ntext13.place(x=495, y=290)
        ntext14 = Label(self, text="RM8.00")
        ntext14.config(font=('Arial Black', 10))
        ntext14.place(x=495, y=320)
        ntext15 = Label(self, text="RM8.50")
        ntext15.config(font=('Arial Black', 10))
        ntext15.place(x=495, y=370)
        ntext16 = Label(self, text="RM1.50")
        ntext16.config(font=('Arial Black', 10))
        ntext16.place(x=495, y=400)
        ntext17 = Label(self, text=str(alldata[8]))
        ntext17.config(font=('Arial Black', 10))
        ntext17.place(x=332, y=370)
        ntext18 = Label(self, text=str(alldata[9]))
        ntext18.config(font=('Arial Black', 10))
        ntext18.place(x=332, y=400)
        if logined==True:
            discount=0.9
            text15 = Label(self, text="Discount: 10%")
            text15.config(font=('Arial Black', 15))
            text15.place(x=10, y=480)
        else:
            discount=1
            text15 = Label(self, text="Discount: 0%")
            text15.config(font=('Arial Black', 15))
            text15.place(x=10, y=480)

        totalprice=alldata[4]*13.50 + alldata[5] * 8.00 + alldata[6] * 8.00 + alldata[7] * 8.00 + alldata[8] * 8.50 + alldata[9] * 1.50
        totalpricey = totalprice * discount
        print(discount)
        cursor.execute('''UPDATE tickets SET price = ? WHERE id = ?''',(totalpricey,cursor.lastrowid))
        text15 = Label(self, text="Total: "+"RM"+str(totalpricey))
        text15.config(font=('Arial Black', 15))
        text15.place(x=10, y=480)



        nextbtn = Button(self, text="Pay!",command=self.OpenInFrameSelfPrint,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=525)

    def hide(self):
        self.withdraw()

    def OpenInFrameSelfPrint(self):
        """"""
        self.hide()
        subFrame = selfprintticket(self)

class selfprintticket(Tk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)

        cursor.execute(
            '''SELECT movie,cinema,date,time,payment,adult,children,oku,senior,popcorn,drinks,seating,price FROM tickets WHERE id = ?''',
            (cursor.lastrowid,))
        alldata = cursor.fetchone()

        for x in range(0,13):
            print(alldata[x])
        load = Image.open("infinity2.png")
        load.resize((50, 50)).save('infinity2.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=10, y=10)
        load2 = Image.open("qrcode.png")
        load2.resize((100, 100)).save('qrcode.png')
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self, image=render2)
        img2.image = render2
        img2.place(x=490, y=10)

        text = Label(self, text="Self-Print Ticket")
        text.config(font=('Arial Black', 30))
        text.place(x=100, y=30)
        text2 = Label(self, text="ID")
        text2.config(font=('Arial Black', 10))
        text2.place(x=10, y=125)
        text3 = Label(self, text="Movie Title")
        text3.config(font=('Arial Black', 10))
        text3.place(x=10, y=150)
        text4 = Label(self, text="Cinema")
        text4.config(font=('Arial Black', 10))
        text4.place(x=10, y=175)
        text5 = Label(self, text="Movie Date")
        text5.config(font=('Arial Black', 10))
        text5.place(x=10, y=200)
        text6 = Label(self, text="Seat No.")
        text6.config(font=('Arial Black', 10))
        text6.place(x=10, y=225)
        text7 = Label(self, text="Amount")
        text7.config(font=('Arial Black', 10))
        text7.place(x=10, y=250)
        text8 = Label(self, text="Transaction Date")
        text8.config(font=('Arial Black', 10))
        text8.place(x=10, y=275)
        text9 = Label(self, text="Movie Time")
        text9.config(font=('Arial Black', 10))
        text9.place(x=10, y=300)
        text10 = Label(self, text="No. of Tickets")
        text10.config(font=('Arial Black', 10))
        text10.place(x=10, y=325)
        text11 = Label(self, text="Payment Type")
        text11.config(font=('Arial Black', 10))
        text11.place(x=10, y=370)

        ntext2 = Label(self, text=":")
        ntext2.config(font=('Arial Black', 10))
        ntext2.place(x=300, y=125)
        ntext3 = Label(self, text=":")
        ntext3.config(font=('Arial Black', 10))
        ntext3.place(x=300, y=150)
        ntext4 = Label(self, text=":")
        ntext4.config(font=('Arial Black', 10))
        ntext4.place(x=300, y=175)
        ntext5 = Label(self, text=":")
        ntext5.config(font=('Arial Black', 10))
        ntext5.place(x=300, y=200)
        ntext6 = Label(self, text=":")
        ntext6.config(font=('Arial Black', 10))
        ntext6.place(x=300, y=225)
        ntext7 = Label(self, text=":")
        ntext7.config(font=('Arial Black', 10))
        ntext7.place(x=300, y=250)
        ntext8 = Label(self, text=":")
        ntext8.config(font=('Arial Black', 10))
        ntext8.place(x=300, y=275)
        ntext9 = Label(self, text=":")
        ntext9.config(font=('Arial Black', 10))
        ntext9.place(x=300, y=300)
        ntext10 = Label(self, text=":")
        ntext10.config(font=('Arial Black', 10))
        ntext10.place(x=300, y=325)
        ntext11 = Label(self, text=":")
        ntext11.config(font=('Arial Black', 10))
        ntext11.place(x=300, y=370)

        vtext2 = Label(self, text=str(cursor.lastrowid))
        vtext2.config(font=('Arial Black', 10))
        vtext2.place(x=310, y=125)
        vtext3 = Label(self, text=alldata[0])
        vtext3.config(font=('Arial Black', 10))
        vtext3.place(x=310, y=150)
        vtext4 = Label(self, text=alldata[1])
        vtext4.config(font=('Arial Black', 10))
        vtext4.place(x=310, y=175)
        vtext5 = Label(self, text=alldata[2])
        vtext5.config(font=('Arial Black', 10))
        vtext5.place(x=310, y=200)
        vtext6 = Label(self, text=alldata[11])
        vtext6.config(font=('Arial Black', 10))
        vtext6.place(x=310, y=225)
        vtext7 = Label(self, text=str(alldata[12]))
        vtext7.config(font=('Arial Black', 10))
        vtext7.place(x=310, y=250)
        now = datetime.datetime.now()

        vtext8 = Label(self, text=str(now))
        vtext8.config(font=('Arial Black', 10))
        vtext8.place(x=310, y=275)
        vtext9 = Label(self, text=alldata[3])
        vtext9.config(font=('Arial Black', 10))
        vtext9.place(x=310, y=300)
        totalticket = alldata[6] + alldata[7] + alldata[8] + alldata[9]
        vtext10 = Label(self, text=str(totalticket))
        vtext10.config(font=('Arial Black', 10))
        vtext10.place(x=310, y=325)
        vtext11 = Label(self, text=alldata[4])
        vtext11.config(font=('Arial Black', 10))
        vtext11.place(x=310, y=370)

        lastext = Label(self, text="*Self-Print Ticket must be printed out and presented at the checkpoint to gain ")
        lastext.config(font=('Arial Black', 10))
        lastext.place(x=10, y=500)
        lastext2 = Label(self, text="admission into the movie hall. Alternatively, you can collect movie tickets by ")
        lastext2.config(font=('Arial Black', 10))
        lastext2.place(x=10, y=520)
        lastext3 = Label(self, text="showing the QR code or the confirmation ID to the receiptionist.")
        lastext3.config(font=('Arial Black', 10))
        lastext3.place(x=10, y=540)

        db.commit()
        db.close()


class TicketSelection(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        text = Label(self, text="Ticket(s) Selection")
        text.config(font=('Arial Black', 15))
        text.place(x=50, y=10)
        text2 = Label(self, text="Adult")
        text2.config(font=('Arial Black', 15))
        text2.place(x=50, y=75)
        text3 = Label(self, text="Children")
        text3.config(font=('Arial Black', 15))
        text3.place(x=50, y=125)
        text4 = Label(self, text="OKU")
        text4.config(font=('Arial Black', 15))
        text4.place(x=50, y=175)
        text5 = Label(self, text="Senior")
        text5.config(font=('Arial Black', 15))
        text5.place(x=50, y=225)
        text6 = Label(self, text="Snacks Selection")
        text6.config(font=('Arial Black', 15))
        text6.place(x=50, y=275)
        text7 = Label(self, text="Popcorn")
        text7.config(font=('Arial Black', 15))
        text7.place(x=175, y=350)
        text7 = Label(self, text="Soft Drink")
        text7.config(font=('Arial Black', 15))
        text7.place(x=175, y=475)

        load = Image.open("popcorn.jpg")
        load.resize((100, 100)).save('popcorn.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=325)

        load2 = Image.open("drink.jpg")
        load2.resize((100, 100)).save('drink.jpg')
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self, image=render2)
        img2.image = render2
        img2.place(x=50, y=450)

        tkvar = IntVar(root)
        choices = [0, 1, 2, 3, 4, 5, 6]
        adult = OptionMenu(self, tkvar,command=self.selectedadult, *choices)
        adult.config(height=1, width=2)
        adult.place(x=400, y=75)
        tkvar.set(0)
        tkvar2 = IntVar(root)
        children = OptionMenu(self, tkvar2,command=self.selectedchildren, *choices)
        children.config(height=1, width=2)
        children.place(x=400, y=125)
        tkvar2.set(0)
        tkvar3 = IntVar(root)
        OKU = OptionMenu(self, tkvar3,command=self.selectedoku, *choices)
        OKU.config(height=1, width=2)
        OKU.place(x=400, y=175)
        tkvar3.set(0)
        tkvar4 = IntVar(root)
        senior = OptionMenu(self, tkvar4,command=self.selectedsenior, *choices)
        senior.config(height=1, width=2)
        senior.place(x=400, y=225)
        tkvar4.set(0)
        tkvar5 = IntVar(root)
        popcorn = OptionMenu(self, tkvar5,command=self.selectedpopcorn, *choices)
        popcorn.config(height=1, width=2)
        popcorn.place(x=400, y=350)
        tkvar5.set(0)
        tkvar6 = IntVar(root)
        drink = OptionMenu(self, tkvar6,command=self.selecteddrinks, *choices)
        drink.config(height=1, width=2)
        drink.place(x=400, y=475)
        tkvar6.set(0)

        nextbtn = Button(self, text="Next",command=self.OpenInFrameSeatings, bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=525)

    def selectedadult(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET adult = ? WHERE id = ?''',(value,cursor.lastrowid))

    def selectedchildren(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET children = ? WHERE id = ?''', (value, cursor.lastrowid))

    def selectedoku(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET oku = ? WHERE id = ?''', (value, cursor.lastrowid))

    def selectedsenior(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET senior = ? WHERE id = ?''', (value, cursor.lastrowid))

    def selectedpopcorn(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET popcorn = ? WHERE id = ?''', (value, cursor.lastrowid))

    def selecteddrinks(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET drinks = ? WHERE id = ?''', (value, cursor.lastrowid))

    def hide(self):
        self.withdraw()

    def OpenInFrameSeatings(self):
        """"""
        cursor.execute('''SELECT adult,children,oku,senior FROM tickets WHERE id = ?''',(cursor.lastrowid,))
        checking=cursor.fetchone()
        if checking[0]==0 and checking[1]==0 and checking[2]==0 and checking[3]==0:
            print('Please make at least one purchase.')
        else:
            self.hide()
            subFrame = Seatings(self)


class Seatings(Tk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)

        text = Label(self, text="Seats Selection")
        text.config(font=('Arial Black', 15))
        text.place(x=10, y=10)

        global nextbtn
        nextbtn = Button(self, text="Next",command=self.OpenInFrameFPayment, bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

        cursor.execute('''SELECT adult,children,oku,senior FROM tickets WHERE id = ?''',(cursor.lastrowid,))
        tix = cursor.fetchone()
        global totalseats
        totalseats=tix[0]+tix[1]+tix[2]+tix[3]


        global text2
        text2 = Label(self, text="Seats selected:")
        text2.config(font=('Arial Black', 10))
        text2.place(x=10, y=50)
        global text3
        text3 = Label(self, text="Seats to select: "+'0'+'/'+str(totalseats))
        text3.config(font=('Arial Black', 10))
        text3.place(x=10, y=75)
        global seats
        seats = Label(self, text="0")
        seats.config(font=('Arial Black', 10))
        seats.place(x=125, y=75)

        screen = Button(self, text='Screen', bg='black')
        screen.config(height=2, width=70)
        screen.config(state=DISABLED)
        screen.place(x=50, y=125)

        global a1
        a1 = Button(self, text='A1', command=self.a1selected, bg='lightblue')
        a1.config(height=2, width=4)
        a1.config(font=('Aharoni', 15))
        a1.place(x=50, y=200)
        global a2
        a2 = Button(self, text='A2', command=self.a2selected, bg='lightblue')
        a2.config(height=2, width=4)
        a2.config(font=('Aharoni', 15))
        a2.place(x=120, y=200)
        global a3
        a3 = Button(self, text='A3', command=self.a3selected, bg='lightblue')
        a3.config(height=2, width=4)
        a3.config(font=('Aharoni', 15))
        a3.place(x=190, y=200)
        global a4
        a4 = Button(self, text='A4', command=self.a4selected, bg='lightblue')
        a4.config(height=2, width=4)
        a4.config(font=('Aharoni', 15))
        a4.place(x=260, y=200)
        global a5
        a5 = Button(self, text='A5',command=self.a5selected, bg='lightblue')
        a5.config(height=2, width=4)
        a5.config(font=('Aharoni', 15))
        a5.place(x=330, y=200)
        global a6
        a6 = Button(self, text='A6',command=self.a6selected, bg='lightblue')
        a6.config(height=2, width=4)
        a6.config(font=('Aharoni', 15))
        a6.place(x=400, y=200)
        global a7
        a7 = Button(self, text='A7',command=self.a7selected, bg='lightblue')
        a7.config(height=2, width=4)
        a7.config(font=('Aharoni', 15))
        a7.place(x=470, y=200)
        global b1
        b1 = Button(self, text='B1',command=self.b1selected, bg='lightblue')
        b1.config(height=2, width=4)
        b1.config(font=('Aharoni', 15))
        b1.place(x=50, y=270)
        global b2
        b2 = Button(self, text='B2',command=self.b2selected, bg='lightblue')
        b2.config(height=2, width=4)
        b2.config(font=('Aharoni', 15))
        b2.place(x=120, y=270)
        global b3
        b3 = Button(self, text='B3',command=self.b3selected, bg='lightblue')
        b3.config(height=2, width=4)
        b3.config(font=('Aharoni', 15))
        b3.place(x=190, y=270)
        global b4
        b4 = Button(self, text='B4',command=self.b4selected, bg='lightblue')
        b4.config(height=2, width=4)
        b4.config(font=('Aharoni', 15))
        b4.place(x=260, y=270)
        global b5
        b5 = Button(self, text='B5',command=self.b5selected, bg='lightblue')
        b5.config(height=2, width=4)
        b5.config(font=('Aharoni', 15))
        b5.place(x=330, y=270)
        global b6
        b6 = Button(self, text='B6',command=self.b6selected, bg='lightblue')
        b6.config(height=2, width=4)
        b6.config(font=('Aharoni', 15))
        b6.place(x=400, y=270)
        global b7
        b7 = Button(self, text='B7',command=self.b7selected, bg='lightblue')
        b7.config(height=2, width=4)
        b7.config(font=('Aharoni', 15))
        b7.place(x=470, y=270)
        global c1
        c1 = Button(self, text='C1',command=self.c1selected, bg='lightblue')
        c1.config(height=2, width=4)
        c1.config(font=('Aharoni', 15))
        c1.place(x=50, y=340)
        global c2
        c2 = Button(self, text='C2',command=self.c2selected, bg='lightblue')
        c2.config(height=2, width=4)
        c2.config(font=('Aharoni', 15))
        c2.place(x=120, y=340)
        global c3
        c3 = Button(self, text='C3',command=self.c3selected, bg='lightblue')
        c3.config(height=2, width=4)
        c3.config(font=('Aharoni', 15))
        c3.place(x=190, y=340)
        global c4
        c4 = Button(self, text='C4',command=self.c4selected, bg='lightblue')
        c4.config(height=2, width=4)
        c4.config(font=('Aharoni', 15))
        c4.place(x=260, y=340)
        global c5
        c5 = Button(self, text='C5',command=self.c5selected, bg='lightblue')
        c5.config(height=2, width=4)
        c5.config(font=('Aharoni', 15))
        c5.place(x=330, y=340)
        global c6
        c6 = Button(self, text='C6',command=self.c6selected, bg='lightblue')
        c6.config(height=2, width=4)
        c6.config(font=('Aharoni', 15))
        c6.place(x=400, y=340)
        global c7
        c7 = Button(self, text='C7',command=self.c7selected, bg='lightblue')
        c7.config(height=2, width=4)
        c7.config(font=('Aharoni', 15))
        c7.place(x=470, y=340)

    def hide(self):
        self.withdraw()

    def OpenInFrameFPayment(self):
        """"""
        self.hide()
        subFrame = FinalPayment(self)
        text2['text']=text2['text'].replace('Seats Selected:','')
        allseats = text2['text']
        print(allseats)
        cursor.execute('''UPDATE tickets SET seating = ? WHERE id = ?''',(allseats,cursor.lastrowid))

    def a1selected(self):
        if a1['bg'] == 'red':
            a1['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A1', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                a1['bg'] = 'red'
                text2['text'] = text2['text'] + ' A1'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'

    def a2selected(self):
        if a2['bg'] == 'red':
            a2['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A2', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                a2['bg'] = 'red'
                text2['text'] = text2['text'] + ' A2'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'

    def a3selected(self):
        if a3['bg'] == 'red':
            a3['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A3', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                a3['bg'] = 'red'
                text2['text'] = text2['text'] + ' A3'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'

    def a4selected(self):
        if a4['bg'] == 'red':
            a4['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A4', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                a4['bg'] = 'red'
                text2['text'] = text2['text'] + ' A4'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def a5selected(self):
        if a5['bg'] == 'red':
            a5['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A5', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                a5['bg'] = 'red'
                text2['text'] = text2['text'] + ' A5'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def a6selected(self):
        if a6['bg'] == 'red':
            a6['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A6', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                a6['bg'] = 'red'
                text2['text'] = text2['text'] + ' A6'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def a7selected(self):
        if a7['bg'] == 'red':
            a7['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A7', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                a7['bg'] = 'red'
                text2['text'] = text2['text'] + ' A7'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b1selected(self):
        if b1['bg'] == 'red':
            b1['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B1', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                b1['bg'] = 'red'
                text2['text'] = text2['text'] + ' B1'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b2selected(self):
        if b2['bg'] == 'red':
            b2['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B2', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                b2['bg'] = 'red'
                text2['text'] = text2['text'] + ' B2'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b3selected(self):
        if b3['bg'] == 'red':
            b3['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B3', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                b3['bg'] = 'red'
                text2['text'] = text2['text'] + ' B3'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'

    def b4selected(self):
        if b4['bg'] == 'red':
            b4['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B4', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text'] = str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text']) == totalseats:
                print('You cannot select more seats.')
            else:
                b4['bg'] = 'red'
                text2['text'] = text2['text'] + ' B4'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text'] = str(seatno)
                if int(seats['text']) == totalseats:
                    nextbtn['state'] = 'normal'
    def b5selected(self):
        if b5['bg'] == 'red':
            b5['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B5', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                b5['bg'] = 'red'
                text2['text'] = text2['text'] + ' B5'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b6selected(self):
        if b6['bg'] == 'red':
            b6['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B6', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                b6['bg'] = 'red'
                text2['text'] = text2['text'] + ' B6'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b7selected(self):
        if b7['bg'] == 'red':
            b7['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B7', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                b7['bg'] = 'red'
                text2['text'] = text2['text'] + ' B7'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c1selected(self):
        if c1['bg'] == 'red':
            c1['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C1', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                c1['bg'] = 'red'
                text2['text'] = text2['text'] + ' C1'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c2selected(self):
        if c2['bg'] == 'red':
            c2['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C2', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                c2['bg'] = 'red'
                text2['text'] = text2['text'] + ' C2'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c3selected(self):
        if c3['bg'] == 'red':
            c3['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C3', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                c3['bg'] = 'red'
                text2['text'] = text2['text'] + ' C3'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c4selected(self):
        if c4['bg'] == 'red':
            c4['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C4', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                c4['bg'] = 'red'
                text2['text'] = text2['text'] + ' C4'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c5selected(self):
        if c5['bg'] == 'red':
            c5['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C5', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                c5['bg'] = 'red'
                text2['text'] = text2['text'] + ' C5'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c6selected(self):
        if c6['bg'] == 'red':
            c6['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C6', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                c6['bg'] = 'red'
                text2['text'] = text2['text'] + ' C6'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c7selected(self):
        if c7['bg'] == 'red':
            c7['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C7', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('You cannot select more seats.')
            else:
                c7['bg'] = 'red'
                text2['text'] = text2['text'] + ' C7'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'









            ########################################################################
########################################################################
class OtherInFrameJL(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='plum3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!",command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("io.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("io1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="Inside Out")
      text.config(font=('Britannic Bold',40))
      text.config(fg = 'chocolate2')
      text.place(x=190, y=20)

      text=Label(self, text="Director  :  Pete Docter")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'maroon')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        :  Amy Poehler, Phyllis Smith, Bill Hader")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'maroon')
      text1.place(x=245, y=130)

      text2=Label(self, text="Synopsis :  Riley is a happy, hockey-loving 11-year-old")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=155)

      text2=Label(self, text="                  Midwestern girl, but her world turns upside")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=175)

      text2=Label(self, text="                  -down when she and her parents move to")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=195)

      text2=Label(self, text="                  San Francisco. Riley's emotions - led by Joy,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=215)

      text2=Label(self, text="                  try to guide her through this difficult,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=235)

      text2=Label(self, text="                  life-changing event. However, the stress of")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=255)

      text2=Label(self, text="                  the move brings Sadness to the forefront.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=275)


      text3=Label(self, text="Duration : 102 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'maroon')
      text3.place(x=245, y=310)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'maroon')
      text5.place(x=245, y=335)

      text6=Label(self, text="Date released : August 27 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'maroon')
      text6.place(x=358, y=430)

      text7=Label(self, text="Distributor     : Walt Disney Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'maroon')
      text7.place(x=358, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=_MC3XuMvsDI) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'maroon')
      text4.place(x=85, y=570)

  def onClose(self):
      self.destroy()
      self.original_frame.show()
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentJL(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Inside Out', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
########################################################################
########################################################################
########################################################################
########################################################################

class OtherFrameOthers(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='hotpink3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("movie.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Johnny English", command=self.OpenInFrameJoh,bg='orchid3', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=128,y=325)

      btn = Tk.Button(self, text="Inside Out",command=self.OpenInFrameJL, bg='plum3', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=398,y=325)
      
      load = Image.open("Johnny.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=105, y=90)

      load = Image.open("jl.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=385, y=105)
      
     # if self.txt=="Others":
      text=Label(self, text="Others movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'light slate blue')
      text.place(x=250, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'SlateBlue3')
      text.place(x=20, y=40)


    #----------------------------------------------------------------------
  def OpenInFrameJoh(self):
      """"""
      self.hide()
      subFrame = OtherInFrameJoh(self)

  def OpenInFrameJL(self):
      """"""
      self.hide()
      subFrame = OtherInFrameJL(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
class OtherInFrameJur(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='CadetBlue3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)

      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("jur.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("jur1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="JURASSIC WORLD")
      text.config(font=('Arial Black',25))
      text.config(fg = 'cyan4')
      text.place(x=160, y=20)

      text=Label(self, text="Director  :  Colin Trevorrow")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'dodger blue')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        :  Bryce Dallas Howard, Chris Pratt")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'dodger blue')
      text1.place(x=245, y=130)

      text2=Label(self, text="Synopsis :  the Jurassic World luxury resort provides ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=175)

      text2=Label(self, text="                  a habitat for an array of genetically")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=195)

      text2=Label(self, text="                  engineered dinosaurs, including the vicious")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=215)

      text2=Label(self, text="                  and intelligent Indominus rex.When the")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=235)

      text2=Label(self, text="                  massive creature escapes, it sets off a")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=255)

      text2=Label(self, text="                  chain reaction that causes the other")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=275)

      text2=Label(self, text="                  dinos to run amok. ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 124 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'dodger blue')
      text3.place(x=245, y=328)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'dodger blue')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : October 6 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'dodger blue')
      text6.place(x=350, y=430)

      text7=Label(self, text="Distributor     : Universal Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'dodger blue')
      text7.place(x=350, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=RFinNxS5KN4) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'dodger blue')
      text4.place(x=85, y=570)

  def hide(self):
      self.withdraw()

  def OpenInFramePayment(self):
      """"""
      self.hide()
      subFrame = PaymentJur(self)
      cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                     ('Jurassic World', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
class OtherInFramePre(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='sky blue', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("pre1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("pre2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="The Predator")
      text.config(font=('Arial Black',25))
      text.config(fg = 'MediumPurple1')
      text.place(x=180, y=20)

      text=Label(self, text="Director  :  Shane Black")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'blue4')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        :  Olivia Munn, Alfie Allen, Thomas Jane")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'blue4')
      text1.place(x=245, y=130)

      text2=Label(self, text="Synopsis :  From the outer reaches of space to the")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=175)

      text2=Label(self, text="                  small-town streets of suburbia, the hunt")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=195)

      text2=Label(self, text="                  comes home. The universe's most lethal")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=215)

      text2=Label(self, text="                  hunters are stronger, smarter and deadlier")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=235)

      text2=Label(self, text="                  than ever before, having genetically")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=255)

      text2=Label(self, text="                  upgraded themselves with DNA from other")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=275)

      text2=Label(self, text="                  species.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 118 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'blue4')
      text3.place(x=245, y=328)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'blue4')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : August 26 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'blue4')
      text6.place(x=350, y=430)

      text7=Label(self, text="Distributor     : 20th Century Fox")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'blue4')
      text7.place(x=350, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=50_Ala5BKBo) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'blue4')
      text4.place(x=85, y=570)

  def hide(self):
      self.withdraw()

  def OpenInFramePayment(self):
      """"""
      self.hide()
      subFrame = PaymentPre(self)
      cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('The Predator', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
########################################################################
########################################################################

class OtherFrameAdventure(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='turquoise4', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("adventure.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Jurassic World",command=self.OpenInFrameJur, bg='CadetBlue3', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=118,y=285)

      btn = Tk.Button(self, text="The Predator", command=self.OpenInFramePre,bg='sky blue', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=388,y=285)
      
      load = Image.open("Jurassic.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=105, y=70)

      load = Image.open("pre.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=370, y=70)
      
     # if self.txt=="Adventure":
      text=Label(self, text="Adventure movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'turquoise4')
      text.place(x=250, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'turquoise3')
      text.place(x=20, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameJur(self):
      """"""
      self.hide()
      subFrame = OtherInFrameJur(self)

  def OpenInFramePre(self):
      """"""
      self.hide()
      subFrame = OtherInFramePre(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################      
class OtherInFrameBlind(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='SeaGreen3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      btn2 = Tk.Button(self, text="Buy Now!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("blinds.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("blinds2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="The Blind Side")
      text.config(font=('Arial Black',35))
      text.config(fg = 'medium sea green')
      text.place(x=200, y=20)

      text=Label(self, text="Director  : John Lee Hancock")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'sea green')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Sandra Bullock, Quinton Aaron, Jae Head")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'sea green')
      text1.place(x=245, y=150)

      text2=Label(self, text="Synopsis : Michael Oher is a homeless black teen. He")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 has drifted in and out of the school system")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 for years. Then Leigh Anne Tuohy and her")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 husband, Sean, take him in. The Tuohys")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 eventually become Michael's guardians,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 transforming both his life and theirs.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 113 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'sea green')
      text3.place(x=245, y=328)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'sea green')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : September 22 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'sea green')
      text6.place(x=350, y=430)

      text7=Label(self, text="Distributor     : Warner Bros.")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'sea green')
      text7.place(x=350, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=gvqj_Tk_kuM) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'sea green')
      text4.place(x=85, y=570)
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentBlind(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('The Blind Side', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
########################################################################
########################################################################
########################################################################
      
class OtherFrameSport(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='SeaGreen3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("run.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="The Blind Side", command=self.OpenInFrameBlind,bg='lawn green', fg='black')
      btn.config(height = 3,  width = 17)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=308,y=225)

      
      load = Image.open("sport.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=75, y=80)

      
     # if self.txt=="Sport":
      text=Label(self, text="Sport movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'chartreuse4')
      text.place(x=250, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'chartreuse3')
      text.place(x=20, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameBlind(self):
      """"""
      self.hide()
      subFrame = OtherInFrameBlind(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class OtherInFrameW(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='sky blue', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("wonder.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("WONDER1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="WONDER")
      text.config(font=('Britannic Bold',45))
      text.config(fg = 'deep sky blue')
      text.place(x=200, y=5)

      text=Label(self, text="Director  : Stephen Chbosky")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'steel blue')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Julia Roberts, Owen Wilson, Nadji Jeter")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'steel blue')
      text1.place(x=245, y=150)

      text2=Label(self, text="Synopsis : Based on the New York Times bestseller,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 WONDER tells the incredibly inspiring and")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 heartwarming story of August Pullman, a ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 boy with facial differences who enters fifth")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 grade, attending a mainstream elementary")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 school for the first time.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 113 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'steel blue')
      text3.place(x=245, y=328)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'steel blue')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : September 29 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'steel blue')
      text6.place(x=350, y=430)

      text7=Label(self, text="Distributor     : Lionsgate")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'steel blue')
      text7.place(x=350, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=ngiK1gQKgK8) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'steel blue')
      text4.place(x=85, y=570)

  def hide(self):
      self.withdraw()

  def OpenInFramePayment(self):
      """"""
      self.hide()
      subFrame = PaymentW(self)
      cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Wonder', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
########################################################################
########################################################################

class OtherFrameFamily(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='maroon3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("family.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Wonder", command=self.OpenInFrameW,bg='hot pink', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("W.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=145, y=80)
      
     # if self.txt=="Family":
      text=Label(self, text="Family movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'maroon3')
      text.place(x=250, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'maroon1')
      text.place(x=20, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameW(self):
      """"""
      self.hide()
      subFrame = OtherInFrameW(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class OtherInFrameBlack(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='SpringGreen3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("bp.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("bp1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=375)

      text=Label(self, text="Black Panther")
      text.config(font=('Britannic Bold',45))
      text.config(fg = 'goldenrod')
      text.place(x=140, y=5)

      text=Label(self, text="Director  : Ryan Coogler")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'dark goldenrod')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Chadwick Boseman, Michael B. Jordan")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'dark goldenrod')
      text1.place(x=245, y=130)

      text2=Label(self, text="Synopsis : After the death of his father, T'Challa")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=155)

      text2=Label(self, text="                 returns home to the African nation of")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 Wakanda to take his rightful place as king. ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 When a powerful enemy suddenly reappears,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 T'Challa's mettle as king -- and as Black")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 Panther -- gets tested when he's drawn into")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 a conflict that puts the fate of Wakanda and")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 the entire world at risk. ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 135 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'dark goldenrod')
      text3.place(x=245, y=328)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'dark goldenrod')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : October 13 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'dark goldenrod')
      text6.place(x=360, y=430)

      text7=Label(self, text="Distributor     : Walt Disney Studios ")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'dark goldenrod')
      text7.place(x=360, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=dxWvtMOGAhw) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'dark goldenrod')
      text4.place(x=85, y=570)

  def hide(self):
      self.withdraw()

  def OpenInFramePayment(self):
      """"""
      self.hide()
      subFrame = PaymentBlack(self)
      cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Black Panther', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
########################################################################
########################################################################
########################################################################

class OtherFrameSuperhero(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='SpringGreen3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("s.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Black Panther",command=self.OpenInFrameBlack ,bg='green2', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("black.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=145, y=80)
      
     # if self.txt=="Superhero":
      text=Label(self, text="Superhero movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'SpringGreen4')
      text.place(x=250, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'SpringGreen3')
      text.place(x=20, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameBlack(self):
      """"""
      self.hide()
      subFrame = OtherInFrameBlack(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################      
class OtherInFrameSMA(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='SteelBlue3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("small1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("small2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=375)

      text=Label(self, text="Small Foot")
      text.config(font=('Britannic Bold',45))
      text.config(fg = 'deep sky blue')
      text.place(x=150, y=5)

      text=Label(self, text="Director  : Karey Kirkpatrick")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'RoyalBlue4')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : LeBron James, Zendaya, Channing Tatum")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'RoyalBlue4')
      text1.place(x=245, y=130)

      text2=Label(self, text="Synopsis : Migo is a friendly Yeti whose world gets")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=155)

      text2=Label(self, text="                 turned upside down when he discovers")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 something that he didn't know existed - a ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 human. He soon faces banishment from his")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 snowy home when the rest of the villagers")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 refuse to believe his fantastic tale. Hoping")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 to prove them wrong, Migo embarks on an")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 epic journey to find the creature.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 102 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'RoyalBlue4')
      text3.place(x=245, y=328)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'RoyalBlue4')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : September 8 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'RoyalBlue4')
      text6.place(x=360, y=430)

      text7=Label(self, text="Distributor     : Warner Bros.")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'RoyalBlue4')
      text7.place(x=360, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=uBw6EvIxIS8) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'RoyalBlue4')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentSMA(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Smallfoot', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
########################################################################
########################################################################

class OtherFrameComedy(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='DeepSkyBlue2', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("c.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=330)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Smallfoot", command=self.OpenInFrameSMA,bg='SteelBlue3', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("small.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=165, y=80)

      
     # if self.txt=="Action":
      text=Label(self, text="Comedy movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'DeepSkyBlue2')
      text.place(x=250, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'steel blue')
      text.place(x=20, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameSMA(self):
      """"""
      self.hide()
      subFrame = OtherInFrameSMA(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()
      

    #----------------------------------------------------------------------
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class OtherInFramePHO(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='Plum2', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("a1.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("dark.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=390)

      text=Label(self, text="Dark Phoenix")
      text.config(font=('Andalus',45))
      text.config(fg = 'midnightblue')
      text.place(x=150, y=5)

      text=Label(self, text="Director  : Simon Kinberg")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'midnightblue')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Sophie Turner, Jessica Chastain, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'midnightblue')
      text1.place(x=245, y=130)

      text1=Label(self, text="                 Jennifer Lawrence")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'midnightblue')
      text1.place(x=245, y=150)

      text2=Label(self, text="Synopsis : The X-Men face their most formidable and ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 powerful foe when one of their own, Jean ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 Grey, starts to spiral out of control. During ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 a rescue mission in outer space, Jean is ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 nearly killed when she's hit by a mysterious")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 cosmic force. Once she returns home, this")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 this force not only makes her infinitely ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=295)

      text2=Label(self, text="                  more powerful, but far more unstable. ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=315)
      
      text3=Label(self, text="Duration : 138 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'midnightblue')
      text3.place(x=245, y=338)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'midnightblue')
      text5.place(x=245, y=360)

      text6=Label(self, text="Date released : October 13 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'midnightblue')
      text6.place(x=370, y=430)

      text7=Label(self, text="Distributor     : 20th Century Fox")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'midnightblue')
      text7.place(x=370, y=450)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=uup2JFXH68g) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'midnightblue')
      text4.place(x=85, y=570)
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentPHO(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Dark Phoenix', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################  
########################################################################
########################################################################      
########################################################################

class OtherFrameAction(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='Plum3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("action.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=330)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Dark Phoenix", command=self.OpenInFramePHO,bg='Plum2', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("a.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=165, y=80)

      
     # if self.txt=="Action":
      text=Label(self, text="Action movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'mediumpurple3')
      text.place(x=250, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'Plum4')
      text.place(x=20, y=40)
    #----------------------------------------------------------------------
  def OpenInFramePHO(self):
      """"""
      self.hide()
      subFrame = OtherInFramePHO(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class OtherInFrameARRIVAL(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='grey60', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      btn2 = Tk.Button(self, text="Buy Now!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("arrival1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("arrival2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      text=Label(self, text="Arrival")
      text.config(font=('Andalus',50))
      text.config(fg = 'grey60')
      text.place(x=240, y=5)

      text=Label(self, text="Director  : Denis Villeneuve")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Amy Adams, Jeremy Renner, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=130)

      text1=Label(self, text="                 Forest Whitaker")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text2=Label(self, text="Synopsis : Linguistics professor Louise Banks leads")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 an elite team of investigators when gigantic")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 spaceships touch down in 12 locations")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 around the world. As nations teeter on the")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 verge of global war, Banks and her crew ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 must race against time to find a way to")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 communicate with the visitors.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 118 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=320)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : October 6 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=360, y=430)

      text7=Label(self, text="Distributor     : Paramount")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=450)

      text7=Label(self, text="                         Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=470)


      text4=Label(self, text="Search (https://www.youtube.com/watch?v=tFMo3UJ4B4g) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentARRIVAL(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Arrival', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))


  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
      
########################################################################
########################################################################      
########################################################################

class OtherFrameSciFi(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='grey82', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      #back image
      load = Image.open("fu.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=20, y=430)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Arrival", command=self.OpenInFrameARRIVAL,bg='grey60', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("arri.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=105, y=80)

      
      
     # if self.txt=="Sci-Fi":
      text=Label(self, text="Sci-Fi movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'grey18')
      text.place(x=250, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'grey50')
      text.place(x=20, y=40)
      
    #----------------------------------------------------------------------
  def OpenInFrameARRIVAL(self):
      """"""
      self.hide()
      subFrame = OtherInFrameARRIVAL(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class OtherInFrameLA(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='medium orchid', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("LaLa1.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("LaLa2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      text=Label(self, text="LA LA LAND")
      text.config(font=('Rockwell Condensed',40))
      text.config(fg = 'medium orchid')
      text.place(x=190, y=15)

      text=Label(self, text="Director  : Damien Chazelle")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Emma Stone, Ryan Gosling, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=130)

      text1=Label(self, text="                 John Legend")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text2=Label(self, text="Synopsis : Sebastian and Mia are drawn together by ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 their common desire to do what they love.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 But as success mounts they are faced with ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 decisions that begin to fray the fragile ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 fabric of their love affair, and the dreams")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 they worked so hard to maintain in each ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 other threaten to rip them apart.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Duration : 128 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=320)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : September 8 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=360, y=430)

      text7=Label(self, text="Distributor     : Summit")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=450)

      text7=Label(self, text="                         Entertainment")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=470)


      text4=Label(self, text="Search (https://www.youtube.com/watch?v=0pdqf4P9MB8) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentLA(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('La La Land', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class OtherInFrameNAP(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='hot pink', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Buy Now!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)

      load = Image.open("nap1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("nap2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      text=Label(self, text="NAPPILY ever AFTER")
      text.config(font=('Britannic Bold',30))
      text.config(fg = 'hot pink')
      text.place(x=160, y=35)

      text=Label(self, text="Director  : Haifaa al-Mansour")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Sanaa Lathan, Ernie Hudson, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text1=Label(self, text="                 Lynn Whitfield")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=170)

      text2=Label(self, text="Synopsis : A soulful barber helps a woman piece her ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=220)

      text2=Label(self, text="                 life back together after an accident at her ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=240)

      text2=Label(self, text="                 hair salon makes her realize she is not living")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=260)

      text2=Label(self, text="                 life to the fullest.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=280)


      text3=Label(self, text="Duration : 98 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=330)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : September 22 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=360, y=430)

      text7=Label(self, text="Distributor     : Netflix")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=450)



      text4=Label(self, text="Search (https://www.youtube.com/watch?v=3xh9XFxo2Hg) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentNAP(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Nappily Ever After', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))


  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
########################################################################      
########################################################################

class OtherFrameRomance(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='medium orchid', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

       #back image
      load = Image.open("love.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=20, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Nappily Ever After",command=self.OpenInFrameNAP, bg='HotPink1', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=118,y=285)

      btn = Tk.Button(self, text="La La Land", command=self.OpenInFrameLA,bg='medium orchid', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=388,y=285)
      
      load = Image.open("nap.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=115, y=100)

      load = Image.open("La.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=385, y=100)
      
     # if self.txt=="Romance":
      text=Label(self, text="Romance movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'deep pink')
      text.place(x=220, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'RosyBrown4')
      text.place(x=20, y=40)
 
    #----------------------------------------------------------------------
  def OpenInFrameNAP(self):
      """"""
      self.hide()
      subFrame = OtherInFrameNAP(self)

  def OpenInFrameLA(self):
      """"""
      self.hide()
      subFrame = OtherInFrameLA(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   

  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
class OtherInFrameNun(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='sky blue', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      btn2 = Tk.Button(self, text="Buy Now!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("TheNun1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("TheNun2.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      text=Label(self, text="THE NuN")
      text.config(font=('Britannic Bold',40))
      text.config(fg = 'Gold3')
      text.place(x=300, y=35)

      text=Label(self, text="Director  : Corin Hardy")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Taissa Farmiga, Demián Bichir, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=130)

      text1=Label(self, text="                 Charlotte Hope")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text2=Label(self, text="Synopsis : After the mysterious death of a young nun ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=170)

      text2=Label(self, text="                 at a secluded abbey in Romania, a priest ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=190)

      text2=Label(self, text="                 with a haunted past is assigned to look into")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=210)

      text2=Label(self, text="                 the matter. Together with a novitiate, the ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=230)

      text2=Label(self, text="                 two uncover the order's unholy secret. They")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=250)

      text2=Label(self, text="                 will then have to risk their lives, faith and ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=270)

      text2=Label(self, text="                 souls to confront a malevolent force in the")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=290)

      text2=Label(self, text="                 form of a demonic nun.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=310)

      text3=Label(self, text="Duration : 96 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=330)

      text5=Label(self, text="Language : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=245, y=350)

      text6=Label(self, text="Date released : September 29 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=360, y=430)

      text7=Label(self, text="Distributor     : Warner Bros.")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=450)

      text7=Label(self, text="                         Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=470)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=pzD9zGcUNrw) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentNun(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('The Nun', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))


  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################      
class OtherInFrameIT(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
      #Details
      load = Image.open("It2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("It1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      load = Image.open("It3.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=300, y=20)

      text=Label(self, text="Director  : Andy Muschietti")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Cast        : Jaeden Lieberher, Jeremy Ray Taylor,")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=130)

      text1=Label(self, text="                 Sophia Lillis, Finn Wolfhard, Jake Sim...")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text2=Label(self, text="Synopsis : Seven young outcasts in Derry, Maine, are ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=170)

      text2=Label(self, text="                 about to face their worst nightmare, an")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=190)

      text2=Label(self, text="                 ancient, shape-shifting evil that emerges")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=210)

      text2=Label(self, text="                 from the sewer every 27 years to prey on ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=230)

      text2=Label(self, text="                 the town's children.Banding together over ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=250)

      text2=Label(self, text="                 the course of one horrifying summer, the")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=270)

      text2=Label(self, text="                 friends must overcome their own personal ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=290)

      text2=Label(self, text="                 fears to battle the murderous, bloodthirsty ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=310)

      text2=Label(self, text="                 clown known as Pennywise.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=330)

      text3=Label(self, text="Duration : 130 minutes")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=350)

      text5=Label(self, text="Language       : English")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=380, y=410)

      text6=Label(self, text="Date released : October 6 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=380, y=430)

      text7=Label(self, text="Distributor     : Warner Bros.")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=380, y=450)

      text7=Label(self, text="                         Television")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=380, y=470)

      text4=Label(self, text="Search (https://www.youtube.com/watch?v=xKJmEC5ieOk) for Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='aquamarine', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      btn2 = Tk.Button(self, text="Buy Now!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = PaymentIT(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('IT', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################

class OtherFrameHorror(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Back", command=self.onClose,bg='CadetBlue1', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     
      
     #back image
      load = Image.open("water.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=300)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="It", command=self.OpenInFrameIT,bg='aquamarine', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=118,y=285)

      btn = Tk.Button(self, text="The Nun",command=self.OpenInFrameNun, bg='sky blue', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=388,y=285)
      
      load = Image.open("It.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=115, y=100)

      load = Image.open("TheNun.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=385, y=100)

      

     # if self.txt=="Horror":
      text=Label(self, text="Horror movies")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'RoyalBlue')
      text.place(x=240, y=0)

      text=Label(self, text="Click the name of the movie to look for further information about the movie you clicked.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'cornflowerblue')
      text.place(x=20, y=40)
      #----------------------------------------------------------------------
  def OpenInFrameIT(self):
      """"""
      self.hide()
      subFrame = OtherInFrameIT(self)

  def OpenInFrameNun(self):
      """"""
      self.hide()
      subFrame = OtherInFrameNun(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
    #----------------------------------------------------------------------
  def onClose(self):
      self.destroy()
      self.original_frame.show()


    
########################################################################
######################################################################## 
########################################################################
class MovieSelection (Tk.Toplevel):
  
#  def __init__(self, master):
  def __init__(self, original):
      
#      Frame.__init__(self, master)
      self.original_frame = original
      Tk.Toplevel.__init__(self)
      self.geometry("800x800")
      self.resizable(False, False)


      
      buttonframe = Frame(self)
      container = Frame(self)
      buttonframe.pack(side="top", fill="x", expand=False)
      container.pack(side="top", fill="both", expand=True)
      
      EX = Exit(self)
      EX.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
      
      
      load = Image.open("text.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=-75, y=60)



      text4=Label(self, text="Top Movies of the week:")
      text4.config(font=('Britannic Bold',18))
      text4.config(fg = 'SlateBlue4')
      text4.place(x=505, y=73)


      load = Image.open("blackpanther.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=535, y=130)
      load = Image.open("topmovie.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=35, y=70)

      load = Image.open("topmovie1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=195, y=70)








      load = Image.open("pop.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=10, y=580)

      load = Image.open("exit.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=670, y=630)

      HorrorButton = Button(self, text="Horror",command=self.openFrameHorror , bg='deep sky blue', fg='black')
      HorrorButton.config(height = 2,  width = 15)
      HorrorButton.config(font=('Britannic Bold',10))
      HorrorButton.place(x=205, y=415)

      RomanceButton = Button(self, text="Romance",command=self.openFrameRomance,bg = 'HotPink2', fg='black')
      RomanceButton.config(height = 2,  width = 15)
      RomanceButton.config(font=('Britannic Bold',10))
      RomanceButton.place(x=460, y=415)

      ScifiButton = Button(self, text="Sci-Fi",command=self.openFrameSciFi,bg = 'Olivedrab1', fg='black')
      ScifiButton.config(height = 2,  width = 15)
      ScifiButton.config(font=('Britannic Bold',10))
      ScifiButton.place(x=205, y=465)

      ActionButton = Button(self, text="Action",command=self.openFrameAction,bg = 'MediumOrchid2', fg='black')
      ActionButton.config(height = 2,  width = 15)
      ActionButton.config(font=('Britannic Bold',10))
      ActionButton.place(x=460, y=465)

      ComedyButton = Button(self, text="Comedy",command=self.openFrameComedy,bg = 'Coral1', fg='black')
      ComedyButton.config(height = 2,  width = 15)
      ComedyButton.config(font=('Britannic Bold',10))
      ComedyButton.place(x=460, y=515)

      SPheroButton = Button(self, text="Superhero",command=self.openFrameSuperhero,bg = 'Seagreen1', fg='black')
      SPheroButton.config(height = 2,  width = 15)
      SPheroButton.config(font=('Britannic Bold',10))
      SPheroButton.place(x=205, y=515)

      FamilyButton = Button(self, text="Family",command=self.openFrameFamily,bg = 'hot pink', fg='black')
      FamilyButton.config(height =2 ,  width = 15)
      FamilyButton.config(font=('Britannic Bold',10))
      FamilyButton.place(x=460, y=565)

      SportButton = Button(self, text="Sport",command=self.openFrameSport,bg = 'SpringGreen3', fg='black')
      SportButton.config(height = 2,  width = 15)
      SportButton.config(font=('Britannic Bold',10))
      SportButton.place(x=205, y=565)

      AdventureButton = Button(self, text="Adventure",command=self.openFrameAdventure,bg = 'LightSkyBlue2', fg='black')
      AdventureButton.config(height = 2,  width = 15)
      AdventureButton.config(font=('Britannic Bold',10))
      AdventureButton.place(x=205, y=615)

      OthersButton = Button(self, text="Others",command=self.openFrameOthers,bg = 'Plum2', fg='black')
      OthersButton.config(height = 2,  width = 15)
      OthersButton.config(font=('Britannic Bold',10))
      OthersButton.place(x=460, y=615)

      EXButton = Button(self, text="Exit",command=EX.lift,bg = 'MistyRose2', fg='black')
      EXButton.config(height = 2,  width = 15)
      EXButton.config(font=('Britannic Bold',10))
      EXButton.place(x=670, y=740)

      LoginButton = Button(self, text="Login",command=self.openFramelogin,bg = 'MistyRose2', fg='black')
      LoginButton.config(height = 2,  width = 15)
      LoginButton.config(font=('Britannic Bold',10))
      LoginButton.place(x=670, y=20)

      ProButton = Button(self, text="Promotions",command=self.openFramePro,bg = 'MistyRose2', fg='black')
      ProButton.config(height = 2,  width = 15)
      ProButton.config(font=('Britannic Bold',10))
      ProButton.place(x=10, y=740)

      

      
      text=Label(self, text="Infinity Cinema")
      text.config(font=('Britannic Bold',14))
      text.config(fg = 'SlateBlue4')
      text.place(x=75, y=23)





      load = Image.open("infinity1.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=10, y=10)



      text1=Label(self, text="Please choose type of movie that you like.")
      text1.config(font=('Britannic Bold',15))
      text1.config(fg = 'SlateBlue3')
      text1.place(x=205, y=375)

      text2=Label(self, text=" Infinity possibilities , Infinity satisfication. ")
      text2.config(font=('Britannic Bold',20))
      text2.config(bg = 'light blue',fg = 'MediumPurple4')
      text2.place(x=135, y=745)



  #----------------------------------------------------------------------
  def hide(self):
    self.withdraw()
 
    #----------------------------------------------------------------------
  def openFrameHorror(self):
      """"""
      self.hide()
      subFrame = OtherFrameHorror(self)
    #----------------------------------------------------------------------
  def openFrameRomance(self):
      """"""
      self.hide()
      subFrame = OtherFrameRomance(self)
    #----------------------------------------------------------------------
  def openFrameSciFi(self):
      """"""
      self.hide()
      subFrame = OtherFrameSciFi(self)

    #----------------------------------------------------------------------
  def openFrameAction(self):
      """"""
      self.hide()
      subFrame = OtherFrameAction(self)

    #----------------------------------------------------------------------
  def openFrameComedy(self):
      """"""  
      self.hide()
      subFrame = OtherFrameComedy(self)

    #----------------------------------------------------------------------

  def openFrameSuperhero(self):
      """"""
      self.hide()
      subFrame = OtherFrameSuperhero(self)

    #----------------------------------------------------------------------

  def openFrameFamily(self):
      """"""
      self.hide()
      subFrame = OtherFrameFamily(self)

    #----------------------------------------------------------------------
  def openFrameSport(self):
      """"""
      self.hide()
      subFrame = OtherFrameSport(self)

    #----------------------------------------------------------------------

  def openFrameAdventure(self):
      """"""
      self.hide()
      subFrame = OtherFrameAdventure(self)

    #----------------------------------------------------------------------

  def openFrameOthers(self):
      """"""
      self.hide()
      subFrame = OtherFrameOthers(self)

    #----------------------------------------------------------------------
  def openFramePro(self):
      """"""
      self.hide()
      subFrame = OtherFramePro(self)

    #----------------------------------------------------------------------
  def openFramelogin(self):
      """"""
      self.hide()
      subFrame = LoginSystem(self)

    #----------------------------------------------------------------------
  def show(self):
    self.update()
    self.deiconify()
 
 
#----------------------------------------------------------------------
      

#####################################################################
#####################################################################      
###################bM VERSION##################################################
#####################################################################

########################################################################
########################################################################
########################################################################

db = sqlite3.connect(':memory:')
db = sqlite3.connect('Tickets6',timeout=10)

cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tickets(id INTEGER PRIMARY KEY, movie TEXT,cinema TEXT, date TEXT,  time TEXT, payment TEXT, 
                                       name TEXT, email TEXT, mobile TEXT, passport TEXT, adult INTEGER, children INTEGER,
                                       oku INTEGER, senior INTEGER, popcorn INTEGER, drinks INTEGER, seating TEXT,price REAL)
''')

class OtherFramelogin(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='hotpink3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)
      text=Label(self, text="Log Masuk")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'light slate blue')
      text.place(x=240, y=20)

    #----------------------------------------------------------------------
  def OpenInFramelogin(self):
      """"""
      self.hide()
      subFrame = OtherInFramelogin(self)
      
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
########################################################################
########################################################################

class OtherInFramebirth(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='hotpink3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)
      text=Label(self, text="Promosi Hari Jadi")
      text.config(font=('Britannic Bold',30))
      text.config(fg = 'royal blue')
      text.place(x=140, y=20)

      load = Image.open("birthday.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=80)

      load = Image.open("BIRTHDAY1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=250, y=90)

      load = Image.open("BIRTHDAY2.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=400)

      text=Label(self, text="Ahli yang mempunyai akaun Pawagam Infiniti \nmendapat diskaun 90% untuk pembelian tiket \ndan diskaun 50% untuk  pembelian  makanan \natau makanan ringan pada bulan hari jadi mereka")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'royal blue', anchor='w')
      text.place(x=30, y=280)

      

    #----------------------------------------------------------------------
 
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
########################################################################
########################################################################
########################################################################

class BMOtherInFramesnack(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='hot pink', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)
      text=Label(self, text="Promosi Makanan Ringan")
      text.config(font=('Britannic Bold',30))
      text.config(fg = 'PaleVioletRed3')
      text.place(x=80, y=20)

      load = Image.open("pop1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=90)

      load = Image.open("snack.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=250, y=90)

      load = Image.open("pop2.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=400)

      text=Label(self, text=" Beli 5 paket popcorn untuk mendapat 60%\ndiskaun baucar untuk membeli makanan \nringan di Pawagam Infiniti.                       ")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'PaleVioletRed4', anchor='w')
      text.place(x=50, y=310)
  
    #----------------------------------------------------------------------
 
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
########################################################################
########################################################################

class BMOtherInFramecast(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='plum3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)
      text=Label(self, text="Pertemuan Pelakon")
      text.config(font=('Britannic Bold',38))
      text.config(fg = 'royal blue')
      text.place(x=100, y=20)

      load = Image.open("cast1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=90)

      load = Image.open("cast2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=250, y=100)

      load = Image.open("cast3.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=400)

      text=Label(self, text="Belilah tiket-tiket Pawagam Infiniti untuk \nmendapat peluang untuk bertemu dan     \n    mengambil gambar dengan pelakon-pelakon \npada bulan Jun.                                       ")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'PaleVioletRed4', anchor='w')
      text.place(x=50, y=310)
      
    
    #----------------------------------------------------------------------
 
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
########################################################################
########################################################################
########################################################################

class BMOtherFramePro(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)

      load = Image.open("text2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=-50, y=-50)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='hotpink3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
      btn = Tk.Button(self, text="Hari Jadi", command=self.OpenInFramebirth,bg='light pink', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=50,y=120)

      btn = Tk.Button(self, text="Makanan Ringan", command=self.OpenInFramesnack,bg='thistle', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=250,y=120)

      btn = Tk.Button(self, text="Pertemuan Pelakon", command=self.OpenInFramecast,bg='plum2', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=450,y=120)

      load = Image.open("birthday.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=30, y=200)

      load = Image.open("pop1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=220, y=200)

      load = Image.open("cast.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=420, y=200)
      
     # print(self.original_frame.text)
      text=Label(self, text="Promosi")
      text.config(font=('Britannic Bold',40))
      text.config(bg = 'white',fg = 'violet red')
      text.place(x=200, y=20)

    #----------------------------------------------------------------------
  def OpenInFramebirth(self):
      """"""
      self.hide()
      subFrame = BMOtherInFramebirth(self)

  def OpenInFramesnack(self):
      """"""
      self.hide()
      subFrame = BMOtherInFramesnack(self)

  def OpenInFramecast(self):
      """"""
      self.hide()
      subFrame = BMOtherInFramecast(self)

      
  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
########################################################################
class BMOtherInFrameJoh(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='orchid3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("Johnny.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("je1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="Johnny English")
      text.config(font=('Britannic Bold',30))
      text.config(fg = 'IndianRed2')
      text.place(x=160, y=20)

      text=Label(self, text="Pengarah  :  Peter Howitt")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'maroon')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon    :  Rowan Atkinson, Ben Miller, Greg Wise")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'maroon')
      text1.place(x=245, y=130)

      text2=Label(self, text="Sinopsis : Pascal Sauvage,seorang penjahat berhasrat")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=155)

      text2=Label(self, text="                untuk mencuri Jewels Mahkota Britain,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=175)

      text2=Label(self, text="                telah membunuh agen penyamarat utama ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=195)

      text2=Label(self, text="                negara ini, dan pengintip biasa Johnny")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=215)

      text2=Label(self, text="                English diperintahkan untuk mengelakkan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=235)

      text2=Label(self, text="                kekacauan. Tetapi walaupun dengan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=255)

      text2=Label(self, text="                bantuan dari sidik akhbar Bough, agen ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=275)

      text2=Label(self, text="                mendarat diri dalam keadaan tidak menentu.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Tempoh : 89 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'maroon')
      text3.place(x=245, y=328)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'maroon')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : October 14 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'maroon')
      text6.place(x=350, y=430)

      text7=Label(self, text="Pengedar        : Universal Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'maroon')
      text7.place(x=350, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=RFinNxS5KN4) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'maroon')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentJoh(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Johnny English', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))



  def onClose(self):
      self.destroy()
      self.original_frame.show()


class BMProfileSetting(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)
        text = Label(self, text="Penetapan Profil")
        text.config(font=('Arial Black', 30))
        text.place(x=150, y=10)
        text2 = Label(self, text="Nama")
        text2.config(font=('Arial Black', 15))
        text2.place(x=100, y=110)
        text3 = Label(self, text="E-mel")
        text3.config(font=('Arial Black', 15))
        text3.place(x=100, y=210)
        text4 = Label(self, text="No. Telefon")
        text4.config(font=('Arial Black', 15))
        text4.place(x=100, y=310)
        text5 = Label(self, text="IC/Passport")
        text5.config(font=('Arial Black', 15))
        text5.place(x=100, y=410)


        global name
        name = Entry(self, textvariable='name', font=('Arahoni', 20))
        name.place(x=100, y=160)
        global email
        email = Entry(self, textvariable='email', font=('Arahoni', 20))
        email.place(x=100, y=260)
        global mobile
        mobile = Entry(self, textvariable='mobile', font=('Arahoni', 20))
        mobile.place(x=100, y=360)
        global passport
        passport = Entry(self, textvariable='passport', font=('Arahoni', 20))
        passport.place(x=100, y=460)

        nextbtn = Button(self, text="Teruskan",command=self.OpenInFrameTicket,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)

    def hide(self):
        self.withdraw()

    def OpenInFrameTicket(self):
        """"""
        self.hide()
        subFrame = BMTicketSelection(self)
        namedata=name.get()
        emaildata=email.get()
        mobiledata=mobile.get()
        passportdata=passport.get()
        cursor.execute('''UPDATE tickets SET name = ?, email = ?, mobile = ?, passport = ? WHERE id = ?''',
                       (namedata,emaildata,mobiledata,passportdata,cursor.lastrowid))


class BMPaymentJur(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("jur - Copy.jpg")
        load.resize((100, 160)).save('jur - Copy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Johny English")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)


class BMPaymentNun(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("nun.jpg")
        load.resize((100, 160)).save('nun.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="The Nun")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)

class BMPaymentJoh(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("je.jpg")
        load.resize((100, 160)).save('je.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Johnny English")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)

class BMPaymentIT(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("itit.jpg")
        load.resize((100, 160)).save('itit.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="IT")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)

class BMPaymentNAP(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("nappy.jpg")
        load.resize((100, 160)).save('nappy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Nappily Ever After")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)

class BMPaymentLA(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("lala.png")
        load.resize((100, 160)).save('lala.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="La La Land")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)

class BMPaymentARRIVAL(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("arrival.jpg")
        load.resize((100, 160)).save('arrival.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Arrival")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('SELECT PAYMENT METHOD')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)

class BMPaymentPHO(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("darky.jpg")
        load.resize((100, 160)).save('darky6+''3.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Dark Phoenix")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)

class BMPaymentBlack(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("blackblack.jpg")
        load.resize((100, 160)).save('blackblack.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Black Panther")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)

class BMPaymentSMA(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("smallsmall.jpg")
        load.resize((100, 160)).save('smallsmall.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Smallfoot")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Next", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)


class BMPaymentBlind(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("blind.jpg")
        load.resize((100, 160)).save('blind.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="The Blind Side")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)


class BMPaymentW(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("W - Copy.jpg")
        load.resize((100, 160)).save('W - Copy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Wonder")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)


class BMPaymentPre(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("pre - Copy.jpg")
        load.resize((100, 160)).save('pre - Copy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="The Predator")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)


class BMPaymentJL(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        load = Image.open("jl - Copy.jpg")
        load.resize((100, 160)).save('jl - Copy.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        text = Label(self, text="Nama Filem")
        text.config(font=('Arial Black', 30))
        text.place(x=250, y=30)
        text2 = Label(self, text="Inside Out")
        text2.config(font=('Arial Black', 25))
        text2.place(x=250, y=90)

        choices = ['lokasi', 'tarikh', 'masa', 'bayar']

        tkvar = StringVar(root)
        cchoices = ['Queensbay Mall', 'Gurney Plaza', 'Sunway Carnival']
        popupMenu = OptionMenu(self, tkvar, *cchoices, command=self.Selected)
        popupMenu.config(height=2, width=30)
        popupMenu.place(x=200, y=200)
        tkvar.set('=PILIH LOKASI')

        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, )
        popupMenu2.config(height=2, width=30)
        popupMenu2.config(state=DISABLED)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')

        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.config(state=DISABLED)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')

        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.config(state=DISABLED)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')

        nextbtn = Button(self, text="Teruskan", command=lambda: self.info_check(), bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

    def Selected(self, value):
        print(value)
        tkvar2 = StringVar(root)
        cchoices2 = ['Rabu 17/10/18', 'Khamis 18/10/18', 'Jumaat 19/10/18']
        popupMenu2 = OptionMenu(self, tkvar2, *cchoices2, command=self.Selected2)
        popupMenu2.config(height=2, width=30)
        popupMenu2.place(x=200, y=275)
        tkvar2.set('PILIH TARIKH')
        cursor.execute('''UPDATE tickets SET cinema = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected2(self, value):
        print(value)
        tkvar3 = StringVar(root)
        cchoices3 = ['2.30 p.m. Hall 1', '4.30 p.m. Hall 1', '6.30 p.m. Hall 1']
        popupMenu3 = OptionMenu(self, tkvar3, *cchoices3, command=self.Selected3)
        popupMenu3.config(height=2, width=30)
        popupMenu3.place(x=200, y=350)
        tkvar3.set('PILIH MASA')
        cursor.execute('''UPDATE tickets SET date = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected3(self, value):
        print(value)
        tkvar4 = StringVar(root)
        cchoices4 = ['Kad Kredit / Kad Debit', 'PayPal', 'E-Baucar']
        popupMenu4 = OptionMenu(self, tkvar4, *cchoices4, command=self.Selected4)
        popupMenu4.config(height=2, width=30)
        popupMenu4.place(x=200, y=425)
        tkvar4.set('PILIH JENIS PEMBAYARAN')
        cursor.execute('''UPDATE tickets SET time = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value

    def Selected4(self, value):
        print(value)
        nextbtn = Button(self, text="Teruskan", command=self.OpenInFrameProfile,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=500)
        cursor.execute('''UPDATE tickets SET payment = ? WHERE id = ?''', (value, cursor.lastrowid))
        return value


    def hide(self):
        self.withdraw()

    def OpenInFrameProfile(self):
        """"""
        self.hide()
        subFrame = BMProfileSetting(self)


class BMFinalPayment(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)

        cursor.execute('''SELECT movie,cinema,date,time,adult,children,oku,senior,popcorn,drinks,seating FROM tickets WHERE id = ?''',(cursor.lastrowid,))
        alldata=cursor.fetchone()

        text = Label(self, text="Pembayaran")
        text.config(font=('Arial Black', 15))
        text.place(x=10, y=10)
        text2 = Label(self, text="TEMPAT PAWAGAM")
        text2.config(font=('Arial Black', 10))
        text2.place(x=10, y=50)
        text3 = Label(self, text="NAMA FILEM")
        text3.config(font=('Arial Black', 10))
        text3.place(x=10, y=70)
        text4 = Label(self, text="MASA")
        text4.config(font=('Arial Black', 10))
        text4.place(x=10, y=90)
        text5 = Label(self, text="TARIKH")
        text5.config(font=('Arial Black', 10))
        text5.place(x=10, y=110)
        #text6 = Label(self, text="SEATS SELECTED")
        #text6.config(font=('Arial Black', 10))
        #text6.place(x=10, y=130)
        text7 = Label(self, text="KUANTITI")
        text7.config(font=('Arial Black', 10))
        text7.place(x=300, y=200)
        text8 = Label(self, text="HARGA")
        text8.config(font=('Arial Black', 10))
        text8.place(x=500, y=200)
        text9 = Label(self, text="Dewasa")
        text9.config(font=('Arial Black', 10))
        text9.place(x=10, y=230)
        text10 = Label(self, text="Kanak-kanak")
        text10.config(font=('Arial Black', 10))
        text10.place(x=10, y=260)
        text11 = Label(self, text="OKU")
        text11.config(font=('Arial Black', 10))
        text11.place(x=10, y=290)
        text12 = Label(self, text="Remaja")
        text12.config(font=('Arial Black', 10))
        text12.place(x=10, y=320)
        text13 = Label(self, text="Popcorn")
        text13.config(font=('Arial Black', 10))
        text13.place(x=10, y=370)
        text14 = Label(self, text="Minuman Ringan")
        text14.config(font=('Arial Black', 10))
        text14.place(x=10, y=400)


        ntext2 = Label(self, text=alldata[1])
        ntext2.config(font=('Arial Black', 10))
        ntext2.place(x=400, y=50)
        ntext3 = Label(self, text=alldata[0])
        ntext3.config(font=('Arial Black', 10))
        ntext3.place(x=400, y=70)
        ntext4 = Label(self, text=alldata[3])
        ntext4.config(font=('Arial Black', 10))
        ntext4.place(x=400, y=90)
        ntext5 = Label(self, text=alldata[2])
        ntext5.config(font=('Arial Black', 10))
        ntext5.place(x=400, y=110)
        #ntext6 = Label(self, text=alldata[10])
        #ntext6.config(font=('Arial Black', 10))
        #ntext6.place(x=400, y=130)
        ntext7 = Label(self, text=str(alldata[4]))
        ntext7.config(font=('Arial Black', 10))
        ntext7.place(x=332, y=230)
        ntext9 = Label(self, text=str(alldata[5]))
        ntext9.config(font=('Arial Black', 10))
        ntext9.place(x=332, y=260)
        ntext8 = Label(self, text="RM13.50")
        ntext8.config(font=('Arial Black', 10))
        ntext8.place(x=495, y=230)
        ntext10 = Label(self, text=str(alldata[6]))
        ntext10.config(font=('Arial Black', 10))
        ntext10.place(x=332, y=290)
        ntext11 = Label(self, text=str(alldata[7]))
        ntext11.config(font=('Arial Black', 10))
        ntext11.place(x=332, y=320)
        ntext12 = Label(self, text="RM8.00")
        ntext12.config(font=('Arial Black', 10))
        ntext12.place(x=495, y=260)
        ntext13 = Label(self, text="RM8.00")
        ntext13.config(font=('Arial Black', 10))
        ntext13.place(x=495, y=290)
        ntext14 = Label(self, text="RM8.00")
        ntext14.config(font=('Arial Black', 10))
        ntext14.place(x=495, y=320)
        ntext15 = Label(self, text="RM8.50")
        ntext15.config(font=('Arial Black', 10))
        ntext15.place(x=495, y=370)
        ntext16 = Label(self, text="RM1.50")
        ntext16.config(font=('Arial Black', 10))
        ntext16.place(x=495, y=400)
        ntext17 = Label(self, text=str(alldata[8]))
        ntext17.config(font=('Arial Black', 10))
        ntext17.place(x=332, y=370)
        ntext18 = Label(self, text=str(alldata[9]))
        ntext18.config(font=('Arial Black', 10))
        ntext18.place(x=332, y=400)

        totalprice=alldata[4]*13.50 + alldata[5] * 8.00 + alldata[6] * 8.00 + alldata[7] * 8.00 + alldata[8] * 8.50 + alldata[9] * 1.50
        cursor.execute('''UPDATE tickets SET price = ? WHERE id = ?''',(totalprice,cursor.lastrowid))
        text15 = Label(self, text="Jumlah: "+"RM"+str(totalprice))
        text15.config(font=('Arial Black', 15))
        text15.place(x=10, y=450)



        nextbtn = Button(self, text="Bayar!",command=self.OpenInFrameSelfPrint,bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=525)

    def hide(self):
        self.withdraw()

    def OpenInFrameSelfPrint(self):
        """"""
        self.hide()
        subFrame = BMselfprintticket(self)

class BMselfprintticket(Tk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)

        cursor.execute(
            '''SELECT movie,cinema,date,time,payment,adult,children,oku,senior,popcorn,drinks,seating,price FROM tickets WHERE id = ?''',
            (cursor.lastrowid,))
        alldata = cursor.fetchone()

        for x in range(0,13):
            print(alldata[x])
        load = Image.open("infinity2.png")
        load.resize((50, 50)).save('infinity2.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=10, y=10)
        load2 = Image.open("qrcode.png")
        load2.resize((100, 100)).save('qrcode.png')
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self, image=render2)
        img2.image = render2
        img2.place(x=490, y=10)

        text = Label(self, text="Tiket Cetak Sendiri")
        text.config(font=('Arial Black', 26))
        text.place(x=100, y=30)
        text2 = Label(self, text="ID")
        text2.config(font=('Arial Black', 10))
        text2.place(x=10, y=125)
        text3 = Label(self, text="Nama Filem")
        text3.config(font=('Arial Black', 10))
        text3.place(x=10, y=150)
        text4 = Label(self, text="Tempat Pawagam")
        text4.config(font=('Arial Black', 10))
        text4.place(x=10, y=175)
        text5 = Label(self, text="Tarikh Filem")
        text5.config(font=('Arial Black', 10))
        text5.place(x=10, y=200)
        text6 = Label(self, text="No. Kedudukan")
        text6.config(font=('Arial Black', 10))
        text6.place(x=10, y=225)
        text7 = Label(self, text="Jumlah")
        text7.config(font=('Arial Black', 10))
        text7.place(x=10, y=250)
        text8 = Label(self, text="Tarikh Transaksi")
        text8.config(font=('Arial Black', 10))
        text8.place(x=10, y=275)
        text9 = Label(self, text="Masa Filem")
        text9.config(font=('Arial Black', 10))
        text9.place(x=10, y=300)
        text10 = Label(self, text="No. Ticket")
        text10.config(font=('Arial Black', 10))
        text10.place(x=10, y=325)
        text11 = Label(self, text="Jenis Pembayaran")
        text11.config(font=('Arial Black', 10))
        text11.place(x=10, y=370)

        ntext2 = Label(self, text=":")
        ntext2.config(font=('Arial Black', 10))
        ntext2.place(x=300, y=125)
        ntext3 = Label(self, text=":")
        ntext3.config(font=('Arial Black', 10))
        ntext3.place(x=300, y=150)
        ntext4 = Label(self, text=":")
        ntext4.config(font=('Arial Black', 10))
        ntext4.place(x=300, y=175)
        ntext5 = Label(self, text=":")
        ntext5.config(font=('Arial Black', 10))
        ntext5.place(x=300, y=200)
        ntext6 = Label(self, text=":")
        ntext6.config(font=('Arial Black', 10))
        ntext6.place(x=300, y=225)
        ntext7 = Label(self, text=":")
        ntext7.config(font=('Arial Black', 10))
        ntext7.place(x=300, y=250)
        ntext8 = Label(self, text=":")
        ntext8.config(font=('Arial Black', 10))
        ntext8.place(x=300, y=275)
        ntext9 = Label(self, text=":")
        ntext9.config(font=('Arial Black', 10))
        ntext9.place(x=300, y=300)
        ntext10 = Label(self, text=":")
        ntext10.config(font=('Arial Black', 10))
        ntext10.place(x=300, y=325)
        ntext11 = Label(self, text=":")
        ntext11.config(font=('Arial Black', 10))
        ntext11.place(x=300, y=370)

        vtext2 = Label(self, text=str(cursor.lastrowid))
        vtext2.config(font=('Arial Black', 10))
        vtext2.place(x=310, y=125)
        vtext3 = Label(self, text=alldata[0])
        vtext3.config(font=('Arial Black', 10))
        vtext3.place(x=310, y=150)
        vtext4 = Label(self, text=alldata[1])
        vtext4.config(font=('Arial Black', 10))
        vtext4.place(x=310, y=175)
        vtext5 = Label(self, text=alldata[2])
        vtext5.config(font=('Arial Black', 10))
        vtext5.place(x=310, y=200)
        vtext6 = Label(self, text=alldata[11])
        vtext6.config(font=('Arial Black', 10))
        vtext6.place(x=310, y=225)
        vtext7 = Label(self, text=str(alldata[12]))
        vtext7.config(font=('Arial Black', 10))
        vtext7.place(x=310, y=250)
        now = datetime.datetime.now()

        vtext8 = Label(self, text=str(now))
        vtext8.config(font=('Arial Black', 10))
        vtext8.place(x=310, y=275)
        vtext9 = Label(self, text=alldata[3])
        vtext9.config(font=('Arial Black', 10))
        vtext9.place(x=310, y=300)
        totalticket = alldata[6] + alldata[7] + alldata[8] + alldata[9]
        vtext10 = Label(self, text=str(totalticket))
        vtext10.config(font=('Arial Black', 10))
        vtext10.place(x=310, y=325)
        vtext11 = Label(self, text=alldata[4])
        vtext11.config(font=('Arial Black', 10))
        vtext11.place(x=310, y=370)

        lastext = Label(self, text="* Tiket Percetakan diri mesti dicetak dan dibentangkan di pusat pemeriksaan ")
        lastext.config(font=('Arial Black', 10))
        lastext.place(x=10, y=500)
        lastext2 = Label(self, text="untuk mendapat kebenaran masuk ke dewan filem. Oleh sebab itu,anda boleh ")
        lastext2.config(font=('Arial Black', 10))
        lastext2.place(x=10, y=520)
        lastext3 = Label(self, text="mengumpul tiket filem. Sila tunjukkan kod QR atau ID pengesahan kepada ")
        lastext3.config(font=('Arial Black', 10))
        lastext3.place(x=10, y=540)
        lastext4 = Label(self, text="penerima.")
        lastext4.config(font=('Arial Black', 10))
        lastext4.place(x=10, y=560)

        db.commit()
        db.close()


class BMTicketSelection(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)


        text = Label(self, text="Pilihan Tiket")
        text.config(font=('Arial Black', 15))
        text.place(x=50, y=10)
        text2 = Label(self, text="Dewasa")
        text2.config(font=('Arial Black', 15))
        text2.place(x=50, y=75)
        text3 = Label(self, text="Kanak-kanak")
        text3.config(font=('Arial Black', 15))
        text3.place(x=50, y=125)
        text4 = Label(self, text="OKU")
        text4.config(font=('Arial Black', 15))
        text4.place(x=50, y=175)
        text5 = Label(self, text="Remaja")
        text5.config(font=('Arial Black', 15))
        text5.place(x=50, y=225)
        text6 = Label(self, text="Pilihan Makanan Ringan")
        text6.config(font=('Arial Black', 15))
        text6.place(x=50, y=275)
        text7 = Label(self, text="Popcorn")
        text7.config(font=('Arial Black', 15))
        text7.place(x=175, y=350)
        text7 = Label(self, text="Minuman ringan")
        text7.config(font=('Arial Black', 15))
        text7.place(x=175, y=475)

        load = Image.open("popcorn.jpg")
        load.resize((100, 100)).save('popcorn.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=325)

        load2 = Image.open("drink.jpg")
        load2.resize((100, 100)).save('drink.jpg')
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self, image=render2)
        img2.image = render2
        img2.place(x=50, y=450)

        tkvar = IntVar(root)
        choices = [0, 1, 2, 3, 4, 5, 6]
        adult = OptionMenu(self, tkvar,command=self.selectedadult, *choices)
        adult.config(height=1, width=2)
        adult.place(x=400, y=75)
        tkvar.set(0)
        tkvar2 = IntVar(root)
        children = OptionMenu(self, tkvar2,command=self.selectedchildren, *choices)
        children.config(height=1, width=2)
        children.place(x=400, y=125)
        tkvar2.set(0)
        tkvar3 = IntVar(root)
        OKU = OptionMenu(self, tkvar3,command=self.selectedoku, *choices)
        OKU.config(height=1, width=2)
        OKU.place(x=400, y=175)
        tkvar3.set(0)
        tkvar4 = IntVar(root)
        senior = OptionMenu(self, tkvar4,command=self.selectedsenior, *choices)
        senior.config(height=1, width=2)
        senior.place(x=400, y=225)
        tkvar4.set(0)
        tkvar5 = IntVar(root)
        popcorn = OptionMenu(self, tkvar5,command=self.selectedpopcorn, *choices)
        popcorn.config(height=1, width=2)
        popcorn.place(x=400, y=350)
        tkvar5.set(0)
        tkvar6 = IntVar(root)
        drink = OptionMenu(self, tkvar6,command=self.selecteddrinks, *choices)
        drink.config(height=1, width=2)
        drink.place(x=400, y=475)
        tkvar6.set(0)

        nextbtn = Button(self, text="Teruskan",command=self.OpenInFrameSeatings, bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.place(x=450, y=525)

    def selectedadult(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET adult = ? WHERE id = ?''',(value,cursor.lastrowid))

    def selectedchildren(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET children = ? WHERE id = ?''', (value, cursor.lastrowid))

    def selectedoku(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET oku = ? WHERE id = ?''', (value, cursor.lastrowid))

    def selectedsenior(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET senior = ? WHERE id = ?''', (value, cursor.lastrowid))

    def selectedpopcorn(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET popcorn = ? WHERE id = ?''', (value, cursor.lastrowid))

    def selecteddrinks(self, value):
        print(value)
        cursor.execute('''UPDATE  tickets SET drinks = ? WHERE id = ?''', (value, cursor.lastrowid))

    def hide(self):
        self.withdraw()

    def OpenInFrameSeatings(self):
        """"""
        cursor.execute('''SELECT adult,children,oku,senior FROM tickets WHERE id = ?''',(cursor.lastrowid,))
        checking=cursor.fetchone()
        if checking[0]==0 and checking[1]==0 and checking[2]==0 and checking[3]==0:
            print('Kamu mesti membeli sekurang-kurangnya satu tiket.')
        else:
            self.hide()
            subFrame = BMSeatings(self)


class BMSeatings(Tk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False, False)

        text = Label(self, text="Pilihan Kedudukan")
        text.config(font=('Arial Black', 15))
        text.place(x=10, y=10)

        global nextbtn
        nextbtn = Button(self, text="Teruskan",command=self.OpenInFrameFPayment, bg='yellow')
        nextbtn.config(height=2, width=10)
        nextbtn.config(font=('Aharoni', 15))
        nextbtn.config(state=DISABLED)
        nextbtn.place(x=450, y=500)

        cursor.execute('''SELECT adult,children,oku,senior FROM tickets WHERE id = ?''',(cursor.lastrowid,))
        tix = cursor.fetchone()
        global totalseats
        totalseats=tix[0]+tix[1]+tix[2]+tix[3]


        global text2
        text2 = Label(self, text="Kedudukan dipilih:")
        text2.config(font=('Arial Black', 10))
        text2.place(x=10, y=50)
        global text3
        text3 = Label(self, text="Jumlah kedudukan untuk dipilih: "+'0'+'/'+str(totalseats))
        text3.config(font=('Arial Black', 10))
        text3.place(x=10, y=75)
        global seats
        seats = Label(self, text="0")
        seats.config(font=('Arial Black', 10))
        seats.place(x=247, y=75)

        screen = Button(self, text='Skrin', bg='black')
        screen.config(height=2, width=70)
        screen.config(state=DISABLED)
        screen.place(x=50, y=125)

        global a1
        a1 = Button(self, text='A1', command=self.a1selected, bg='lightblue')
        a1.config(height=2, width=4)
        a1.config(font=('Aharoni', 15))
        a1.place(x=50, y=200)
        global a2
        a2 = Button(self, text='A2', command=self.a2selected, bg='lightblue')
        a2.config(height=2, width=4)
        a2.config(font=('Aharoni', 15))
        a2.place(x=120, y=200)
        global a3
        a3 = Button(self, text='A3', command=self.a3selected, bg='lightblue')
        a3.config(height=2, width=4)
        a3.config(font=('Aharoni', 15))
        a3.place(x=190, y=200)
        global a4
        a4 = Button(self, text='A4', command=self.a4selected, bg='lightblue')
        a4.config(height=2, width=4)
        a4.config(font=('Aharoni', 15))
        a4.place(x=260, y=200)
        global a5
        a5 = Button(self, text='A5',command=self.a5selected, bg='lightblue')
        a5.config(height=2, width=4)
        a5.config(font=('Aharoni', 15))
        a5.place(x=330, y=200)
        global a6
        a6 = Button(self, text='A6',command=self.a6selected, bg='lightblue')
        a6.config(height=2, width=4)
        a6.config(font=('Aharoni', 15))
        a6.place(x=400, y=200)
        global a7
        a7 = Button(self, text='A7',command=self.a7selected, bg='lightblue')
        a7.config(height=2, width=4)
        a7.config(font=('Aharoni', 15))
        a7.place(x=470, y=200)
        global b1
        b1 = Button(self, text='B1',command=self.b1selected, bg='lightblue')
        b1.config(height=2, width=4)
        b1.config(font=('Aharoni', 15))
        b1.place(x=50, y=270)
        global b2
        b2 = Button(self, text='B2',command=self.b2selected, bg='lightblue')
        b2.config(height=2, width=4)
        b2.config(font=('Aharoni', 15))
        b2.place(x=120, y=270)
        global b3
        b3 = Button(self, text='B3',command=self.b3selected, bg='lightblue')
        b3.config(height=2, width=4)
        b3.config(font=('Aharoni', 15))
        b3.place(x=190, y=270)
        global b4
        b4 = Button(self, text='B4',command=self.b4selected, bg='lightblue')
        b4.config(height=2, width=4)
        b4.config(font=('Aharoni', 15))
        b4.place(x=260, y=270)
        global b5
        b5 = Button(self, text='B5',command=self.b5selected, bg='lightblue')
        b5.config(height=2, width=4)
        b5.config(font=('Aharoni', 15))
        b5.place(x=330, y=270)
        global b6
        b6 = Button(self, text='B6',command=self.b6selected, bg='lightblue')
        b6.config(height=2, width=4)
        b6.config(font=('Aharoni', 15))
        b6.place(x=400, y=270)
        global b7
        b7 = Button(self, text='B7',command=self.b7selected, bg='lightblue')
        b7.config(height=2, width=4)
        b7.config(font=('Aharoni', 15))
        b7.place(x=470, y=270)
        global c1
        c1 = Button(self, text='C1',command=self.c1selected, bg='lightblue')
        c1.config(height=2, width=4)
        c1.config(font=('Aharoni', 15))
        c1.place(x=50, y=340)
        global c2
        c2 = Button(self, text='C2',command=self.c2selected, bg='lightblue')
        c2.config(height=2, width=4)
        c2.config(font=('Aharoni', 15))
        c2.place(x=120, y=340)
        global c3
        c3 = Button(self, text='C3',command=self.c3selected, bg='lightblue')
        c3.config(height=2, width=4)
        c3.config(font=('Aharoni', 15))
        c3.place(x=190, y=340)
        global c4
        c4 = Button(self, text='C4',command=self.c4selected, bg='lightblue')
        c4.config(height=2, width=4)
        c4.config(font=('Aharoni', 15))
        c4.place(x=260, y=340)
        global c5
        c5 = Button(self, text='C5',command=self.c5selected, bg='lightblue')
        c5.config(height=2, width=4)
        c5.config(font=('Aharoni', 15))
        c5.place(x=330, y=340)
        global c6
        c6 = Button(self, text='C6',command=self.c6selected, bg='lightblue')
        c6.config(height=2, width=4)
        c6.config(font=('Aharoni', 15))
        c6.place(x=400, y=340)
        global c7
        c7 = Button(self, text='C7',command=self.c7selected, bg='lightblue')
        c7.config(height=2, width=4)
        c7.config(font=('Aharoni', 15))
        c7.place(x=470, y=340)

    def hide(self):
        self.withdraw()

    def OpenInFrameFPayment(self):
        """"""
        self.hide()
        subFrame = BMFinalPayment(self)
        text2['text']=text2['text'].replace('Seats Selected:','')
        allseats = text2['text']
        print(allseats)
        cursor.execute('''UPDATE tickets SET seating = ? WHERE id = ?''',(allseats,cursor.lastrowid))

    def a1selected(self):
        if a1['bg'] == 'red':
            a1['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A1', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                a1['bg'] = 'red'
                text2['text'] = text2['text'] + ' A1'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'

    def a2selected(self):
        if a2['bg'] == 'red':
            a2['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A2', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                a2['bg'] = 'red'
                text2['text'] = text2['text'] + ' A2'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'

    def a3selected(self):
        if a3['bg'] == 'red':
            a3['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A3', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                a3['bg'] = 'red'
                text2['text'] = text2['text'] + ' A3'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'

    def a4selected(self):
        if a4['bg'] == 'red':
            a4['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A4', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                a4['bg'] = 'red'
                text2['text'] = text2['text'] + ' A4'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def a5selected(self):
        if a5['bg'] == 'red':
            a5['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A5', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                a5['bg'] = 'red'
                text2['text'] = text2['text'] + ' A5'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def a6selected(self):
        if a6['bg'] == 'red':
            a6['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A6', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                a6['bg'] = 'red'
                text2['text'] = text2['text'] + ' A6'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def a7selected(self):
        if a7['bg'] == 'red':
            a7['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' A7', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                a7['bg'] = 'red'
                text2['text'] = text2['text'] + ' A7'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b1selected(self):
        if b1['bg'] == 'red':
            b1['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B1', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                b1['bg'] = 'red'
                text2['text'] = text2['text'] + ' B1'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b2selected(self):
        if b2['bg'] == 'red':
            b2['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B2', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                b2['bg'] = 'red'
                text2['text'] = text2['text'] + ' B2'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b3selected(self):
        if b3['bg'] == 'red':
            b3['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B3', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                b3['bg'] = 'red'
                text2['text'] = text2['text'] + ' B3'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'

    def b4selected(self):
        if b4['bg'] == 'red':
            b4['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B4', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text'] = str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text']) == totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                b4['bg'] = 'red'
                text2['text'] = text2['text'] + ' B4'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text'] = str(seatno)
                if int(seats['text']) == totalseats:
                    nextbtn['state'] = 'normal'
    def b5selected(self):
        if b5['bg'] == 'red':
            b5['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B5', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                b5['bg'] = 'red'
                text2['text'] = text2['text'] + ' B5'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b6selected(self):
        if b6['bg'] == 'red':
            b6['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B6', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                b6['bg'] = 'red'
                text2['text'] = text2['text'] + ' B6'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def b7selected(self):
        if b7['bg'] == 'red':
            b7['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' B7', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                b7['bg'] = 'red'
                text2['text'] = text2['text'] + ' B7'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c1selected(self):
        if c1['bg'] == 'red':
            c1['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C1', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                c1['bg'] = 'red'
                text2['text'] = text2['text'] + ' C1'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c2selected(self):
        if c2['bg'] == 'red':
            c2['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C2', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                c2['bg'] = 'red'
                text2['text'] = text2['text'] + ' C2'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c3selected(self):
        if c3['bg'] == 'red':
            c3['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C3', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                c3['bg'] = 'red'
                text2['text'] = text2['text'] + ' C3'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c4selected(self):
        if c4['bg'] == 'red':
            c4['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C4', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                c4['bg'] = 'red'
                text2['text'] = text2['text'] + ' C4'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c5selected(self):
        if c5['bg'] == 'red':
            c5['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C5', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                c5['bg'] = 'red'
                text2['text'] = text2['text'] + ' C5'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c6selected(self):
        if c6['bg'] == 'red':
            c6['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C6', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                c6['bg'] = 'red'
                text2['text'] = text2['text'] + ' C6'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'
    def c7selected(self):
        if c7['bg'] == 'red':
            c7['bg'] = 'lightblue'
            text2['text'] = text2['text'].replace(' C7', '')
            seatno = int(seats['text'])
            seatno = seatno - 1
            seats['text']=str(seatno)
            if int(seats['text']) != totalseats:
                nextbtn['state'] = DISABLED

        else:
            if int(seats['text'])==totalseats:
                print('Anda tidak boleh memilih lebih banyak kedudukan.')
            else:
                c7['bg'] = 'red'
                text2['text'] = text2['text'] + ' C7'
                seatno = int(seats['text'])
                seatno = seatno + 1
                seats['text']=str(seatno)
                if int(seats['text'])==totalseats:
                    nextbtn['state']='normal'









            ########################################################################
########################################################################
class BMOtherInFrameJL(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='plum3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!",command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("io.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("io1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="Inside Out")
      text.config(font=('Britannic Bold',40))
      text.config(fg = 'chocolate2')
      text.place(x=190, y=20)

      text=Label(self, text="Pengarah  :  Pete Docter")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'maroon')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     :  Amy Poehler, Phyllis Smith, Bill Hader")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'maroon')
      text1.place(x=245, y=130)

      text2=Label(self, text="Sinopsis : Riley adalah seorang gadis Midwestern yang")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=155)

      text2=Label(self, text="                 berusia 11 tahun, yang gembira dengan")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 hoki, tetapi dunianya terbalik apabila dia")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 dan keluarganya beralih ke San Francisco.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 Diketuai oleh Joy, cuba membimbingnya ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 melalui peristiwa yang sukar dan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 mengubah kehidupan ini. Namun...")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'maroon')
      text2.place(x=245, y=275)


      text3=Label(self, text="Tempoh : 102 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'maroon')
      text3.place(x=245, y=310)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'maroon')
      text5.place(x=245, y=335)

      text6=Label(self, text="Tarikh keluar : August 27 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'maroon')
      text6.place(x=358, y=430)

      text7=Label(self, text="Pengedar        : Walt Disney Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'maroon')
      text7.place(x=358, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=_MC3XuMvsDI) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'maroon')
      text4.place(x=85, y=570)

  def onClose(self):
      self.destroy()
      self.original_frame.show()
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentJL(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Inside Out', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
########################################################################
########################################################################
########################################################################
########################################################################

class BMOtherFrameOthers(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='hotpink3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("movie.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Johnny English", command=self.OpenInFrameJoh,bg='orchid3', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=128,y=325)

      btn = Tk.Button(self, text="Inside Out",command=self.OpenInFrameJL, bg='plum3', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=398,y=325)
      
      load = Image.open("Johnny.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=105, y=90)

      load = Image.open("jl.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=385, y=105)
      
     # if self.txt=="Others":
      text=Label(self, text="Filem Lain-lain")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'light slate blue')
      text.place(x=250, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'SlateBlue3')
      text.place(x=60, y=40)


    #----------------------------------------------------------------------
  def OpenInFrameJoh(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameJoh(self)

  def OpenInFrameJL(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameJL(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
class BMOtherInFrameJur(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='CadetBlue3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)

      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("jur.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("jur1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="JURASSIC WORLD")
      text.config(font=('Arial Black',25))
      text.config(fg = 'cyan4')
      text.place(x=160, y=20)

      text=Label(self, text="Pengarah  :  Colin Trevorrow")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'dodger blue')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     :  Bryce Dallas Howard, Chris Pratt")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'dodger blue')
      text1.place(x=245, y=130)

      text2=Label(self, text="Sinopsis :  Resort mewah Jurassic World menyediakan")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=175)

      text2=Label(self, text="                  habitat untuk pelbagai dinosaur")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=195)

      text2=Label(self, text="                  kejuruteraan genetik, termasuk reaksi")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=215)

      text2=Label(self, text="                  Indominus yang ganas dan cerdik. Apabila")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=235)

      text2=Label(self, text="                  makhluk yang besar itu melarikan diri,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=255)

      text2=Label(self, text="                  ia mengetepikan tindak balas rantai yang")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=275)

      text2=Label(self, text="                  menyebabkan dinos menjalankan amok.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dodger blue')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Tempoh : 124 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'dodger blue')
      text3.place(x=245, y=328)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'dodger blue')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : October 6 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'dodger blue')
      text6.place(x=350, y=430)

      text7=Label(self, text="Pengedar        : Universal Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'dodger blue')
      text7.place(x=350, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=RFinNxS5KN4) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'dodger blue')
      text4.place(x=85, y=570)

  def hide(self):
      self.withdraw()

  def OpenInFramePayment(self):
      """"""
      self.hide()
      subFrame = BMPaymentJur(self)
      cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                     ('Jurassic World', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
class BMOtherInFramePre(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='sky blue', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("pre1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("pre2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="The Predator")
      text.config(font=('Arial Black',25))
      text.config(fg = 'MediumPurple1')
      text.place(x=180, y=20)

      text=Label(self, text="Pengarah  :  Shane Black")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'blue4')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     :  Olivia Munn, Alfie Allen, Thomas Jane")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'blue4')
      text1.place(x=245, y=130)

      text2=Label(self, text="Sinopsis :  Dari luar ruang angkasa ke jalan-jalan")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=175)

      text2=Label(self, text="                  kota kecil di suburbia, memburu pulang.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=195)

      text2=Label(self, text="                  Pemburu alam semesta yang paling maut ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=215)

      text2=Label(self, text="                  adalah lebih kuat, lebih bijak dan lebih ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=235)

      text2=Label(self, text="                  dahsyat daripada sebelumnya, dengan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=255)

      text2=Label(self, text="                  genetik menaik taraf diri mereka dengan")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=275)

      text2=Label(self, text="                  DNA dari spesies lain.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'blue4')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Tempoh : 118 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'blue4')
      text3.place(x=245, y=328)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'blue4')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : August 26 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'blue4')
      text6.place(x=350, y=430)

      text7=Label(self, text="Pengedar        : 20th Century Fox")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'blue4')
      text7.place(x=350, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=50_Ala5BKBo) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'blue4')
      text4.place(x=85, y=570)

  def hide(self):
      self.withdraw()

  def OpenInFramePayment(self):
      """"""
      self.hide()
      subFrame = BMPaymentPre(self)
      cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('The Predator', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
########################################################################
########################################################################

class BMOtherFrameAdventure(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='turquoise4', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("adventure.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Jurassic World",command=self.OpenInFrameJur, bg='CadetBlue3', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=118,y=285)

      btn = Tk.Button(self, text="The Predator", command=self.OpenInFramePre,bg='sky blue', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=388,y=285)
      
      load = Image.open("Jurassic.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=105, y=70)

      load = Image.open("pre.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=370, y=70)
      
     # if self.txt=="Adventure":
      text=Label(self, text="Filem Pengembaraan")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'turquoise4')
      text.place(x=250, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'turquoise3')
      text.place(x=60, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameJur(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameJur(self)

  def OpenInFramePre(self):
      """"""
      self.hide()
      subFrame = BMOtherInFramePre(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

class LoginSystem(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame=original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False,False)

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS user (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")

        # ================MAIN FUNCTIONS====================#

        def Login(event=None):
            if USERNAME.get() == '' or PASSWORD.get() == '':
                lbl_error.config(text='Please complete the required field!', fg='red')
            else:
                cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?",
                               (USERNAME.get(), PASSWORD.get()))
                data = cursor.fetchone()
                print(data[1])
                if data[1] == USERNAME.get() and data[2] == PASSWORD.get():
                    print("Successfully logged in!")
                    lbl_error.config(text="")
                    self.onClose()
                    global logined
                    logined=True
                else:
                    lbl_error.config(text="Invalid username or password", fg="red")

        def Sign_up(event=None):
            if USERNAME_1.get() == '' or PASSWORD_1.get() == '':
                lbl_error_1.config(text='Please complete the required field!', fg='red')
            else:
                cursor.execute("INSERT INTO user (username, password)VALUES(?,?)", (USERNAME_1.get(), PASSWORD_1.get()))
                db.commit()

        lbl_success = Label(self, text="Successfull\nLogin!", font=('Times New Roman', 20), width=30, bg='Gold3',
                            fg='red3')
        lbl_success.place(x=70, y=250)
        btn_back = Button(self, text='BACK', width=15, command=self.onClose)
        btn_back.place(x=230, y=400)
        canvas = Canvas(self, height=600, width=600)
        canvas.pack()
        main_bg = PhotoImage(file='scenery.png')
        canvas.create_image(0, 0, anchor=NW, image=main_bg)

        ## BIG LABEL

        lbl_title = Label(self, text='Welcome To Infinite Cinemas', font=('Aharoni', 25, 'bold'), bg='Gold3')
        lbl_title.place(x=70, y=30)

        ## LOGIN

        login_label = Label(text='---USER LOGIN---', font=('Arahoni', 18, 'bold'), bg='Gold3')
        login_label.place(x=200, y=150)

        lbl_username = Label(self, text="Username:", font=('Arial', 15), bg='goldenrod')
        lbl_username.place(x=70, y=213)

        lbl_password = Label(self, text="Password:", font=('Arial', 15), bg='goldenrod')
        lbl_password.place(x=70, y=253)

        USERNAME = Entry(self, textvariable='', font=(14))
        USERNAME.place(x=250, y=218)
        PASSWORD = Entry(self, textvariable='', show="*", font=(14))
        PASSWORD.place(x=250, y=255)

        lbl_error = Label(self)
        lbl_error.place(x=245, y=300)

        btn_login = Button(self, text="LOGIN", width=15, command=Login)
        btn_login.place(x=460, y=230)


        ## SIGN UP

        login_label_1 = Label(text='---USER SIGN UP---', font=('Arahoni', 18, 'bold'), bg='Gold3')
        login_label_1.place(x=200, y=400)

        lbl_username_1 = Label(self, text="Username:", font=('Arial', 15), bg='goldenrod')
        lbl_username_1.place(x=70, y=463)

        lbl_password_1 = Label(self, text="Password:", font=('Arial', 15), bg='goldenrod')
        lbl_password_1.place(x=70, y=503)

        USERNAME_1 = Entry(self, textvariable='', font=(14))
        USERNAME_1.place(x=250, y=470)
        PASSWORD_1 = Entry(self, show="*", textvariable='', font=(14))
        PASSWORD_1.place(x=250, y=507)

        btn_sign_up = Button(self, text="SIGN UP", width=15, command=Sign_up)
        btn_sign_up.place(x=460, y=490)


        lbl_error_1 = Label(self)
        lbl_error_1.place(x=245, y=560)



    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

    def onClose(self):
        self.destroy()
        self.original_frame.show()

class BMLoginSystem(Tk.Toplevel):

    def __init__(self, original):
        self.original_frame=original
        Tk.Toplevel.__init__(self)
        self.geometry("600x600")
        self.resizable(False,False)

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS user (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")

        # ================MAIN FUNCTIONS====================#

        def Login(event=None):
            if USERNAME.get() == '' or PASSWORD.get() == '':
                lbl_error.config(text='Sila masukkan maklumat dalam ruang kosong!', fg='red')
            else:
                cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?",
                               (USERNAME.get(), PASSWORD.get()))
                data = cursor.fetchone()
                print(data[1])
                if data[1] == USERNAME.get() and data[2] == PASSWORD.get():
                    print("Log Masuk Berjaya!")
                    lbl_error.config(text="")
                    self.onClose()
                    global logined
                    logined=True
                else:
                    lbl_error.config(text="Nama Pengguna atau Kata Laluan yang salah", fg="red")

        def Sign_up(event=None):
            if USERNAME_1.get() == '' or PASSWORD_1.get() == '':
                lbl_error_1.config(text='Sila masukkan maklumat dalam ruang kosong!', fg='red')
            else:
                cursor.execute("INSERT INTO user (username, password)VALUES(?,?)", (USERNAME_1.get(), PASSWORD_1.get()))
                db.commit()

        lbl_success = Label(self, text="Log Masuk \n Berjaya!", font=('Times New Roman', 20), width=30, bg='Gold3',
                            fg='red3')
        lbl_success.place(x=70, y=250)
        btn_back = Button(self, text='BACK', width=15, command=self.onClose)
        btn_back.place(x=230, y=400)
        canvas = Canvas(self, height=600, width=600)
        canvas.pack()
        main_bg = PhotoImage(file='scenery.png')
        canvas.create_image(0, 0, anchor=NW, image=main_bg)

        ## BIG LABEL

        lbl_title = Label(self, text='Selamat Datang Ke Pawagam Infiniti', font=('Aharoni', 20, 'bold'), bg='Gold3')
        lbl_title.place(x=70, y=30)

        ## LOGIN

        login_label = Label(text='---LOG MASUK---', font=('Arahoni', 18, 'bold'), bg='Gold3')
        login_label.place(x=200, y=150)

        lbl_username = Label(self, text="Nama Pengguna:", font=('Arial', 15), bg='goldenrod')
        lbl_username.place(x=70, y=213)

        lbl_password = Label(self, text="Kata Laluan:", font=('Arial', 15), bg='goldenrod')
        lbl_password.place(x=70, y=253)

        USERNAME = Entry(self, textvariable='', font=(14))
        USERNAME.place(x=250, y=218)
        PASSWORD = Entry(self, textvariable='', show="*", font=(14))
        PASSWORD.place(x=250, y=255)

        lbl_error = Label(self)
        lbl_error.place(x=245, y=300)

        btn_login = Button(self, text="LOG MASUK", width=15, command=Login)
        btn_login.place(x=460, y=230)


        ## SIGN UP

        login_label_1 = Label(text='---DAFTAR AKAUN---', font=('Arahoni', 18, 'bold'), bg='Gold3')
        login_label_1.place(x=200, y=400)

        lbl_username_1 = Label(self, text="Nama Pengguna:", font=('Arial', 15), bg='goldenrod')
        lbl_username_1.place(x=70, y=463)

        lbl_password_1 = Label(self, text="Kata Laluan:", font=('Arial', 15), bg='goldenrod')
        lbl_password_1.place(x=70, y=503)

        USERNAME_1 = Entry(self, textvariable='', font=(14))
        USERNAME_1.place(x=250, y=470)
        PASSWORD_1 = Entry(self, show="*", textvariable='', font=(14))
        PASSWORD_1.place(x=250, y=507)

        btn_sign_up = Button(self, text="DAFTAR", width=15, command=Sign_up)
        btn_sign_up.place(x=460, y=490)


        lbl_error_1 = Label(self)
        lbl_error_1.place(x=245, y=560)



    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

    def onClose(self):
        self.destroy()
        self.original_frame.show()

########################################################################      
class BMOtherInFrameBlind(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='SeaGreen3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      btn2 = Tk.Button(self, text="Beli sekarang!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("blinds.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("blinds2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="The Blind Side")
      text.config(font=('Arial Black',35))
      text.config(fg = 'medium sea green')
      text.place(x=200, y=20)

      text=Label(self, text="Pengarah  : John Lee Hancock")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'sea green')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Sandra Bullock, Quinton Aaron, Jae Head")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'sea green')
      text1.place(x=245, y=150)

      text2=Label(self, text="Sinopsis : Michael Oher adalah remaja hitam yang ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 tiada tempat tinggal, telah hanyut masuk")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 dan keluar dari sistem sekolah selama")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 bertahun-tahun. Leigh Anne Tuohy dan")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 suaminya, Sean, bawa dia masuk Tuohys")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 akhirnya menjadi penjaga Michael.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'sea green')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Tempoh : 113 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'sea green')
      text3.place(x=245, y=328)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'sea green')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : September 22 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'sea green')
      text6.place(x=350, y=430)

      text7=Label(self, text="Pengedar        : Warner Bros.")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'sea green')
      text7.place(x=350, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=gvqj_Tk_kuM) untuk Trailers.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'sea green')
      text4.place(x=85, y=570)
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentBlind(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('The Blind Side', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
########################################################################
########################################################################
########################################################################
      
class BMOtherFrameSport(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='SeaGreen3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("run.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="The Blind Side", command=self.OpenInFrameBlind,bg='lawn green', fg='black')
      btn.config(height = 3,  width = 17)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=308,y=225)

      
      load = Image.open("sport.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=75, y=80)

      
     # if self.txt=="Sport":
      text=Label(self, text="Filem Sukan")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'chartreuse4')
      text.place(x=250, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'chartreuse3')
      text.place(x=60, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameBlind(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameBlind(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class BMOtherInFrameW(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='sky blue', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("wonder.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("WONDER1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=385)

      text=Label(self, text="WONDER")
      text.config(font=('Britannic Bold',45))
      text.config(fg = 'deep sky blue')
      text.place(x=200, y=5)

      text=Label(self, text="Pengarah  : Stephen Chbosky")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'steel blue')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Julia Roberts, Owen Wilson, Nadji Jeter")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'steel blue')
      text1.place(x=245, y=150)

      text2=Label(self, text="Sinopsis : Berdasarkan buku terlaris New York Times,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 WONDER menceritakan kisah yang sangat ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 menginspirasi dan menyedihkan August ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 Pullman, seorang lelaki dengan perbezaan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 wajah yang memasuki kelas kelima, ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 menghadiri sekolah rendah aliran utama.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'steel blue')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Tempoh : 113 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'steel blue')
      text3.place(x=245, y=328)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'steel blue')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : September 29 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'steel blue')
      text6.place(x=350, y=430)

      text7=Label(self, text="Pengedar        : Lionsgate")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'steel blue')
      text7.place(x=350, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=ngiK1gQKgK8) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'steel blue')
      text4.place(x=85, y=570)

  def hide(self):
      self.withdraw()

  def OpenInFramePayment(self):
      """"""
      self.hide()
      subFrame = BMPaymentW(self)
      cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Wonder', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
########################################################################
########################################################################

class BMOtherFrameFamily(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='maroon3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("family.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Wonder", command=self.OpenInFrameW,bg='hot pink', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("W.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=145, y=80)
      
     # if self.txt=="Family":
      text=Label(self, text="Filem Keluarga")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'maroon3')
      text.place(x=250, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'maroon1')
      text.place(x=60, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameW(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameW(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class BMOtherInFrameBlack(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='SpringGreen3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("bp.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("bp1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=375)

      text=Label(self, text="Black Panther")
      text.config(font=('Britannic Bold',45))
      text.config(fg = 'goldenrod')
      text.place(x=140, y=5)

      text=Label(self, text="Pengarah  : Ryan Coogler")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'dark goldenrod')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Chadwick Boseman, Michael B. Jordan")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'dark goldenrod')
      text1.place(x=245, y=130)

      text2=Label(self, text="Sinopsis : Selepas kematian bapanya,T'Challa kembali")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=155)

      text2=Label(self, text="                 ke negara Afrika Wakanda untuk ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 mengambil tempatnya sebagai raja. Apabila ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 musuh yang kuat tiba-tiba muncul kembali,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 keberanian T'Challa sebagai raja dan  ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 sebagai Black Panther,akan diuji ketika dia")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 ditarik ke dalam konflik yang meletakkan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=275)

      text2=Label(self, text="                  nasib Wakanda berisiko.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'dark goldenrod')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Tempoh : 135 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'dark goldenrod')
      text3.place(x=245, y=328)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'dark goldenrod')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : October 13 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'dark goldenrod')
      text6.place(x=360, y=430)

      text7=Label(self, text="Pengedar        : Walt Disney Studios ")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'dark goldenrod')
      text7.place(x=360, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=dxWvtMOGAhw) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'dark goldenrod')
      text4.place(x=85, y=570)

  def hide(self):
      self.withdraw()

  def OpenInFramePayment(self):
      """"""
      self.hide()
      subFrame = BMPaymentBlack(self)
      cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Black Panther', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
########################################################################
########################################################################
########################################################################

class BMOtherFrameSuperhero(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='SpringGreen3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("s.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Black Panther",command=self.OpenInFrameBlack ,bg='green2', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("black.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=145, y=80)
      
     # if self.txt=="Superhero":
      text=Label(self, text="Filem Superhero")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'SpringGreen4')
      text.place(x=250, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'SpringGreen3')
      text.place(x=60, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameBlack(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameBlack(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################      
class BMOtherInFrameSMA(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='SteelBlue3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("small1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("small2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=375)

      text=Label(self, text="Small Foot")
      text.config(font=('Britannic Bold',45))
      text.config(fg = 'deep sky blue')
      text.place(x=150, y=5)

      text=Label(self, text="Pengarah  : Karey Kirkpatrick")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'RoyalBlue4')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : LeBron James, Zendaya, Channing Tatum")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'RoyalBlue4')
      text1.place(x=245, y=130)

      text2=Label(self, text="Sinopsis : Migo adalah Yeti yang mesra yang dunia ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=155)

      text2=Label(self, text="                 namun apabila dia mendapati sesuatu yang")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 tidak diketahuinya - manusia. Dia tidak")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 lama lagi akan mengalami masalah ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 pembuangan rumah dari rumah bersalji ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 apabila seluruh penduduk enggan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 mempercayai kisahnya yang hebat.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'RoyalBlue4')
      text2.place(x=245, y=275)

      text3=Label(self, text="Tempoh : 102 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'RoyalBlue4')
      text3.place(x=245, y=308)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'RoyalBlue4')
      text5.place(x=245, y=330)

      text6=Label(self, text="Tarikh keluar : September 8 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'RoyalBlue4')
      text6.place(x=360, y=430)

      text7=Label(self, text="Pengedar        : Warner Bros.")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'RoyalBlue4')
      text7.place(x=360, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=uBw6EvIxIS8) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'RoyalBlue4')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentSMA(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Smallfoot', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
########################################################################
########################################################################

class BMOtherFrameComedy(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='DeepSkyBlue2', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("c.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=330)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Smallfoot", command=self.OpenInFrameSMA,bg='SteelBlue3', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("small.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=165, y=80)

      
     # if self.txt=="Action":
      text=Label(self, text="Filem Komedi")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'DeepSkyBlue2')
      text.place(x=250, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'steel blue')
      text.place(x=60, y=40)
    #----------------------------------------------------------------------
  def OpenInFrameSMA(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameSMA(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
  def onClose(self):
      self.destroy()
      self.original_frame.show()
      

    #----------------------------------------------------------------------
  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class BMOtherInFramePHO(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='Plum2', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("a1.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("dark.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=390)

      text=Label(self, text="Dark Phoenix")
      text.config(font=('Andalus',45))
      text.config(fg = 'midnightblue')
      text.place(x=150, y=5)

      text=Label(self, text="Pengarah  : Simon Kinberg")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'midnightblue')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Sophie Turner, Jessica Chastain, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'midnightblue')
      text1.place(x=245, y=130)

      text1=Label(self, text="                    Jennifer Lawrence")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'midnightblue')
      text1.place(x=245, y=150)

      text2=Label(self, text="Sinopsis : X-Men menghadapi musuh yang paling kuat ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 apabila salah seorang mereka sendiri, Jean ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 Gray, mula keluar dari kawalan. Semasa ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 misi menyelamat di luar angkasa, Jean ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 hampir terbunuh apabila dia dilanda ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 angkatan kosmik misterius. Sebaik sahaja")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 dia pulang ke rumah, kuasa ini lebih")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=295)

      text2=Label(self, text="                 berkuasa tetapi tidak stabil.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'midnightblue')
      text2.place(x=245, y=315)
      
      text3=Label(self, text="Tempoh : 138 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'midnightblue')
      text3.place(x=245, y=338)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'midnightblue')
      text5.place(x=245, y=360)

      text6=Label(self, text="Tarikh keluar :  October 13 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'midnightblue')
      text6.place(x=370, y=430)

      text7=Label(self, text="Pengedar        : 20th Century Fox")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'midnightblue')
      text7.place(x=370, y=450)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=uup2JFXH68g) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'midnightblue')
      text4.place(x=85, y=570)
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentPHO(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Dark Phoenix', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################  
########################################################################
########################################################################      
########################################################################

class BMOtherFrameAction(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='Plum3', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      load = Image.open("action.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=0, y=330)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Dark Phoenix", command=self.OpenInFramePHO,bg='Plum2', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("a.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=165, y=80)

      
     # if self.txt=="Action":
      text=Label(self, text="Filem Aksi")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'mediumpurple3')
      text.place(x=250, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'Plum4')
      text.place(x=60, y=40)
    #----------------------------------------------------------------------
  def OpenInFramePHO(self):
      """"""
      self.hide()
      subFrame = BMOtherInFramePHO(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class BMOtherInFrameARRIVAL(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='grey60', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      btn2 = Tk.Button(self, text="Beli sekarang!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("arrival1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("arrival2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      text=Label(self, text="Arrival")
      text.config(font=('Andalus',50))
      text.config(fg = 'grey60')
      text.place(x=240, y=5)

      text=Label(self, text="Pengarah  : Denis Villeneuve")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Amy Adams, Jeremy Renner, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=130)

      text1=Label(self, text="                    Forest Whitaker")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text2=Label(self, text="Sinopsis : Profesor linguistik Louise Banks mengetuai")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 pasukan elit penyiasat apabila kapal ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 angkasa raksasa menyentuh di 12 lokasi di")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 seluruh dunia. Memandangkan negara yang")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 menghadapi krisis global,Bank dan krewnya")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 mesti berlumba-lumba dengan masa untuk")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 mencari jalan.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Tempoh : 118 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=320)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : October 6 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=360, y=430)

      text7=Label(self, text="Pengedar        : Paramount")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=450)

      text7=Label(self, text="                         Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=470)


      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=tFMo3UJ4B4g) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentARRIVAL(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Arrival', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))


  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
      
########################################################################
########################################################################      
########################################################################

class BMOtherFrameSciFi(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='grey82', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

      #back image
      load = Image.open("fu.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=20, y=430)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Arrival", command=self.OpenInFrameARRIVAL,bg='grey60', fg='black')
      btn.config(height = 3,  width = 20)
      btn.config(font=('Britannic Bold',13))
      btn.place(x=388,y=285)

      
      load = Image.open("arri.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=105, y=80)

      
      
     # if self.txt=="Sci-Fi":
      text=Label(self, text="Filem Sci-Fi")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'grey18')
      text.place(x=250, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'grey50')
      text.place(x=60, y=40)
      
    #----------------------------------------------------------------------
  def OpenInFrameARRIVAL(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameARRIVAL(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class BMOtherInFrameLA(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='medium orchid', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("LaLa1.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("LaLa2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      text=Label(self, text="LA LA LAND")
      text.config(font=('Rockwell Condensed',40))
      text.config(fg = 'medium orchid')
      text.place(x=190, y=15)

      text=Label(self, text="Pengarah  : Damien Chazelle")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Emma Stone, Ryan Gosling, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=130)

      text1=Label(self, text="                    John Legend")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text2=Label(self, text="Sinopsis : Sebastian and Mia ditarik bersama dengan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=175)

      text2=Label(self, text="                 hasrat bersama mereka untuk melakukan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=195)

      text2=Label(self, text="                 apa yang mereka suka. Tetapi sebagai ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=215)

      text2=Label(self, text="                 kejayaan melangkah mereka dihadapkan")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=235)

      text2=Label(self, text="                 dengan keputusan yang mula meremehkan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=255)

      text2=Label(self, text="                 kain yang rapuh dalam hubungan cinta ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=275)

      text2=Label(self, text="                 mereka.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=295)
      
      text3=Label(self, text="Tempoh : 128 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=320)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : September 8 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=360, y=430)

      text7=Label(self, text="Pengedar        : Summit")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=450)

      text7=Label(self, text="                         Entertainment")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=470)


      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=0pdqf4P9MB8) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentLA(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('La La Land', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################      
class BMOtherInFrameNAP(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='hot pink', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)

      btn2 = Tk.Button(self, text="Beli sekarang!", command=self.OpenInFramePayment, bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)

      load = Image.open("nap1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("nap2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      text=Label(self, text="NAPPILY ever AFTER")
      text.config(font=('Britannic Bold',30))
      text.config(fg = 'hot pink')
      text.place(x=160, y=35)

      text=Label(self, text="Pengarah  : Haifaa al-Mansour")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Sanaa Lathan, Ernie Hudson, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text1=Label(self, text="                 Lynn Whitfield")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=170)

      text2=Label(self, text="Sinopsis :  Seorang tukang gunting rambut membantu seorang")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=220)

      text2=Label(self, text="                 wanita memotong hidupnya bersama-sama")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=240)

      text2=Label(self, text="                 selepas kecelakaan di salon rambutnya ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=260)

      text2=Label(self, text="                 membuatnya menyedari bahawa dia tidak ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=280)

      text2=Label(self, text="                 hidup sebenarnya.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=300)


      text3=Label(self, text="Tempoh : 98 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=330)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : September 22 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=360, y=430)

      text7=Label(self, text="Pengedar        : Netflix")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=450)



      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=3xh9XFxo2Hg) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentNAP(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('Nappily Ever After', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))


  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################
########################################################################
########################################################################      
########################################################################

class BMOtherFrameRomance(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='medium orchid', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     # print(self.original_frame.text)

       #back image
      load = Image.open("love.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=20, y=350)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="Nappily Ever After",command=self.OpenInFrameNAP, bg='HotPink1', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=118,y=285)

      btn = Tk.Button(self, text="La La Land", command=self.OpenInFrameLA,bg='medium orchid', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=388,y=285)
      
      load = Image.open("nap.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=115, y=100)

      load = Image.open("La.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=385, y=100)
      
     # if self.txt=="Romance":
      text=Label(self, text="Filem Cinta")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'deep pink')
      text.place(x=220, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'RosyBrown4')
      text.place(x=60, y=40)
 
    #----------------------------------------------------------------------
  def OpenInFrameNAP(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameNAP(self)

  def OpenInFrameLA(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameLA(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   

  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################
class BMOtherInFrameNun(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='sky blue', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      btn2 = Tk.Button(self, text="Beli sekarang!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
      load = Image.open("TheNun1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("TheNun2.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      text=Label(self, text="THE NuN")
      text.config(font=('Britannic Bold',40))
      text.config(fg = 'Gold3')
      text.place(x=300, y=35)

      text=Label(self, text="Pengarah  : Corin Hardy")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Taissa Farmiga, Demián Bichir, ")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=130)

      text1=Label(self, text="                    Charlotte Hope")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text2=Label(self, text="Sinopsis : Selepas kematian misteri seorang biarawati ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=170)

      text2=Label(self, text="                 muda di biara yang terpencil di Romania,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=190)

      text2=Label(self, text="                 seorang pastor yang dihantui ditugaskan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=210)

      text2=Label(self, text="                 untuk melihat perkara itu.Bersama novitiat,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=230)

      text2=Label(self, text="                 kedua-dua mendedahkan rahsia itu.Mereka")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=250)

      text2=Label(self, text="                 kemudian akan membahayakan nyawa, ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=270)

      text2=Label(self, text="                 iman dan jiwa mereka untuk menghadapi ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=290)

      text2=Label(self, text="                 kuasa biarawati jahat.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=310)

      text3=Label(self, text="Tempoh : 96 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=330)

      text5=Label(self, text="Bahasa  : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=245, y=350)

      text6=Label(self, text="Tarikh keluar : September 29 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=360, y=430)

      text7=Label(self, text="Pengedar        : Warner Bros.")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=450)

      text7=Label(self, text="                         Pictures")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=360, y=470)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=pzD9zGcUNrw) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)

  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentNun(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('The Nun', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))


  def onClose(self):
      self.destroy()
      self.original_frame.show()

########################################################################      
class BMOtherInFrameIT(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
      #Details
      load = Image.open("It2.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=100)

      load = Image.open("It1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=380)

      load = Image.open("It3.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=300, y=20)

      text=Label(self, text="Pengarah  : Andy Muschietti")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'black')
      text.place(x=245, y=110)

      text1=Label(self, text="Pelakon     : Jaeden Lieberher, Jeremy Ray Taylor,")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=130)

      text1=Label(self, text="                    Sophia Lillis, Finn Wolfhard, Jake Sim...")
      text1.config(font=('Britannic Bold',11))
      text1.config(fg = 'black')
      text1.place(x=245, y=150)

      text2=Label(self, text="Sinopsis : Tujuh orang buangan muda di Derry, Maine ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=170)

      text2=Label(self, text="                 , akan menghadapi perkara yang amat")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=190)

      text2=Label(self, text="                 menakutkan. Bentuk-pergeseran kejahatan ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=210)

      text2=Label(self, text="                 yang muncul dari pembentung setiap 27 ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=230)

      text2=Label(self, text="                 tahun untuk menjadi mangsa kanak-kanak ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=250)

      text2=Label(self, text="                 di bandar. Menggabungkan bersama  ")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=270)

      text2=Label(self, text="                 sepanjang musim panas yang mengerikan,")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=290)

      text2=Label(self, text="                 para sahabat mesti mengatasi ketakutan")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=310)

      text2=Label(self, text="                 mereka.")
      text2.config(font=('Britannic Bold',11))
      text2.config(fg = 'black')
      text2.place(x=245, y=330)

      text3=Label(self, text="Tempoh : 130 minit")
      text3.config(font=('Britannic Bold',11))
      text3.config(fg = 'black')
      text3.place(x=245, y=350)

      text5=Label(self, text="Bahasa           : Inggeris")
      text5.config(font=('Britannic Bold',11))
      text5.config(fg = 'black')
      text5.place(x=380, y=410)

      text6=Label(self, text="Tarikh keluar : October 6 , 2018")
      text6.config(font=('Britannic Bold',11))
      text6.config(fg = 'black')
      text6.place(x=380, y=430)

      text7=Label(self, text="Pengedar        : Warner Bros.")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=380, y=450)

      text7=Label(self, text="                         Television")
      text7.config(font=('Britannic Bold',11))
      text7.config(fg = 'black')
      text7.place(x=380, y=470)

      text4=Label(self, text="Cari (https://www.youtube.com/watch?v=xKJmEC5ieOk) untuk Trailer.")
      text4.config(font=('Britannic Bold',11))
      text4.config(fg = 'black')
      text4.place(x=85, y=570)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='aquamarine', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      btn2 = Tk.Button(self, text="Beli sekarang!",command=self.OpenInFramePayment,bg='yellow', fg='black')
      btn2.config(height=2, width=15)
      btn2.config(font=('Britannic Bold', 11))
      btn2.place(x=10, y=10)
      #btn.pack(side="bottom",padx=6,pady=8)
  def hide(self):
        self.withdraw()

  def OpenInFramePayment(self):
        """"""
        self.hide()
        subFrame = BMPaymentIT(self)
        cursor.execute('''INSERT INTO tickets(movie,cinema,date,time,payment,name,email,mobile,passport,adult,children,oku,senior,popcorn,drinks,seating,price) 
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       ('IT', None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None))

  def onClose(self):
      self.destroy()
      self.original_frame.show()
########################################################################

class BMOtherFrameHorror(Tk.Toplevel):
 
    #----------------------------------------------------------------------
#  def __init__(self):
  def __init__(self,original):
     #   """Constructor"""
      self.original_frame=original      
      Tk.Toplevel.__init__(self)
      self.geometry("600x600")
      self.resizable(False,False)
       # self.title("otherFrame")
      btn = Tk.Button(self, text="Kembali", command=self.onClose,bg='CadetBlue1', fg='black')
      btn.config(height = 2,  width = 15)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=415,y=505)
      #btn.pack(side="bottom",padx=6,pady=8)
     
      
     #back image
      load = Image.open("water.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=50, y=300)

    # print(self.original_frame.text)
      btn = Tk.Button(self, text="It", command=self.OpenInFrameIT,bg='aquamarine', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=118,y=285)

      btn = Tk.Button(self, text="The Nun",command=self.OpenInFrameNun, bg='sky blue', fg='black')
      btn.config(height = 2,  width = 13)
      btn.config(font=('Britannic Bold',11))
      btn.place(x=388,y=285)
      
      load = Image.open("It.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=115, y=100)

      load = Image.open("TheNun.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=385, y=100)

      

     # if self.txt=="Horror":
      text=Label(self, text="Filem Seram")
      text.config(font=('Britannic Bold',18))
      text.config(fg = 'RoyalBlue')
      text.place(x=240, y=0)

      text=Label(self, text="Sila tekan filem yang anda suka untuk maklumat lanjut atau membeli tiket.")
      text.config(font=('Britannic Bold',11))
      text.config(fg = 'cornflowerblue')
      text.place(x=60, y=40)
      #----------------------------------------------------------------------
  def OpenInFrameIT(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameIT(self)

  def OpenInFrameNun(self):
      """"""
      self.hide()
      subFrame = BMOtherInFrameNun(self)

  def hide(self):
      self.withdraw()
      
  def show(self):
      self.update()
      self.deiconify()   
    #----------------------------------------------------------------------
  def onClose(self):
      self.destroy()
      self.original_frame.show()


    
########################################################################
######################################################################## 
########################################################################
class BMMovieSelection (Tk.Toplevel):
  
#  def __init__(self, master):
  def __init__(self, original):
      
#      Frame.__init__(self, master)
      self.original_frame = original
      Tk.Toplevel.__init__(self)
      self.geometry("800x800")
      self.resizable(False, False)


      
      buttonframe = Frame(self)
      container = Frame(self)
      buttonframe.pack(side="top", fill="x", expand=False)
      container.pack(side="top", fill="both", expand=True)
     
      BMEX = BMExit(self)
      BMEX.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
     
      
      load = Image.open("text.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=-75, y=60)



      text4=Label(self, text="Filem Teratas Minggu ini:")
      text4.config(font=('Britannic Bold',18))
      text4.config(fg = 'SlateBlue4')
      text4.place(x=505, y=73)


      load = Image.open("blackpanther.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=535, y=130)
      load = Image.open("topmovie.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=35, y=70)

      load = Image.open("topmovie1.jpg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=195, y=70)








      load = Image.open("pop.jpeg")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=10, y=580)

      load = Image.open("exit.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=670, y=630)

      HorrorButton = Button(self, text="Seram",command=self.openFrameHorror , bg='deep sky blue', fg='black')
      HorrorButton.config(height = 2,  width = 15)
      HorrorButton.config(font=('Britannic Bold',10))
      HorrorButton.place(x=205, y=415)

      RomanceButton = Button(self, text="Cinta",command=self.openFrameRomance,bg = 'HotPink2', fg='black')
      RomanceButton.config(height = 2,  width = 15)
      RomanceButton.config(font=('Britannic Bold',10))
      RomanceButton.place(x=460, y=415)

      ScifiButton = Button(self, text="Sci-Fi",command=self.openFrameSciFi,bg = 'Olivedrab1', fg='black')
      ScifiButton.config(height = 2,  width = 15)
      ScifiButton.config(font=('Britannic Bold',10))
      ScifiButton.place(x=205, y=465)

      ActionButton = Button(self, text="Aksi",command=self.openFrameAction,bg = 'MediumOrchid2', fg='black')
      ActionButton.config(height = 2,  width = 15)
      ActionButton.config(font=('Britannic Bold',10))
      ActionButton.place(x=460, y=465)

      ComedyButton = Button(self, text="Komedi",command=self.openFrameComedy,bg = 'Coral1', fg='black')
      ComedyButton.config(height = 2,  width = 15)
      ComedyButton.config(font=('Britannic Bold',10))
      ComedyButton.place(x=460, y=515)

      SPheroButton = Button(self, text="Superhero",command=self.openFrameSuperhero,bg = 'Seagreen1', fg='black')
      SPheroButton.config(height = 2,  width = 15)
      SPheroButton.config(font=('Britannic Bold',10))
      SPheroButton.place(x=205, y=515)

      FamilyButton = Button(self, text="Keluarga",command=self.openFrameFamily,bg = 'hot pink', fg='black')
      FamilyButton.config(height =2 ,  width = 15)
      FamilyButton.config(font=('Britannic Bold',10))
      FamilyButton.place(x=460, y=565)

      SportButton = Button(self, text="Sukan",command=self.openFrameSport,bg = 'SpringGreen3', fg='black')
      SportButton.config(height = 2,  width = 15)
      SportButton.config(font=('Britannic Bold',10))
      SportButton.place(x=205, y=565)

      AdventureButton = Button(self, text="Pengembaraan",command=self.openFrameAdventure,bg = 'LightSkyBlue2', fg='black')
      AdventureButton.config(height = 2,  width = 15)
      AdventureButton.config(font=('Britannic Bold',10))
      AdventureButton.place(x=205, y=615)

      OthersButton = Button(self, text="Lain-lain",command=self.openFrameOthers,bg = 'Plum2', fg='black')
      OthersButton.config(height = 2,  width = 15)
      OthersButton.config(font=('Britannic Bold',10))
      OthersButton.place(x=460, y=615)

      EXButton = Button(self, text="Keluar",command=BMEX.lift,bg = 'MistyRose2', fg='black')
      EXButton.config(height = 2,  width = 15)
      EXButton.config(font=('Britannic Bold',10))
      EXButton.place(x=670, y=740)

      LoginButton = Button(self, text="Log Masuk",command=self.openFramelogin,bg = 'MistyRose2', fg='black')
      LoginButton.config(height = 2,  width = 15)
      LoginButton.config(font=('Britannic Bold',10))
      LoginButton.place(x=670, y=20)

      ProButton = Button(self, text="Promosi",command=self.openFramePro,bg = 'MistyRose2', fg='black')
      ProButton.config(height = 2,  width = 15)
      ProButton.config(font=('Britannic Bold',10))
      ProButton.place(x=10, y=740)

      

      
      text=Label(self, text="Pawagam Infiniti")
      text.config(font=('Britannic Bold',14))
      text.config(fg = 'SlateBlue4')
      text.place(x=75, y=23)





      load = Image.open("infinity1.png")
      render = ImageTk.PhotoImage(load)
      img = Label(self, image=render)
      img.image = render
      img.place(x=10, y=10)



      text1=Label(self, text="Sila pilih jenis movie yang didapati.")
      text1.config(font=('Britannic Bold',15))
      text1.config(fg = 'SlateBlue3')
      text1.place(x=235, y=375)

      text2=Label(self, text=" Kemungkinan infiniti, Kepuasan infiniti. ")
      text2.config(font=('Britannic Bold',20))
      text2.config(bg = 'light blue',fg = 'MediumPurple4')
      text2.place(x=145, y=745)



  #----------------------------------------------------------------------
  def hide(self):
    self.withdraw()
 
    #----------------------------------------------------------------------
  def openFrameHorror(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameHorror(self)
    #----------------------------------------------------------------------
  def openFrameRomance(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameRomance(self)
    #----------------------------------------------------------------------
  def openFrameSciFi(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameSciFi(self)

    #----------------------------------------------------------------------
  def openFrameAction(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameAction(self)

    #----------------------------------------------------------------------
  def openFrameComedy(self):
      """"""  
      self.hide()
      subFrame = BMOtherFrameComedy(self)

    #----------------------------------------------------------------------

  def openFrameSuperhero(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameSuperhero(self)

    #----------------------------------------------------------------------

  def openFrameFamily(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameFamily(self)

    #----------------------------------------------------------------------
  def openFrameSport(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameSport(self)

    #----------------------------------------------------------------------

  def openFrameAdventure(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameAdventure(self)

    #----------------------------------------------------------------------

  def openFrameOthers(self):
      """"""
      self.hide()
      subFrame = BMOtherFrameOthers(self)

    #----------------------------------------------------------------------
  def openFramePro(self):
      """"""
      self.hide()
      subFrame = BMOtherFramePro(self)

    #----------------------------------------------------------------------
  def openFramelogin(self):
      """"""
      self.hide()
      subFrame = BMLoginSystem(self)

    #----------------------------------------------------------------------
  def show(self):
    self.update()
    self.deiconify()
 
 
#----------------------------------------------------------------------




class BMExit(Frame):
  def __init__ (self, master=None):
      Frame.__init__(self, master)
      self.master = master
      self.pack(fill=BOTH, expand=1)
      
      text3=Label(self, text="Terima kasih")
      text3.config(font=('Britannic Bold',25))
      text3.config(fg = 'purple4')
      text3.place(x=320, y=320)



#####################################################################
#####################################################################
#####################################################################
      
class StartPage(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.root = parent

        # Changing the title of our master widget
        self.master.title("Infinity Cinema")

        # Allowing the widget to take the MovieSelectionfull space of the root window
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master, bd=5)
        self.master.config(bg='#2A2C2B', menu=menu)

        #  file = Menu(menu)

        #  menu.add_cascade(label="File", menu=file)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        # Creating a button instance
        EngButton = Button(self, text="English", command=self.openFrameMovieSelection, bg='blue', fg='white')
        EngButton.config(height=2, width=17)
        EngButton.config(font=('Aharoni', 15))

        # Placing the button on my window
        EngButton.place(x=60, y=450)
        
        BMButton = Button(self, text="Bahasa Melayu", command=self.openFrameBMMovieSelection, bg='green', fg='white')
        BMButton.config(height=2, width=17)
        BMButton.config(font=('Aharoni', 15))


        # Placing the button on my window
        BMButton.place(x=335, y=450)

        load = Image.open("infinity.png")
        load.resize((200, 200)).save('infinity.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=200, y=40)

        text = Label(self, text="Welcome to Infinity Cinema!")
        text.config(font=('Arial Black', 15))
        text.place(x=135, y=220)
        text2 = Label(self, text="Selamat Datang ke Pawagam Infiniti!")
        text2.config(font=('Arial Black', 15))
        text2.place(x=100, y=250)

        text3 = Label(self, text="Please select your desired language.")
        text3.config(font=('Arial Black', 15))
        text3.place(x=100, y=320)
        text4 = Label(self, text="Sila memilih bahasa yang anda ingini.")
        text4.config(font=('Arial Black', 15))
        text4.place(x=100, y=350)

    # ----------------------------------------------------------------------
    def hide(self):
        self.root.withdraw()

        # ----------------------------------------------------------------------

    def openFrameMovieSelection(self):
        """"""
        self.hide()
        subFrame = MovieSelection(self)

    def openFrameBMMovieSelection(self):
        """"""
        self.hide()
        subFrame = BMMovieSelection(self)


    def show(self):
        self.root.update()
        self.root.deiconify()
 
 
#----------------------------------------------------------------------



class Exit(Frame):
  def __init__ (self, master=None):
      Frame.__init__(self, master)
      self.master = master
      self.pack(fill=BOTH, expand=1)
      
      text3=Label(self, text="Thank you")
      text3.config(font=('Britannic Bold',25))
      text3.config(fg = 'purple4')
      text3.place(x=320, y=320)
#----------------------------------------------------------------------


      

  

      

root = Tk.Tk()
root.resizable(False,False)
root.geometry("600x600")
app = StartPage(root)
root.mainloop()

db.commit()
db.close()


      
        

