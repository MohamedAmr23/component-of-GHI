from tkinter import *
from tkinter import messagebox 
root=Tk()
root.title("Login")
# #function to set login in the center of any screen
# def center(w,h):
#     screenwidth=root.winfo_screenwidth()
#     screenheight=root.winfo_screenheight()
#     x=int((screenwidth-w)/2)
#     y=int((screenheight-h)/2)
#     root.geometry(f"{w}x{h}+{x}+{y}")

# center(500,300) 
# root.resizable(False,False)
# padx=10
# pady=10
# font=('Tahoma',12)
# frame=Frame(root)
# #check if the name is it or not
# def change():
#     name=enname.get()
#     password=enpass.get()
#     validname='ahmed'
#     validpass='47200333'
#     if name==validname and password==validpass:
#         messagebox.showinfo('Info','valid email')
#     else:
#         messagebox.showerror("Info",'invalid email')    


# #create label name        
# lblname=Label(frame,text="name",font=font)
# enname=Entry(frame,font=font)

# # create label password
# lblpass=Label(frame,text='password',font=font)
# enpass=Entry(frame, show='*',font=font)
# #button login
# bu=Button(frame,text="login",command=change,background='red',fg='white',font=font)

# #control label
# lblname.grid(row=0,column=0,padx=padx,pady=pady)
# enname.grid(row=0,column=1,padx=padx,pady=pady)

# #control password
# lblpass.grid(row=1,column=0,padx=padx,pady=pady)
# enpass.grid(row=1,column=1,padx=padx,pady=pady)

# #control botton
# bu.grid(row=2,column=0,columnspan=2,padx=padx,pady=pady)

# #container to put all elements in it
# frame.place(anchor='center',relx=.5,rely=.5)
# root.mainloop()
#############################################################################
#create radio button

#function to command button
# def choice():
#    choice= myvar.get()
#    messagebox.showinfo('yout option',choice)

# #variable to take value from radio   
# myvar=StringVar()

# #set default value when programe run
# myvar.set('Female')

# #create radiobutton
# rad1=Radiobutton(root,text='Male',value='Male',variable=myvar)
# rad2=Radiobutton(root,text='Female',value='Female',variable=myvar)

# #create button
# btn=Button(root,text='login',command=choice)

# #show elements
# rad1.pack()
# rad2.pack()
# btn.pack()
# root.mainloop()
##################################################################################
#create checkbutton

#create function to button to select in checkbox
# def chebox():
#  lis=[] #create empty list
#  if bcheck1.get()==True: #if user select this value
#   lis.append(check1['text']) #append val
#  if bcheck2.get()==True:
#   lis.append(check2['text'])
#  if bcheck3.get()==True:
#   lis.append(check3['text'])  
#  s='  ,  '.join(lis) #separate with comma (,)
#  messagebox.showinfo('info',s)   #show list that you choice
#  #value of button1
# bcheck1=BooleanVar()

#  #value of button2
# bcheck2=BooleanVar()

#  #value of button3
# bcheck3=BooleanVar()

# #create checkbuttons
# check1=Checkbutton(root,text='C++',variable=bcheck1)
# check2=Checkbutton(root,text='Java',variable=bcheck2)
# check3=Checkbutton(root,text='Python',variable=bcheck3)

# #create button
# btn=Button(root,text='choice',command=chebox)

# check1.pack()
# check2.pack()
# check3.pack()
# btn.pack()
# root.mainloop()
#####################################################################
#create combobox

#to call combobox
# from tkinter.ttk import Combobox

# #function to button
# def combo():
#     s1=c1.get()
#     s2=c2.get()
#     s=s1+' '+s2
#     messagebox.showinfo('info',s)

# #value of combo1    
# colors=['white','red','blue']

# #value of combo2   
# obj=['car','bus','motor']

# #value1
# c1=StringVar()
# c1.set('select color')

# #value1
# c2=StringVar()
# c2.set('select kind')

# #create combobox
# comb1=Combobox(root,values=colors,textvariable=c1,state='readonly')
# comb2=Combobox(root,values=obj,textvariable=c2,state='readonly')

# btn=Button(root,text='select',command=combo)
# comb1.pack()
# comb2.pack()
# btn.pack()
# root.mainloop()
##########################################################
#create text

#function button
# def copy():
#     txt=txt1.get('1.0','end').upper()#write start from row 1 to end
#     txt2.configure(state='normal') #put state normal to can delete it
#     txt2.delete('1.0','end')#delete to write again
#     txt2.insert('1.0',txt)#insert to txt2
#     txt2.configure(state='disabled')#set state
# btn=Button(root,text='copy',command=copy)
# btn.pack()
# #create text
# txt1=Text(root,width=30)
# txt1.pack(side='left')
# txt2=Text(root,width=30,state='disabled')
# txt2.pack(side='right')
# #note:text=entery but the difference is that text you can write in multiple column
# root.mainloop()

##############################################################
#coolors website =>a website contain colors that are harmony with us
###########################################################
# import img or icon to your page


#flaticon website=>is a website to icons

# import webbrowser#library about link of webbrowser
# def openlink():
#     webbrowser.open('https://www.google.com.eg/?hl=ar')
# img=PhotoImage(file='imgs/google.png') #import img
# btn=Button(root,text='Google',compound='left',image=img,relief='flat',padx=5,command=openlink) #link the img with button 
# btn.pack()
# root.mainloop()
########################################################
#how to show table(database) in gui
# from tkinter.ttk import *
# employees=[(1,'mohammed',400), #suppose that is the table that you want to show it
#            (2,'amr',500),
#            (3,'osama',600),
#            (4,'ahmed',700),
#            (5,'mahmoud',800),
#            (6,'hager',900),
#            (7,'asmaa',100),
#            (8,'Tasneem',5000),
#            (9,'aya',4000),
#            (10,'mariam',3000)
# ]
# columns=['id','name','salary'] #prepare columns 
# #create table
# tree=Treeview(root,columns=columns,show='headings',height=4)
# #write text on the heading
# tree.heading('id',text='id')
# tree.heading('name',text='Name')
# tree.heading('salary',text='Salary')
# #loop to insert in table
# for employ in employees:
#     tree.insert('','end',iid=employ[0],values=employ)
# #control width of column
# tree.column('id',width=40,anchor='center')
# tree.column('salary',anchor='center')
# #function to scroll
# scrollbar=Scrollbar(root,orient='vertical',command=tree.yview())
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0,column=1,sticky='ns')#sticky means from north to south
# #fun to btn 
# def selsected():
#     for select in tree.selection():
#         print(tree.item(select)['values']) #print result when click
# def delete(): #function to delete
#     for select in tree.selection():
#         tree.delete(select)
# def edit():#function to edit
#     for select in tree.selection():
#         tree.item(select,values=(1,2,3))

# btn=Button(root,text='click',command=selsected)
# btndelete=Button(root,text='delete',command=delete)
# btnedit=Button(root,text='edit',command=edit)
# tree.grid(row=0,column=0)    
# btn.grid(row=1,column=0) 
# btndelete.grid(row=2,column=0) 
# btnedit.grid(row=3,column=0) 
# root.mainloop()   
#################################################################
#button to exit from page
# def exit():
#     res=messagebox.askyesno('Exit','are you want to exit')
#     if res==True: #true =yes
#         root.destroy()#exit page
# btn=Button(root,text='Exit',command=exit)
# btn.pack()
# root.mainloop()   
##########################################################
#create shapes with canavas
# canvas=Canvas(root,width=200,height=200)
# #create line
# #canvas.create_line(10,10,190,190,fill='red',width=2)
# #create rectangle
# canvas.create_rectangle(10,10,190,190,fill='red')
# canvas.pack()
# root.mainloop()   
##########################################################
#create shapes with canavas
# canvas=Canvas(root,width=500,height=500)
# color=True
# for x in range(50,401,50):
#     for y in range(50,401,50):
#         if color==True:
#               canvas.create_rectangle(x,y,x+50,y+50,fill='white')
#         else:
#               canvas.create_rectangle(x,y,x+50,y+50,fill='black')  
#         color=not color
#     color=not color     

# canvas.pack()        
# root.mainloop()  
###############################################################
#create shapes with canavas(animation)
# w=500
# h=300
# x=0
# dx=3
# canvas=Canvas(root,width=w,height=h)
# canvas.create_rectangle(x,50,100,100,tags='car',fill='red')
# canvas.pack()
# while True:
#     canvas.move('car',dx,0)
#     canvas.after(20)
#     canvas.update()
#     if x<w:
#         x+=dx
#     else:
#         x=0
#         canvas.delete()    
#         canvas.create_rectangle(x,50,100,100,tags='car',fill='red')
# root.mainloop()
#######################################################################
#simpledialog =entry
# from tkinter import simpledialog
# def enter():
#     val=simpledialog.askstring("get val",'Enter x') #entry
#     if val is not None:
#         print(val)
#     else:
#         print("no value")    

# btn=Button(root,text='click',command=enter)
# btn.pack()
# root.mainloop()
######################################################
#button selet color
# from tkinter import colorchooser #import library of color
# def select():
#     color=colorchooser.askcolor(title="select color")  #choose color
#     if color is not None:
#         print(color[1])
#         root['bg']=color[1]
# btn=Button(root,text='click',command=select)
# btn.pack()
# root.mainloop()
##########################################################
#change icon of root
# from PIL import Image,ImageTk
# img=Image.open('imgs/google.png')
# ico=ImageTk.PhotoImage(img)
# root.iconphoto(False,ico)
# root.mainloop()
##########################################################
#multiple windows
# def new_window():
#     window=Toplevel() #create new window
#     lbl1=Label(window,text='label1')
#     lbl1.pack()
#     lbl2=Label(window,text='label2')
#     lbl2.pack()

# btn=Button(root,text='click',command=new_window)
# btn.pack()
# root.mainloop()


################################################ Done ################################################################