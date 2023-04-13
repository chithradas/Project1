from tkinter import *
from employee import epmployeeClass
from suppliers import suppliersClass
from category import categoryClass
from products import productClass
class IMS:
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

        #---------menu
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        #----menu_button

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), bg="dark green",fg="white").pack(side=TOP,fill=X)

        btn_logout = Button(LeftMenu, text="Employee", command= self.employee,font=("times new roman", 20, "bold"), bg="white",cursor="hand2",bd=3).pack(side=TOP,fill=X)

        btn_logout = Button(LeftMenu, text="Supplier",command= self.suppliers, font=("times new roman", 20, "bold"), bg="white", cursor="hand2",bd=3).pack(side=TOP, fill=X)

        btn_logout = Button(LeftMenu, text="Category",command= self.category, font=("times new roman", 20, "bold"), bg="white", cursor="hand2",bd=3).pack(side=TOP, fill=X)

        btn_logout = Button(LeftMenu, text="Products",command= self.product, font=("times new roman", 20, "bold"), bg="white", cursor="hand2",bd=3).pack(side=TOP, fill=X)

        btn_logout = Button(LeftMenu, text="Sales", font=("times new roman", 20, "bold"), bg="white", cursor="hand2", bd=3).pack(side=TOP, fill=X)

        btn_logout = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg="white", cursor="hand2",bd=3).pack(side=TOP, fill=X)


        #==============content

        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief= RIDGE, bg="#33bbf9", fg='white',)
        self.lbl_employee.place(x=300,y=120,height=200,width=300)

        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9",
                                  fg='white', )
        self.lbl_employee.place(x=700, y=120, height=200, width=300)

        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9",
                                  fg='white', )
        self.lbl_employee.place(x=300, y=420, height=200, width=300)

        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9",
                                  fg='white', )
        self.lbl_employee.place(x=700, y=420, height=200, width=300)

#-------------------------------------------------------

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = epmployeeClass(self.new_win)

    def suppliers(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = suppliersClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()