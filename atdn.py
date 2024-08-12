import os
import smtplib
import ssl
from email.message import EmailMessage
import cv2
import qrcode
from tkinter import *
from tkinter import messagebox
import pyttsx3
import random
greet=['Hello','Hai','Hey']
fn=['Nice','Fantastic','Marvelous','Wonderful']
present=[]
def main():
    def edit():
        def ress(e):
            en1.destroy()
            bn1.destroy()
            la1.destroy()
            return main()
        root.bind('<Tab>',ress)
        try:
            scanqr.destroy()
            makeqr.destroy()
            remname.destroy()
            dele.destroy()
            inf.destroy()
            ti.destroy()
        except:
            ...
        def ft():
            fi=open('clnm.txt','w+')
            con=en1.get()
            if '@gmail.com' in con:
                fi.write(con)
            else:
                messagebox.showwarning('Warning','Enter valid Email address')
                la1.destroy()
                en1.destroy()
                bn1.destroy()
                return edit()
            fi.close()
            la1.destroy()
            en1.destroy()
            bn1.destroy()
            return main()
        ms=open('clnm.txt','r+')
        data=ms.read()
        ms.close()
        if data!='':
            cont=data
        else:
            cont='Enter class incharge Email'
        root.geometry("500x300")
        la1=Label(root,image=im8,bd=0,bg='white')
        la1.place(x=60,y=62)
        en1=Entry(root,width=30,bd=0,bg='white',fg='grey',font=('',18))
        en1.place(x=150,y=70)
        en1.insert(0,cont)
        bn1=Button(root,image=im10,bd=0,bg='white',activebackground='white',command=ft)
        bn1.place(x=170,y=200)
    def clsm():
        body='\nPresent\n~~~~~~~'
        for i in present:
            body+='\n'+i
        else:
            body+="\n\nAbsentees\n~~~~~~~~~"
        nams=open('names.txt','r')
        tns=nams.read().split()
        nams.close()
        for i in tns:
            if i not in present:
                body+='\n'+i
        try:
            tto=open('clnm.txt','r')
            rec=tto.read()
            tto.close()
        except:
            messagebox.showerror('Error','file clnm.txt not found !')
            rec='botid127@gmail.com'
        em=EmailMessage()
        em['From']=sender
        em['To']=rec
        em['Subject']='Today attendence '
        em.set_content(body)
        context=ssl.create_default_context()
        try:
            ser=smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)
        except:
            messagebox.showwarning('Error','Not connected to internet try again !')
            scanqr.destroy()
            makeqr.destroy()
            remname.destroy()
            dele.destroy()
            inf.destroy()
            ti.destroy()
            return main()
        ser.login(sender,password)
        ser.sendmail(sender,rec,em.as_string())
        ser.quit()
        messagebox.showinfo("Info",'Mail successfully sent to Class incharge')
    def deles():
        def cmd():
            def chkd():
                e1.destroy()
                b1.destroy()
                b2.destroy()
                return deles()
            try:
                na=open("names.txt",'r')
                namelist=na.read().split()
                na.close()
            except:
                messagebox.showerror('Error','File names.txt not found ! ')
                return chkd()
            nms=e1.get()
            nm=nms.replace(' ','')
            try:
                namelist.remove(nm.lower())
            except:
                messagebox.showwarning('Warning','Name not found ')
                return chkd()
            na1=open('names.txt','a+')
            for i in namelist:
                na1.write(' '+i)
            na1.close()
            messagebox.showinfo("Info",'Name '+nm+' removed')
            return chkd()
        def tom(e):
            e1.delete(0,"end")
            e1['fg']='black'
        root.geometry("400x300")
        scanqr.destroy()
        makeqr.destroy()
        remname.destroy()
        dele.destroy()
        inf.destroy()
        ti.destroy()
        def re(e):
            b1.destroy()
            e1.destroy()
            b2.destroy()
            return main()
        def ree():
            b1.destroy()
            e1.destroy()
            b2.destroy()
            return main()
        root.bind("<Tab>",re)
        e1=Entry(root,bd=0,width=30,font=('',15),bg='white',fg='grey')
        e1.place(x=50,y=70)
        e1.insert(0,'Enter name to remove')
        e1.bind("<FocusIn>",tom)
        b1=Button(root,image=imd,bd=0,font=('',30),bg='white',activebackground='white',command=cmd)
        b1.place(x=300,y=57)
        b2=Button(root,image=im6,bd=0,bg='white',activebackground='white',command=ree)
        b2.place(x=150,y=200)
    def scanqrr():
        cap=cv2.VideoCapture(0)
        a=open('names.txt','r')
        aa=a.read().split()
        a.close()
        leng=len(aa)
        while True:
            ret,frame=cap.read()
            d=cv2.QRCodeDetector()
            cv2.imshow('Scaning QR code',frame)
            ke=cv2.waitKey(1)
            if ke==ord('q') or leng==len(present):
                cap.release()
                cv2.destroyAllWindows()
                return clsm()
            try:
                s=d.detectAndDecode(frame)
            except:
                try:
                    scanqr.destroy()
                    makeqr.destroy()
                    remname.destroy()
                    dele.destroy()
                    inf.destroy()
                    ti.destroy()
                except:
                    ...
                return main()
            if s[0]:
                if s[0] not in present:
                    if s[0] in aa:
                        present.append(s[0])
                        en=pyttsx3.init()
                        voice=en.getProperty('voices')
                        en.setProperty('voice',voice[2].id)
                        en.setProperty("rate",170)
                        en.say(random.choice(greet)+s[0]+',Welcome to C.K.C.E.T. ,Have a ,'+random.choice(fn)+'Day.')
                        en.runAndWait()
                    else:
                        en=pyttsx3.init()
                        voice=en.getProperty('voices')
                        en.setProperty('voice',voice[2].id)
                        en.setProperty("rate",170)
                        en.say('Please Register before scaning')
                        en.runAndWait()
                elif s[0] in present:
                    en=pyttsx3.init()
                    voice=en.getProperty('voices')
                    en.setProperty('voice',voice[2].id)
                    en.setProperty("rate",170)
                    en.say('Already verified ')
                    en.runAndWait()
    def mail(receiverr):
        em=EmailMessage()
        em['From']=sender
        em['To']=receiverr
        em['Subject']='QR code '
        r=open('ckcetqr.jpg','rb')
        im=r.read()
        em.add_attachment(im,maintype='image',subtype='jpg',filename=r.name)
        context=ssl.create_default_context()
        try:
            ser=smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)
        except:
            messagebox.showwarning('Error','Not connected to internet Please try again !')
            return makeqrcode()
        ser.login(sender,password)
        ser.sendmail(sender,receiverr,em.as_string())
        r.close()
        ser.quit()
        os.system("del ckcetqr.jpg")
        messagebox.showinfo("Info",'Mail successfully sent check your Inbox')
        return makeqrcode()
    def makeqrcode():
        def bev(e):
            l1.destroy()
            l2.destroy()
            na.destroy()
            em.destroy()
            mas.destroy()
            bc.destroy()
            return main()
        def tem(e):
            na.delete(0,"end")
        def temg(e):
            em.delete(0,"end")
        def sen():
            nam=na.get()
            if nam=='Enter your name' or len(nam)<=2:
                messagebox.showinfo('Warning','please enter valid name')
                l1.destroy()
                l2.destroy()
                na.destroy()
                em.destroy()
                mas.destroy()
                bc.destroy()
                return makeqrcode()
            nams=nam.lower()
            name=nams.replace(' ','')
            mailid=em.get()
            if '@gmail.com' not in mailid:
                messagebox.showwarning('Warning','Please enter valid Email')
                na.destroy()
                em.destroy()
                mas.destroy()
                bc.destroy()
                l1.destroy()
                l2.destroy()
                return makeqrcode()
            nms=open('names.txt','r')
            tn=nms.read().split()
            nms.close()
            if name not in tn:
                nms=open('names.txt','a+')
                nms.write(' '+name)
                nms.close()
            else:
                messagebox.showwarning("Warning","Already registered !")
                na.destroy()
                em.destroy()
                mas.destroy()
                bc.destroy()
                l1.destroy()
                l2.destroy()
                return makeqrcode()
            qr=qrcode.make(name)
            qr.save("ckcetqr.jpg")
            na.destroy()
            em.destroy()
            mas.destroy()
            l1.destroy()
            l2.destroy()
            bc.destroy()
            return mail(mailid)
        root.bind("<Tab>",bev)
        try:
            scanqr.destroy()
            makeqr.destroy()
            remname.destroy()
            dele.destroy()
            inf.destroy()
            ti.destroy()
        except:
            ...
        def era():
            na.destroy()
            em.destroy()
            mas.destroy()
            bc.destroy()
            l1.destroy()
            l2.destroy()
            return main()
        root.geometry("500x400")
        na=Entry(root,font=('',20),width=30,bd=0,bg='white',fg='grey')
        na.insert(0,'Enter your name')
        na.place(x=160,y=70)
        na.bind("<FocusIn>",tem)
        em=Entry(root,font=('',20),width=30,bd=0,bg='white',fg='grey')
        em.insert(0,'Enter your Email')
        em.place(x=160,y=150)
        em.bind("<FocusIn>",temg)
        mas=Button(root,image=im7,bd=0,bg='white',activebackground='white',command=sen)
        mas.place(x=260,y=240)
        bc=Button(root,image=im6,activebackground='white',bd=0,bg='white',command=era)
        bc.place(x=150,y=250)
        l1=Label(root,image=im9,bd=0,bg='white',activebackground='white')
        l1.place(x=83,y=60)
        l2=Label(root,image=im8,bd=0,bg='white',activebackground='white')
        l2.place(x=80,y=145)
    def about():
        scanqr.destroy()
        makeqr.destroy()
        remname.destroy()
        dele.destroy()
        inf.destroy()
        ti.destroy()
        def evn(e):
            a.destroy()
            b.destroy()
            return main()
        def rett():
            a.destroy()
            b.destroy()
            return main()
        root.bind('<Tab>',evn)
        try:
            ab=open('abt.txt','r')
            da=ab.read()
            ab.close()
        except:
            da='hello'
        a=Label(root,text=da,font=('',12),bd=0,bg='white',fg='grey')
        a.place(x=0,y=50)
        b=Button(root,image=im6,bd=0,bg='white',activebackground='white',command=rett)
        b.place(x=200,y=500)
    sender='ckcetcuddalore@gmail.com'
    password='mnft wqln brib quqf'
    root.geometry("500x650")
    root.configure(background='white')
    root.title("")
    im1=PhotoImage(file='signup.png')
    im2=PhotoImage(file='qscan.png')
    im3=PhotoImage(file='edit.png')
    im4=PhotoImage(file='delete.png')
    imd=PhotoImage(file='dustbin.png')
    im5=PhotoImage(file='information.png')
    im6=PhotoImage(file='back.png')
    im7=PhotoImage(file='message.png')
    im8=PhotoImage(file='gmail.png')
    im9=PhotoImage(file='id.png')
    im10=PhotoImage(file='save.png')
    im11=PhotoImage(file='top.png')
    makeqr=Button(root,image=im1,bd=0,activebackground='white',bg='white',command=makeqrcode)
    makeqr.place(x=100,y=170)
    scanqr=Button(root,image=im2,bg='white',activebackground='white',bd=0,command=scanqrr)
    scanqr.place(x=265,y=170)
    remname=Button(root,image=im3,bg='white',activebackground='white',bd=0,command=edit)
    remname.place(x=100,y=350)
    dele=Button(root,image=im4,activebackground='white',bd=0,bg='white',command=deles)
    dele.place(x=265,y=340)
    inf=Button(root,image=im5,bd=0,activebackground='white',bg='white',command=about)
    inf.place(x=180,y=550)
    ti=Label(root,image=im11,bd=0,bg='white')
    ti.place(x=-15,y=-5)
    root.mainloop()
root=Tk()
main()