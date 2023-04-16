import sqlite3
from tkinter import *
from employee import epmployeeClass
from suppliers import suppliersClass
from category import categoryClass
from products import productClass
from sales import salesClass
from datetime import datetime
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #==title==
        self.title = Label(self.root, text="Inventory   Management  System", font=("times new roman", 40, "bold"),
                              bg="brown", fg="white", anchor="w",padx=20)
        self.title.place(x=0, y=0, relwidth=1, height=70)


        #----clock---
        self.lbl_clock = Label(self.root, text="", font=("times new roman", 15, "bold"), bg="blue", fg="AntiqueWhite2")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()



        #---------menu
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        #----menu_button

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), bg="dark green",fg="white").pack(side=TOP,fill=X)

        btn_logout = Button(LeftMenu, text="Employee", command= self.employee,font=("times new roman", 20, "bold"), bg="white",cursor="hand2",bd=3).pack(side=TOP,fill=X)

        btn_logout = Button(LeftMenu, text="Supplier",command= self.suppliers, font=("times new roman", 20, "bold"), bg="white", cursor="hand2",bd=3).pack(side=TOP, fill=X)

        btn_logout = Button(LeftMenu, text="Category",command= self.category, font=("times new roman", 20, "bold"), bg="white", cursor="hand2",bd=3).pack(side=TOP, fill=X)

        btn_logout = Button(LeftMenu, text="Products",command= self.product, font=("times new roman", 20, "bold"), bg="white", cursor="hand2",bd=3).pack(side=TOP, fill=X)

        btn_logout = Button(LeftMenu, text="Sales",command= self.sales, font=("times new roman", 20, "bold"), bg="white", cursor="hand2", bd=3).pack(side=TOP, fill=X)



        btn_exit = Button(LeftMenu, text="Exit",command=root.destroy, font=("times new roman", 20, "bold"), bg="white", cursor="hand2",bd=3).pack(side=TOP, fill=X)


        #==============content
        conn = sqlite3.connect('ims.db')
        c = conn.cursor()
        d = conn.cursor()

        # Execute a query to retrieve the total number of suppliers from the table
        c.execute("SELECT COUNT(*) FROM employee")
        c.execute("SELECT COUNT(*) FROM employee")
        total_employee = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM category")
        total_category = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM products")
        total_product = c.fetchone()[0]

        d.execute("SELECT COUNT(*) FROM supplier")
        total_supplier = d.fetchone()[0]



        self.lbl_employee = Label(self.root, text=f"Total Employee\n[ {total_employee} ]",font=("goudy old style", 25, "bold"), bd=5, relief= RIDGE, bg="brown", fg='white',)
        self.lbl_employee.place(x=300,y=120,height=200,width=300)

        self.lbl_employee = Label(self.root, text=f"Total Supplier\n[ {total_supplier} ]", font=("goudy old style", 25, "bold"),bd=5, relief=RIDGE, bg="bisque",
                                  fg='black', )
        self.lbl_employee.place(x=700, y=120, height=200, width=300)

        self.lbl_employee = Label(self.root, text=f"Total category\n[ {total_category} ]", font=("goudy old style", 25, "bold"), bd=5, relief=RIDGE, bg="lightgrey",
                                  )
        self.lbl_employee.place(x=300, y=420, height=200, width=300)

        self.lbl_employee = Label(self.root, text=f"Total product\n[ {total_product} ]", font=("goudy old style", 25, "bold"), bd=5, relief=RIDGE, bg="darkkhaki",
                                  fg='white', )
        self.lbl_employee.place(x=700, y=420, height=200, width=300)

    def update_clock(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
        self.lbl_clock.config(text=f"Welcome to Inventory Management System {current_time}")
        self.root.after(1000, self.update_clock)  # Update every 1 second







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

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)


    root.mainloop()