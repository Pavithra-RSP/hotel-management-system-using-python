from tkinter import*
from supplier import supplier_win
from event import eventbooking 
#from PIL import ImageTk,Image

class eventmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("EVENT MANAGEMENT SYSTEM")
        self.root.geometry("1150x800+0+0")
    

        '''img1=Image.open(Image.open("images.jpeg"))
        img1=img1.resize((1150,140),Image.ANTIALIAS)
        self.photoimg1=Image.photoImage(img1)'''


        label_title=Label(self.root,text="EVENT MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        label_title.place(x=0,y=140,width=1150,height=50)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1150,height=620)

        label_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        label_menu.place(x=0,y=0,width=230)

        button_frame=Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=228,height=190)

        admin_button=Button(button_frame,text="ADMIN",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        admin_button.grid(row=0,column=0,pady=1)

        supplier_button=Label(button_frame,text="SUPPLIER",command=self.supplier_win,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        supplier_button.grid(row=1,column=0,pady=1)

        customer_button=Label(button_frame,text="CUSTOMER",command=self.eventbooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        customer_button.grid(row=2,column=0,pady=1)

        report_button=Label(button_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_button.grid(row=3,column=0,pady=1)

        logout_button=Label(button_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_button.grid(row=4,column=0,pady=1)
    def supplier_details(self):
        self.new_window=Toplevel(self.root)
        self.app=supplier_win(self.new_window)

    def eventbooking(self):
        self.new_window=Toplevel(self.root)
        self.app=eventbooking(self.new_window)


        




if __name__=="__main__":
    root=Tk()
    obj=eventmanagementsystem(root)
    root.mainloop()
            

    
