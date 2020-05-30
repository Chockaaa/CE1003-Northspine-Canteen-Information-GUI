import tkinter as tk
from tkinter import ttk
from tkinter import *
import sys
from PIL import Image,ImageTk
from time import strftime
from datetime import date
from datetime import datetime
from tkcalendar import *
import calendar


############################################################################################################
class northspineapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.geometry("600x400")
        self.title("NorthSpine Canteen")
        self.resizable(False, False)

        self.frames={}
        for F in (startpage,currentstall,futurestalls,promocode):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(startpage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

        

############################################################################################################
class startpage(tk.Frame):#Initialize home page
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.parent=parent
        self.init_window(controller)

    def init_window(self,controller):
        night=Image.open("NSbackground.png")#insert background image
        render1=ImageTk.PhotoImage(night)
        img=Label(self,image=render1)
        img.image=render1
        img.place(x=0,y=0)
        
        label=Label(self,text="NTU NORTHSPINE CANTEEN SYSTEM",font=heading)
        label.pack(pady=10,padx=10)
        label.place(x=300,y=50,anchor="center")

        button1=ttk.Button(self,text="STALLS IN OPERATION",command=lambda:controller.show_frame(currentstall))#button
        button1.pack()
        button1.place(x=300,y=150,anchor="center",width=160,height=50)

        button2=ttk.Button(self,text="STALL INFO BY DATE",command=lambda:controller.show_frame(futurestalls))#button 
        button2.pack()
        button2.place(x=300,y=210,anchor="center",width=160,height=50)

        button3=ttk.Button(self,text="VERIFY PROMOTION CODE",command=lambda:controller.show_frame(promocode))#button
        button3.pack()
        button3.place(x=300,y=270,anchor="center",width=160,height=50)

        button4=ttk.Button(self,text="EXIT",command=self.client_exit)#exit application
        button4.pack()
        button4.place(x=300,y=330,anchor="center",width=160,height=50)


        def time():
            self.checktime=strftime('%d/%m/%Y %H:%M:%S %p')#real-time update
            lbl.config(text=self.checktime)
            lbl.after(1000,time)

        lbl = Label(self, font = timefont)
        lbl.pack()
        lbl.place(x=300,y=100,anchor="center")
        time()

    def client_exit(self):
        exit()
        
        
        
        
############################################################################################################
class currentstall(tk.Frame):#View stalls based on current time
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        night=Image.open("NSbackground.png")#insert background image
        render1=ImageTk.PhotoImage(night)
        img=Label(self,image=render1)
        img.image=render1
        img.place(x=0,y=0)        
        label=tk.Label(self,text="Viewing Current Stalls in Operation",font=heading)
        label.pack(pady=10,padx=10)
        label.place(x=300,y=20,anchor="center")
                
        

        alphabutton1=ttk.Button(self,text="Home",command=lambda:controller.show_frame(startpage))#return to home
        alphabutton1.pack()
        alphabutton1.place(x=300,y=380,anchor="center",width=120)

        alphabutton2=ttk.Button(self,text="Operating Hours",command=lambda:popupmsg(hours))#check Operating Hours
        alphabutton2.pack()
        alphabutton2.place(x=130,y=80,anchor="center",width=120)


        currentday=date.today().strftime("%A").upper()
        hourcheck=int(datetime.now().strftime("%H"))#current time

        if currentday in weekday:#check the time and display the stalls open accordingly
            if hourcheck>=0 and hourcheck<=6:
                self.close()
            elif hourcheck>=7 and hourcheck<=11:
                self.breakfast("BREAKFAST MENU")
            elif hourcheck>=11 and hourcheck<21:
                self.lunch("LUNCH-DINNER MENU")
            else:
                self.close()
        elif currentday in weekend:
            if hourcheck>=0 and hourcheck<=6:
                self.close()
            elif hourcheck>=7 and hourcheck<=11:
                self.breakfast("BREAKFAST MENU")
            elif hourcheck>=11 and hourcheck<15:
                self.lunch("LUNCH-DINNER MENU")
            else:
                self.close()
        else:
            self.close()

    def close(self):#display when stall is closed
        closedpop=tk.Label(self,text=closeprint,font=fuzzy)
        closedpop.pack()
        closedpop.place(x=300,y=150,anchor="center")
        return
    
    def breakfast(self,timeref):#display for breakfast menu
        menutype1=tk.Label(self,text="BREAKFAST STALLS",font=fuzzy)
        menutype1.pack()
        menutype1.place(x=300,y=80,anchor="center",width=200)
        
        breakwok=ttk.Button(self,text="MINI WOK",command=lambda:printmenubreak("MINIWOK",timeref,1))#button 0/1
        breakwok.pack()
        breakwok.place(x=300,y=120,anchor="center",width=120)

        breakveg=ttk.Button(self,text="VEGETERIAN",command=lambda:printmenubreak('VEGETERIAN',timeref,1))#button 4/6
        breakveg.pack()
        breakveg.place(x=300,y=160,anchor="center",width=120)

        breakwest=ttk.Button(self,text="WESTERN",command=lambda:printmenubreak('WESTERN',timeref,1))#button 8/9
        breakwest.pack()
        breakwest.place(x=300,y=200,anchor="center",width=120)

        breakmalay=ttk.Button(self,text="MALAY BBQ",command=lambda:printmenubreak('MALAY BBQ',timeref,1))#button 12/13
        breakmalay.pack()
        breakmalay.place(x=300,y=240,anchor="center",width=120)

        breakindian=ttk.Button(self,text="INDIAN CUISINE",command=lambda:printmenubreak('INDIAN CUISINE',timeref,1))#button 16/17
        breakindian.pack()
        breakindian.place(x=300,y=280,anchor="center",width=120)

        breakdrinks=ttk.Button(self,text="DRINKS",command=lambda:printmenubreak('DRINKS',timeref,1))#button 20/21
        breakdrinks.pack()
        breakdrinks.place(x=300,y=320,anchor="center",width=120)
        return

    def lunch(self,timeref):#display for lunch menu
        menutype2=tk.Label(self,text="LUNCH DINNER STALLS",font=fuzzy)
        menutype2.pack()
        menutype2.place(x=300,y=80,anchor="center",width=200)
        
        lunchwok=ttk.Button(self,text="MINI WOK",command=lambda:printmenubreak("MINIWOK",timeref,1))#2/3
        lunchwok.pack()
        lunchwok.place(x=300,y=120,anchor="center",width=120)

        lunchveg=ttk.Button(self,text="VEGETERIAN",command=lambda:printmenubreak('VEGETERIAN',timeref,1))#6/7
        lunchveg.pack()
        lunchveg.place(x=300,y=160,anchor="center",width=120)

        lunchwest=ttk.Button(self,text="WESTERN",command=lambda:printmenubreak('WESTERN',timeref,1))#10/11
        lunchwest.pack()
        lunchwest.place(x=300,y=200,anchor="center",width=120)

        lunchmalay=ttk.Button(self,text="MALAY BBQ",command=lambda:printmenubreak('MALAY BBQ',timeref,1))#14/15
        lunchmalay.pack()
        lunchmalay.place(x=300,y=240,anchor="center",width=120)

        lunchindian=ttk.Button(self,text="INDIAN CUISINE",command=lambda:printmenubreak('INDIAN CUISINE',timeref,1))#18/19
        lunchindian.pack()
        lunchindian.place(x=300,y=280,anchor="center",width=120)

        lunchdrinks=ttk.Button(self,text="DRINKS",command=lambda:printmenubreak('DRINKS',timeref,1))#22/23
        lunchdrinks.pack()
        lunchdrinks.place(x=300,y=320,anchor="center",width=120)
        return   
        
            


        
############################################################################################################
class futurestalls(tk.Frame):#Check future stall timing
    def __init__(self,parent,controller):#insert background
        tk.Frame.__init__(self,parent)
        night=Image.open("NSbackground.png")
        render1=ImageTk.PhotoImage(night)
        img=Label(self,image=render1)
        img.image=render1
        img.place(x=0,y=0)
        
        label=tk.Label(self,text="Viewing Stall Information by Date",font=heading)
        label.pack(pady=10,padx=10)
        label.place(x=300,y=20,anchor="center")

        bravobutton3=ttk.Button(self,text="Choose the time",command=lambda:self.cal_func())#button to choose the time
        bravobutton3.pack()
        bravobutton3.place(x=250,y=50,anchor="center",width=120)
  
        
        bravobutton1=ttk.Button(self,text="Home",command=lambda:controller.show_frame(startpage))#go back to start page
        bravobutton1.pack()
        bravobutton1.place(x=300,y=380,anchor="center",width=120)

        bravobutton2=ttk.Button(self,text="Operating Hours",command=lambda:popupmsg(hours))#check operating hours
        bravobutton2.pack()
        bravobutton2.place(x=70,y=20,anchor="center",width=120)

    def close(self):#display if stall is closed
        closedpop=tk.Label(self,text=closeprint,font=fuzzy)
        closedpop.pack()
        closedpop.place(x=300,y=150,anchor="center")

        clear=ttk.Button(self,text="CLEAR",command=lambda:delete())#button to clear the screen
        clear.pack()
        clear.place(x=250,y=50,anchor="center",width=120)

        def delete():#clearing the screen
            closedpop.destroy()
            clear.destroy()
        return
    
    def breakfast(self,timeref):#DISPLAY STALLS OPEN FOR BREAKFAST
        menutype1=tk.Label(self,text="BREAKFAST STALLS",font=fuzzy)
        menutype1.pack()
        menutype1.place(x=300,y=80,anchor="center",width=200)
        
        breakwok=ttk.Button(self,text="MINI WOK",command=lambda:printmenubreak("MINIWOK",timeref))#0/1
        breakwok.pack()
        breakwok.place(x=300,y=120,anchor="center",width=120)

        breakveg=ttk.Button(self,text="VEGETERIAN",command=lambda:printmenubreak('VEGETERIAN',timeref))#4/6
        breakveg.pack()
        breakveg.place(x=300,y=160,anchor="center",width=120)

        breakwest=ttk.Button(self,text="WESTERN",command=lambda:printmenubreak('WESTERN',timeref))#8/9
        breakwest.pack()
        breakwest.place(x=300,y=200,anchor="center",width=120)

        breakmalay=ttk.Button(self,text="MALAY BBQ",command=lambda:printmenubreak('MALAY BBQ',timeref))#12/13
        breakmalay.pack()
        breakmalay.place(x=300,y=240,anchor="center",width=120)

        breakindian=ttk.Button(self,text="INDIAN CUISINE",command=lambda:printmenubreak('INDIAN CUISINE',timeref))#16/17
        breakindian.pack()
        breakindian.place(x=300,y=280,anchor="center",width=120)

        breakdrinks=ttk.Button(self,text="DRINKS",command=lambda:printmenubreak('DRINKS',timeref))#20/21
        breakdrinks.pack()
        breakdrinks.place(x=300,y=320,anchor="center",width=120)
        
        clear=ttk.Button(self,text="CLEAR",command=lambda:delete())
        clear.pack()
        clear.place(x=250,y=50,anchor="center",width=120)

        def delete():#CLEAR THE SCREEN
            menutype1.destroy()
            breakwok.destroy()
            breakveg.destroy()
            breakwest.destroy()
            breakmalay.destroy()
            breakindian.destroy()
            breakdrinks.destroy()
            clear.destroy()
        return

    def lunch(self,timeref):#DISPLAY STALLS OPEN FOR LUNCH
        menutype2=tk.Label(self,text="LUNCH DINNER STALLS",font=fuzzy)
        menutype2.pack()
        menutype2.place(x=300,y=80,anchor="center",width=200)
        
        lunchwok=ttk.Button(self,text="MINI WOK",command=lambda:printmenubreak("MINIWOK",timeref))#2/3
        lunchwok.pack()
        lunchwok.place(x=300,y=120,anchor="center",width=120)

        lunchveg=ttk.Button(self,text="VEGETERIAN",command=lambda:printmenubreak('VEGETERIAN',timeref))#6/7
        lunchveg.pack()
        lunchveg.place(x=300,y=160,anchor="center",width=120)

        lunchwest=ttk.Button(self,text="WESTERN",command=lambda:printmenubreak('WESTERN',timeref))#10/11
        lunchwest.pack()
        lunchwest.place(x=300,y=200,anchor="center",width=120)

        lunchmalay=ttk.Button(self,text="MALAY BBQ",command=lambda:printmenubreak('MALAY BBQ',timeref))#14/15
        lunchmalay.pack()
        lunchmalay.place(x=300,y=240,anchor="center",width=120)

        lunchindian=ttk.Button(self,text="INDIAN CUISINE",command=lambda:printmenubreak('INDIAN CUISINE',timeref))#18/19
        lunchindian.pack()
        lunchindian.place(x=300,y=280,anchor="center",width=120)

        lunchdrinks=ttk.Button(self,text="DRINKS",command=lambda:printmenubreak('DRINKS',timeref))#22/23
        lunchdrinks.pack()
        lunchdrinks.place(x=300,y=320,anchor="center",width=120)

        clear=ttk.Button(self,text="CLEAR",command=lambda:delete())#20/21
        clear.pack()
        clear.place(x=250,y=50,anchor="center",width=120)

        def delete():#CLEAR THE SCREEN
            menutype2.destroy()
            lunchwok.destroy()
            lunchveg.destroy()
            lunchwest.destroy()
            lunchmalay.destroy()
            lunchindian.destroy()
            lunchdrinks.destroy()
            clear.destroy()
        return   
                      


    def cal_func(self):#PREPARE THE TIME
        def calval():
            self.datepicked=cal.get_date()
            top.destroy()
            zonetime=self.datepicked.split('/')
            temp=zonetime[0]
            zonetime[0]=zonetime[1]
            zonetime[1]=temp                   
            timeranger=selectedtime.get()
            self.blasttime=zonetime[0]+" "+zonetime[1]+" "+str(int(zonetime[2])+2000)
            printtime=Label(self,text=(self.blasttime+" "+ str(timeranger)),font=normal)
            printtime.pack(pady=10,padx=10)
            printtime.place(x=380,y=50,anchor="center")
            future=datetime.strptime(self.blasttime, '%d %m %Y').weekday()
            currentday=calendar.day_name[future].upper()

            if timeranger in timeboom:#ASSIGN THE VALUE FOR TIME
                hourcheck=timeboom[timeranger]

            if currentday in weekday:#PRINT STALL INFORMATION
                if hourcheck>=0 and hourcheck<=6:
                    self.close()
                elif hourcheck>=7 and hourcheck<=11:
                    self.breakfast("BREAKFAST MENU")
                elif hourcheck>=11 and hourcheck<21:
                    self.lunch("LUNCH-DINNER MENU")
                else:
                    self.close()
            elif currentday in weekend:
                if hourcheck>=0 and hourcheck<=6:
                    self.close()
                elif hourcheck>=7 and hourcheck<=11:
                    self.breakfast("BREAKFAST MENU")
                elif hourcheck>=11 and hourcheck<15:
                    self.lunch("LUNCH-DINNER MENU")
                else:
                    self.close()
            else:
                self.close()            

        #CALENDAR OPTION                   
        top=Tk()
        cal=Calendar(top,selectmode="day",year=int(strftime('%y')),month=int(strftime('%m')),day=int(strftime('%d')))
        cal.pack(fill="both",expand=True)
        combostreak=["0000-0700","0700-0900","0900-1100","1100-1300","1300-1500","1500-1700","1700-1900","1900-2100","2100-2359"]
        selectedtime=StringVar(top)
        selectedtime.set(combostreak[0])        
        timemenu=OptionMenu(top,selectedtime,*combostreak)
        timemenu.pack()
        timemenu.config(width=10)      
        AMbutton=Button(top,text='Choose Date',command=lambda:calval())
        AMbutton.pack()            
        mainloop()
            
    

        
############################################################################################################
class promocode(tk.Frame):#PAGE TO CHECK PROMOCODE
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        night=Image.open("NSbackground.png")
        render1=ImageTk.PhotoImage(night)
        img=Label(self,image=render1)
        img.image=render1
        img.place(x=0,y=0)
        
        label=tk.Label(self,text="  Promocode Verification Menu  ",font=heading)
        label.pack()
        label.place(x=300,y=20,anchor="center")

        typepromo=tk.Label(self,text="Type your promotion code below",font=heading)
        typepromo.pack()
        typepromo.place(x=300,y=60,anchor="center")
        self.verify=StringVar()
        

        boxhead=tk.Entry(self,textvariable=self.verify)
        boxhead.pack()
        boxhead.place(x=300,y=100,anchor="center",height=30,width=200)

        boxheadbutton=tk.Button(self,text="CHECK",command=self.glance,font=normal)
        boxheadbutton.pack()
        boxheadbutton.place(x=300,y=140,anchor="center")

        bravobutton1=ttk.Button(self,text="Home",command=lambda:controller.show_frame(startpage))
        bravobutton1.pack()
        bravobutton1.place(x=300,y=380,anchor="center",width=120)
    def glance(self):#CHECK THE PROMOCODE AND DISPLAY IF CODE IS VALID
        sms=self.verify.get().upper()
        if sms in promotioncode:
            loadedmsg=promotioncode[sms]
        else:
            loadedmsg="Invalid Code!!!"

        
        reply=tk.Label(self,text=loadedmsg,font=normal)
        reply.pack()
        reply.place(x=300,y=250,anchor='center',height=150,width=150)
        
        
############################################################################################################

def popupmsg(msg):#DISPLAY OPERATION HOURS
    popup = tk.Tk()
    popup.title("OH")
    popup.resizable(False, False)
    popup.geometry("150x120")
    label1= ttk.Label(popup, text=msg, font=normal)
    label1.pack(side="top", fill="x", pady=10)
    label1.place(x=75,y=40,anchor="center")
    
    B1 = ttk.Button(popup, text="Close", command = popup.destroy)
    B1.pack()
    B1.place(x=75,y=90,anchor="center",width=60)
    popup.mainloop()


def printmenubreak(stallname,timeref,yq=0):# NEW SCREEN FOR MENU AND CHECK WAITING TIME
    import xlrd
    book=xlrd.open_workbook("northspinedata.xlsx")
    data=book.sheet_by_index(0)
    root=tk.Toplevel()
    root.wm_title(stallname)
    root.geometry('300x300')
    root.resizable(False, False)
    night=Image.open("NSbackground.png")
    render1=ImageTk.PhotoImage(night)
    img=Label(root,image=render1)
    img.image=render1
    img.place(x=150,y=150,anchor="center")

    if stallname in stallnamebreak:
        code=stallnamebreak[stallname]
    boxleft=[]
    boxright=[]
    if timeref==("LUNCH-DINNER MENU"):
        code=code+2
    for x in range(2,8):  #RETRIEVE FROM EXCEL SHEET                  
        for y in range (code,code+2):
            if y%2==0:
                boxleft.append(data.cell(x,y).value)
            else:
                if x==2:
                    boxright.append(str(data.cell(x,y).value))
                else:
                    boxright.append(str(data.cell(x,y).value)+"0")
                
    boxleft="\n\n".join(boxleft)
    boxright="\n\n$ ".join(boxright)

    stalltype=Label(root,text=stallname,font=normal)
    stalltype.pack()
    stalltype.place(x=150,y=20,anchor="center")

    menutype=Label(root,text=timeref,font=normal)
    menutype.pack()
    menutype.place(x=150,y=45,anchor="center")

    dishes=Label(root,text=boxleft,font=normal)
    dishes.pack()
    dishes.place(x=125,y=150,anchor="center")

    pricing=Label(root,text=boxright,font=normal)
    pricing.pack()
    pricing.place(x=240,y=150,anchor="center")

    queue=StringVar()
    menuclear = Button(root, text="Close", command = root.destroy)
    menuclear.pack()
    menuclear.place(x=260,y=20,anchor="center",width=60)

    if yq==1:
        waiting=Label(root,text="PAX IN QUEUE:",font=normal)
        waiting.pack()
        waiting.place(x=50,y=270,anchor="center")
        queue=StringVar()

        paxno=Entry(root,textvariable=queue)
        paxno.pack()
        paxno.place(x=125,y=270,width=35,anchor="center")


        def estimate():#WAITING TIME
            try:
                msg=queue.get()
                finalqueue=int(msg)
            except:
                feedback="INVALID\nENTRY"
                reply=tk.Label(root,text=feedback,font=normal)
                reply.pack()
                reply.place(x=250,y=270,anchor="center",height=40,width=80)
            else:
                if finalqueue >=0 and finalqueue <=100:
                    inst=finalqueue*0.5
                    feedback=(str(inst)+ " Minutes\nWaiting Time")
                    reply=tk.Label(root,text=feedback,font=normal)
                    reply.pack()
                    reply.place(x=250,y=270,anchor="center",height=40,width=80)
                else:
                    feedback="INVALID\nENTRY"
                    reply=tk.Label(root,text=feedback,font=normal)
                    reply.pack()
                    reply.place(x=250,y=270,anchor="center",height=40,width=80)
               
        timecal=tk.Button(root,text="CHECK",command=lambda:estimate(),font=normal)
        timecal.pack()
        timecal.place(x=180,y=270,anchor="center")           

        root.mainloop()

    
        
############################################################################################################    
hours="MON-FRI: 7AM - 9PM\nSAT       : 7AM - 3PM\nSUN & PH  : CLOSED"       

promotioncode={"SAVE5":"$5 discount code is valid\n Redeem at any stall",
               "DINOROCKS":"Free Milo Dinosaur\n Redeem at Drinks Stall",
               "NUGGET":"Free Nuggets\n Redeem at Western Stall"}

weekday=("MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY")
weekend=("SATURDAY")
weekend2=("SUNDAY")

stallnamebreak={'MINIWOK':0,'VEGETERIAN':4,'WESTERN':8,'MALAY BBQ':12,'INDIAN CUISINE':16,'DRINKS':20}
stallnamelunch={'MINIWOK':2,'VEGETERIAN':6,'WESTERN':10,'MALAY BBQ':14,'INDIAN CUISINE':18,'DRINKS':22}

heading=("Helvetica",16)
normal=("Helvetica",10)
timefont=("Helvetica",14)
fuzzy=("calibri",16)

closeprint=("Sorry we are closed\n Please check the operating hours\n Hope to see you soon")

timeboom={"0000-0700":2,"0700-0900":8,"0900-1100":8,"1100-1300":13,"1300-1500":13,"1500-1700":13,"1700-1900":13,
          "1900-2100":13,"2100-2359":2}


app=northspineapp()
app.mainloop()
