from tkinter import *
from tkinter import ttk


class categoryClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x700+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="antiqueWhite2")
        self.root.focus_force()

        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        self.var_emp_id = StringVar()

        # ---frame
        lbl_title = Label(self.root, text="Manage Product Category", font=("goudy old style", 25, "bold"), bg="blue",fg="white",bd=3).pack(side=TOP,fill=X)

        lbl_name = Label(self.root,text="Enter Category Name",font=("goudy old style", 25, "bold"),fg="black").place(x= 120,y=120)
        txt_name = Entry(self.root, font=("goudy old style", 25, "bold"),bg="lightyellow",fg="black").place(x=650,y=120)

        btn_add = Button(self.root,text="Add",font=("goudy old style", 25, "bold"), bg="darkgreen", fg="white").place(x=650,y=320,width=120)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 25, "bold"), bg="red", fg="white").place(x=850, y=320, width=120)

        # ------------------employee frame

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=450, relwidth=1, height=350)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("cid", "name"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("cid", text="Cat Id")
        self.EmployeeTable.heading("name", text="Name")



        self.EmployeeTable.column("cid", width=50)
        self.EmployeeTable.column("name", width=50)



        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.pack(fill=BOTH, expand=1)


if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()


