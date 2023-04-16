import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


class categoryClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x700+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="antiqueWhite2")
        self.root.focus_force()

        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        self.var_emp_id = StringVar()


        # ---frame
        lbl_title = Label(self.root, text="Manage Product Category", font=("goudy old style", 25, "bold"), bg="blue",fg="white",bd=3).pack(side=TOP,fill=X)

        lbl_cat_id = Label(self.root, text="Enter Category id", font=("goudy old style", 25, "bold"), fg="black").place(
            x=120, y=80)
        txt_cat_id = Entry(self.root,textvariable=self.var_cat_id, font=("goudy old style", 25, "bold"), bg="lightyellow", fg="black").place(x=600,
                                                                                                              y=80)

        lbl_name = Label(self.root,text="Enter Category Name",font=("goudy old style", 25, "bold"),fg="black").place(x= 120,y=150)
        txt_name = Entry(self.root,textvariable=self.var_name,  font=("goudy old style", 25, "bold"),bg="lightyellow",fg="black").place(x=600,y=150)

        btn_add = Button(self.root,text="Add",font=("goudy old style", 25, "bold"),command= self.add, bg="darkgreen", fg="white").place(x=650,y=320,width=120)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 25, "bold"),command= self.delete, bg="darkred", fg="white").place(x=850, y=320, width=120)

        # ------------------employee frame

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=450, relwidth=1, height=350)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.CategoryTable = ttk.Treeview(emp_frame, columns=("cid", "name"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        self.CategoryTable.heading("cid", text="Cat Id")
        self.CategoryTable.heading("name", text="Name")



        self.CategoryTable.column("cid", width=50)
        self.CategoryTable.column("name", width=50)



        self.CategoryTable["show"] = "headings"
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Id Must be required", parent=self.root)
            else:
                cur.execute("Select * from category where  catId=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Id already assigned, try diffrent", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO category( catId, name) VALUES (?, ?)",
                        (
                            self.var_cat_id.get(),
                            self.var_name.get(),

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "category added succesfully", parent=self.root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)},parent=self.root")

    def get_data(self, ev):
        f = self.CategoryTable.focus()
        content = (self.CategoryTable.item(f))
        row = content['values']

        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from  category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "ID Must be required", parent=self.root)
            else:
                cur.execute("Select * from category where catId=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid category ID", parent=self.root)
                else:
                    op =messagebox.askyesno("Confirm","Do you real want to delete?")
                    if op == True:

                        cur.execute("delete from category where catId=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee deleted successfully",parent=self.root)

                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_cat_id.set(""),
        self.var_name.set(""),

        self.show()

if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()


