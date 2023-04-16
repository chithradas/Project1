from tkinter import *

class BillClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #==title==
        title = Label(self.root,text="Inventory Management System",font=("times new roman",40,"bold"),bg="brown",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===button_lo==
        btn_logout = Button(self.root,text="Logout",font=("times new roman",10,"bold"),bg="yellow",cursor="hand2").place(title,x=1100,y=10,height=30,width=150)
        #----clock---
        self.lbl_clock= Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-mm-yyyy \t\t Time: HH:MM:SS ",font=("times new roman",15,"bold"),bg="blue",fg="AntiqueWhite2").place(x=0,y=70,relwidth=1,height=30)

    if __name__ == "__main__":
        root = Tk()
        obj = BillClass(root)
        root.mainloop()