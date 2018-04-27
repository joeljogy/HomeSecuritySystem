# -*- coding: UTF-8 -*-
import cv2
import os
import numpy as np
import PIL.Image
import pymysql
from Tkinter import *
from PIL import Image, ImageTk
import nexmo
import paramiko
import pygame


detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.createLBPHFaceRecognizer()

master = Tk() #  (main) window
master.title("Home Security System")  #Title the form
master.configure(background = '#494949')
logo = PhotoImage(file="home.gif")

#Label(master,text=None,image=logo).grid(row=0,columnspan=2,sticky=W,padx=80)
Label(master, text="Home Security System",fg='#FFFFFF',font=("Segoe UI Light", 45),bg='#494949').grid(row=0,columnspan=2,sticky=E,padx=40)






def dashboard():
    dashboard_window=Tk()
    dashboard_window.title("Dashboard")
    dashboard_window.configure(background = '#656565')
    Label(dashboard_window, text="Registered Users Database",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#656565').grid(row=0,columnspan=4,sticky=W,padx=10,pady=20)
    Label(dashboard_window, text="ID",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=1,column=0,sticky=W,padx=5,pady=0)
    Label(dashboard_window, text="Name",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=1,column=1,sticky=W,padx=0,pady=0)
    Label(dashboard_window, text="Email ID",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=1,column=2,sticky=W,padx=0,pady=0)
    Label(dashboard_window, text="Phone No",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=1,column=3,sticky=W,padx=0,pady=0)
    connection = pymysql.connect(host = 'localhost', user = 'admin', password = 'admin', db = 'home_security_system')
    
    try:
        with connection.cursor() as cursor:
            
            F_Idquery = "SELECT Id FROM `registered_users` WHERE `Name` LIKE 'Administrator'" #Gives the total number of registered users in the database
            cursor.execute(F_Idquery)
            rows = cursor.fetchone() #try with fetchone()
            No_of_IDs = rows[0]
            if No_of_IDs == 0:
                i=0
            F_Idquery = "SELECT * FROM `registered_users` WHERE `Name` NOT LIKE 'Administrator' ORDER BY Id ASC" #Gives the total number of registered users in the database
            cursor.execute(F_Idquery)
            
            for i in range(No_of_IDs):
                row = cursor.fetchone()
                Label(dashboard_window, text=row[0],fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=i+2,column=0,sticky=W,padx=5,pady=0)
                Label(dashboard_window, text=row[1],fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=i+2,column=1,sticky=W,padx=0,pady=0)
                Label(dashboard_window, text=row[2],fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=i+2,column=2,sticky=W,padx=0,pady=0)
                Label(dashboard_window, text=row[3],fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=i+2,column=3,sticky=W,padx=0,pady=0)
                

        
    finally:
        connection.close()


    def delete_user():
        delete_window=Tk()
        delete_window.title("Delete User")
        delete_window.configure(background = '#656565')
        Label(delete_window, text ="Delete User",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#656565').grid(row=1,sticky=W,padx=20,pady=20)
        Label(delete_window, text="Enter Name",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=5,sticky=W,pady=10,padx=12)
        f10=Entry(delete_window,width=30)
        f10.grid(row=5, column=1,sticky=E,padx=10)

        def delete_action():
            F_delete_name=f10.get()
            f10.delete(0,END)
            connection = pymysql.connect(host = 'localhost', user = 'admin', password = 'admin', db = 'home_security_system')
            try:
                with connection.cursor() as cursor:
                    
                    F_Idquery = "DELETE FROM `registered_users` WHERE `Name` LIKE '%s'" %(F_delete_name) #Gives the total number of registered users in the database
                    cursor.execute(F_Idquery)
                    
                    F_Idquery = "SELECT Id FROM `registered_users` WHERE `Name` LIKE 'Administrator'" #Gives the total number of registered users in the database
                    cursor.execute(F_Idquery)
                    rows = cursor.fetchone() #try with fetchone()
                    F_Id = rows[0] - 1
                    if (F_Id > 0) or (F_Id == 0):
                        update_id = "UPDATE `registered_users` SET Id = %s WHERE Name = 'Administrator'" %(F_Id) #Updates the total number of registered users in the database
                        cursor.execute(update_id)
                    dashboard_window.destroy()
            finally:
                connection.close()

            
        def quit4():
            delete_window.destroy()
            
        Button(delete_window, text='Delete',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=delete_action,height = 1, width = 15).grid(row=9,column=0,sticky=W,pady=30,padx=10)
        Button(delete_window, text='Cancel',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=quit4,height = 1, width = 15).grid(row=9,column=1,sticky=W,pady=30,padx=10)
        mainloop()




    Button(dashboard_window, text='Delete User',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command = delete_user ,height = 1, width = 15).grid(row=i+3,column=0,sticky=W,pady=30,padx=10)












def about():
    about_window=Tk()
    about_window.title("About")
    about_window.configure(background = '#656565')
    Label(about_window, text="About",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#656565').grid(row=0,sticky=W,padx=20,pady=20)
    Label(about_window, text="Home Security System (with Raspberry Pi)",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=1,sticky=W,padx=20,pady=0)
    Label(about_window, text="Version 10.1604.21020.0",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=2,sticky=W,padx=20,pady=0)
    Label(about_window, text="Developed by Joel J, Sameer P, Sachin V.",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=3,sticky=W,padx=20,pady=0)
    Label(about_window, text="© Copyright 2017 MIT,Manipal",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=4,sticky=W,padx=20,pady=0)
    Label(about_window, text="All rights reserved.",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=5,sticky=W,padx=20,pady=0)
    Label(about_window, text=" ",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=6,sticky=W,padx=20,pady=0)













def activate():
    
    def quit2():
        activate_window.destroy()
        
    activate_window=Tk()
    activate_window.title("Activate")
    activate_window.configure(background = '#656565')
    Label(activate_window, text ="Access Login",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#656565').grid(row=1,sticky=W,padx=20,pady=20)
    Label(activate_window, text="Enter Password",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=5,sticky=W,pady=10,padx=12)
    f=Entry(activate_window,width=30)
    F_passkey=f.get()
    f.grid(row=5, column=1,sticky=E,padx=10)

    def face_recognition():
        count_sms=0
        
        if f.get()=="admin":
            activate_window.destroy()
            
            recognizer = cv2.createLBPHFaceRecognizer()
            recognizer.load('Trainer.yml')
            cascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascadePath);

            connection = pymysql.connect(host = 'localhost', user = 'admin', password = 'admin', db = 'home_security_system')
            flagbit=1
            cam = cv2.VideoCapture(0)
            font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_TRIPLEX, 1, 1, 0, 1, 1)
            while flagbit==1:
                ret,img =cam.read()
                img = cv2.flip(img, 1)
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=faceCascade.detectMultiScale(gray, 1.5,5)
                unknown_count=0
                for(x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
                    Id2, conf = recognizer.predict(gray[y:y+h,x:x+w])
                    
                    if(conf<45):
                        with connection.cursor() as cursor:
                            
                            F_Idquery = "SELECT Name FROM `registered_users` WHERE (`Id` = %s and 'Name' NOT LIKE 'Administrator')" %(Id2)#Gives the total number of registered users in the database
                            cursor.execute(F_Idquery)
                            rows = cursor.fetchone() #try with fetchone()
                            Id = rows[0]             
                    else:
                        Id="Unknown"                        
                        
                        if count_sms==0:
                        #Send SMS
                            client = nexmo.Client(key='879fdda7', secret='7ed24cc85d4a8f92')
                            client.send_message({'from': 'Nexmo', 'to': '919071063113', 'text': 'INTRUDER ALERT!! House is insecure!'})
                            count_sms=count_sms+1
                            

##                        ssh = paramiko.SSHClient()
##                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##                        target_host = '192.168.137.39'
##                        target_port = 22
##                        target_port = 22
##                        pwd = 'raspberry'
##                        un = 'pi'
##                        ssh.connect( hostname = target_host, port = target_port, username = un, password = pwd )
##                        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sudo python test.py")
##                        ssh.close()

                    cv2.cv.PutText(cv2.cv.fromarray(img),str(Id), (x,y+h),font, 255)
                cv2.imshow('img',img) 
                if cv2.waitKey(1)==27:
                    deactivate_window=Tk()
                    deactivate_window.title("Activate")
                    deactivate_window.configure(background = '#656565')

                    Label(deactivate_window, text ="Access Login",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#656565').grid(row=1,sticky=W,padx=20,pady=20)
                    Label(deactivate_window, text="Enter Password",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=5,sticky=W,pady=10,padx=12)
                    f7=Entry(deactivate_window,width=30)
                    f7.grid(row=5, column=1,sticky=E,padx=10)
                    F_passkey=f7.get()
                    
                    def deactivate():
                        deactivate_window.destroy()
                        flagbit=0
                        cam.release()
                        cv2.destroyAllWindows()
                    def quit3():
                        deactivate_window.destroy()
                        
                    Button(deactivate_window, text='Ok',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=deactivate,height = 1, width = 15).grid(row=9,column=0,sticky=W,pady=30,padx=10)
                    Button(deactivate_window, text='Cancel',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=quit3,height = 1, width = 15).grid(row=9,column=1,sticky=W,pady=30,padx=10)
                    mainloop()

            
        #Entered password is incorrect
        else:
            f.delete(0,END)

    #Creating buttons for Ok and Cancel
    Button(activate_window, text='Ok',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=face_recognition ,height = 1, width = 15).grid(row=9,column=0,sticky=W,pady=30,padx=10)
    Button(activate_window, text='Cancel',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=quit2,height = 1, width = 15).grid(row=9,column=1,sticky=W,pady=30,padx=10)

    










            
        
def setup():
    
    def quit():
        master1.destroy()

    def authentication():
        def quit3():
            authentication_window.destroy()
            
        authentication_window=Tk()
        authentication_window.title("Activate")
        authentication_window.configure(background = '#656565')
        Label(authentication_window, text ="Access Login",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#656565').grid(row=1,sticky=W,padx=20,pady=20)
        Label(authentication_window, text="Enter Password",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=5,sticky=W,pady=10,padx=12)
        f9=Entry(authentication_window,width=30)
        f9.grid(row=5, column=1,sticky=E,padx=10)
        F_password=f9.get()

        
        def create_dataset():
            if f9.get()=="admin":
                authentication_window.destroy()

            
                connection = pymysql.connect(host = 'localhost', user = 'admin', password = 'admin', db = 'home_security_system')
                try:
                    with connection.cursor() as cursor:
                        F_name = f1.get()
                        F_email1 = f2.get()
                        F_email2 = f3.get()
                        F_contactno = f4.get()
                        F_passkey1 = f5.get()
                        F_passkey2 = f6.get()
                        
                        f1.delete(0,END)
                        f2.delete(0,END)
                        f3.delete(0,END)
                        f4.delete(0,END)
                        f5.delete(0,END)
                        f6.delete(0,END)
                        
                        F_Idquery = "SELECT Id FROM `registered_users` WHERE `Name` LIKE 'Administrator'" #Gives the total number of registered users in the database
                        cursor.execute(F_Idquery)
                        rows = cursor.fetchone() #try with fetchone()
                        F_Id = rows[0] + 1
                        sql = "INSERT INTO `registered_users` VALUES (%s, %s, %s, %s, %s)" 
                        cursor.execute(sql, (F_Id,F_name,F_email1,F_contactno,F_passkey1))
                        update_id = "UPDATE `registered_users` SET Id = %s WHERE Name = 'Administrator'" %(F_Id) #Updates the total number of registered users in the database
                        cursor.execute(update_id)
                        connection.commit()


                    
                finally:
                    connection.close()

                cam = cv2.VideoCapture(0)
                count=0
                    
                while(True):             
                    ret, img = cam.read()
                    img = cv2.flip(img, 1)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                            
                        # incrementing count of snaps taken 
                        count+=1
                            
                        # save the captured face in the dataset folder
                        cv2.imwrite("Registered_dataSet/User."+ str(F_Id) +'.'+ str(count) + ".jpg", gray[y:y+h,x:x+w])

                        cv2.imshow('frame',img)
                            
                    # wait for escape button to be pressed and close screen
                    if cv2.waitKey(1)==27:
                        break
                        
                    # break if count becomes greater than 20
                    elif count>30:
                        break
                        
                cam.release()
                cv2.destroyAllWindows()

                from PIL import Image
                # get the path of all the files in the folder
                imagePaths=[os.path.join('Registered_dataset',f) for f in os.listdir('Registered_dataset')]

                        
                # create empty face list
                faceSamples=[]
                        
                # create empty ID list
                Ids=[]
                        
                #now looping through all the image paths and loading the Ids and the images
                for imagePath in imagePaths:
                    # load the image and convert it to gray scale
                    pilImage=Image.open(imagePath).convert('L')
                            
                    # convert the PIL image into numpy array
                    imageNp=np.array(pilImage,'uint8')
                            
                    # get the Id from the image filename         
                    Id=int((os.path.split(imagePath)[-1].split(".")[1]))
                    print Id                                     
                    # extract the face from the training image sample
                    faces=detector.detectMultiScale(imageNp)
                    #If a face is there then append that in the list as well as Id of it
                    for (x,y,w,h) in faces:
                        faceSamples.append(imageNp[y:y+h,x:x+w])
                        Ids.append(Id)
                recognizer.train(faceSamples, np.array(Ids))
                recognizer.save('Trainer.yml')

            else:
                f9.delete(0,END)





        #Creating buttons for Ok and Cancel
        Button(authentication_window, text='Ok',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=create_dataset ,height = 1, width = 15).grid(row=9,column=0,sticky=W,pady=30,padx=10)
        Button(authentication_window, text='Cancel',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=quit3,height = 1, width = 15).grid(row=9,column=1,sticky=W,pady=30,padx=10)

                    
            


    
    #Create the Registration window
    master1 = Tk() #  (main) window
    master1.title("Setup")  #Title the form
    master1.configure(background = '#656565')
    Label(master1, text="Register Users",fg='#FFFFFF',font=("Segoe UI Light", 30),bg='#656565').grid(row=0,columnspan=1,sticky=W,padx=10,pady=10)
    Label(master1, text="* indicates mandatory fields",fg='#FFFFFF',font=("Segoe UI Light", 12),bg='#656565').grid(row=1,columnspan=1,sticky=W,padx=10,pady=10)


    #Label box in each row
    var = IntVar()
    Radiobutton(master1, text="Administrator",fg='#000000', variable=var,font=("Segoe UI Light", 15),bg='#494949', value=1).grid(sticky=W,row=2,columnspan=1,pady=10,padx=50)
    Radiobutton(master1, text="Verified User",fg='#000000', variable=var,font=("Segoe UI Light", 15),bg='#494949', value=2).grid(sticky=E,row=2,columnspan=2,pady=10,padx=50)
    Label(master1, text="Name*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=3,sticky=W,pady=10)
    Label(master1, text="Email",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=4,sticky=W,pady=10)
    Label(master1, text="Confirm Email",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=5,sticky=W,pady=10)
    Label(master1, text="Contact No:*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=6,sticky=W,pady=10)
    Label(master1, text="Passkey*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=7,sticky=W,pady=10)
    Label(master1, text="Confirm Passkey*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=8,sticky=W,pady=10)

    
    #Text entry/box for each label
    f1=Entry(master1,width=30)
    f2=Entry(master1,width=30)
    f3=Entry(master1,width=30)
    f4=Entry(master1,width=30)
    f5=Entry(master1,width=30)
    f6=Entry(master1,width=30)
    
    #Text box in each row
    f1.grid(row=3, column=1,sticky=E,padx=10)
    f2.grid(row=4, column=1,sticky=E,padx=10)
    f3.grid(row=5, column=1,sticky=E,padx=10)
    f4.grid(row=6, column=1,sticky=E,padx=10)
    f5.grid(row=7, column=1,sticky=E,padx=10)
    f6.grid(row=8, column=1,sticky=E,padx=10)


    Button(master1, text='Add User',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=authentication,height = 1, width = 15).grid(row=9,column=0,sticky=W,pady=30,padx=10)
    Button(master1, text='Cancel',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#581845', command=quit,height = 1, width = 15).grid(row=9,column=1,sticky=W,pady=30,padx=10)


image_dashboard = PIL.Image.open("Dashboard.png")
photo_dashboard = ImageTk.PhotoImage(image_dashboard)


image_status = PIL.Image.open("Status.png")
photo_status = ImageTk.PhotoImage(image_status)

image_settings = PIL.Image.open("Settings.png")
photo_settings = ImageTk.PhotoImage(image_settings)

image_about = PIL.Image.open("About.png")
photo_about = ImageTk.PhotoImage(image_about)

    
B1 = Button(master, text='Dashboard',fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#494949', command=dashboard,height = 150, width = 150,image=photo_dashboard,compound="top",borderwidth=0)
B1.grid(row=1,columnspan=1,sticky=W,padx=111,pady=30)
B2 = Button(master, text='Setup',fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#494949', command=setup,height = 150, width = 150,image=photo_settings,compound="top",borderwidth=0)
B2.grid(row=1,columnspan=1,sticky=E,padx=0,pady=10)
B3 = Button(master, text='Activate',fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#494949',command=activate,height = 150, width = 150,image=photo_status,compound="top",borderwidth=0)
B3.grid(row=2,columnspan=1,sticky=W,padx=111,pady=10)
B4 = Button(master, text='About',fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#494949', command=about,height = 150, width = 150,image=photo_about,compound="top",borderwidth=0)
B4.grid(row=2,columnspan=1,sticky=E,padx=0,pady=10)
mainloop()
