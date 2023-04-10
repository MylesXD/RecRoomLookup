import requests
import tkinter as tk
import customtkinter as ctk


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry('800x530')
root.title('Rec Room Lookup')

accId=ctk.StringVar()
accId.set('Account ID: ')
user=ctk.StringVar()
user.set('Username: ')
disp=ctk.StringVar()
disp.set('Display Name: ')
emoj=ctk.StringVar()
emoj.set('Emoji: ')
profimg=ctk.StringVar()
profimg.set('Profile Image: ')
banrimg=ctk.StringVar()
banrimg.set('Banner Image: ')
junr=ctk.StringVar()
junr.set('Junior: ')
plat=ctk.StringVar()
plat.set('Platforms: ')
flag=ctk.StringVar()
flag.set('Flags: ')
create=ctk.StringVar()
create.set('createdAt: ')

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text='Rec Room Lookup', font=('Roboto', 24))
label.pack(pady=12, padx=10)

ent1=ctk.CTkEntry(master=frame, placeholder_text="Username")
ent1.pack(pady=12, padx=10)

def request():
    r=requests.get('https://accounts.rec.net/account?username=' + ent1.get())
    if r.ok==True:
        print(r.json())
        r_dict=r.json()
        accId.set('accountId: '+str(r_dict['accountId']))
        user.set('Username: '+r_dict['username'])
        disp.set('Display Name: '+r_dict['displayName'])
        emoj.set('Emoji: '+r_dict['displayEmoji'])
        profimg.set('Profile Image: http://img.rec.net/'+r_dict['profileImage'])
        banrimg.set('Profile Image: http://img.rec.net/' + r_dict['bannerImage'])
        junr.set('Junior: ' + str(r_dict['isJunior']))
        plat.set('Platforms: ' + str(r_dict['platforms']))
        flag.set('Pride Flags: ' + str(r_dict['identityFlags']))
        create.set('Platforms: ' + str(r_dict['createdAt']))

button=ctk.CTkButton(master=frame, text='Lookup', command=request)
button.pack(pady=12, padx=10)

accIdlabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=accId)
accIdlabel.pack()
userlabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=user)
userlabel.pack()
displabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=disp)
displabel.pack()
emojlabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=emoj)
emojlabel.pack()
profimglabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=profimg)
profimglabel.pack()
banrimglabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=banrimg)
banrimglabel.pack()
junrlabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=junr)
junrlabel.pack()
platlabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=plat)
platlabel.pack()
flaglabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=flag)
flaglabel.pack()
createlabel = ctk.CTkLabel(master=frame, font=('Roboto', 16), textvariable=create)
createlabel.pack()

credit=ctk.CTkLabel(master=frame, text='myles#7118', font=('Roboto', 14), text_color=('grey'))
credit.place(relx=0.98,rely=0.97,anchor='e')


root.mainloop()