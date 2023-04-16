import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


class productClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x700+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="antiqueWhite2")
        self.root.focus_force()

        self.var_pro_id = StringVar()
        self.var_name = StringVar()


        self.var_cat_id = StringVar()


        # ---frame
        lbl_title = Label(self.root, text="Manage Product", font=("goudy old style", 25, "bold"), bg="blue",fg="white",bd=3).pack(side=TOP,fill=X)

        lbl_pro_id = Label(self.root, text="Enter product id", font=("goudy old style", 25, "bold"), fg="black").place(
            x=120, y=80)
        txt_pro_id = Entry(self.root,textvariable=self.var_pro_id, font=("goudy old style", 25, "bold"), bg="lightyellow", fg="black").place(x=600,
                                                                                                              y=80)

        lbl_name = Label(self.root,text="Enter Product Name",font=("goudy old style", 25, "bold"),fg="black").place(x= 120,y=150)
        txt_name = Entry(self.root,textvariable=self.var_name,  font=("goudy old style", 25, "bold"),bg="lightyellow",fg="black").place(x=600,y=150)

        lbl_cat_id = Label(self.root, text="Enter Category Name", font=("goudy old style", 25, "bold"), fg="black").place(
            x=120, y=220)
        txt_cat_id = Entry(self.root, textvariable=self.var_cat_id, font=("goudy old style", 25, "bold"), bg="lightyellow",
                         fg="black").place(x=600, y=220)

        btn_add = Button(self.root,text="Add",font=("goudy old style", 25, "bold"),command= self.add, bg="darkgreen", fg="white").place(x=650,y=320,width=120)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 25, "bold"),command= self.delete, bg="darkred", fg="white").place(x=850, y=320, width=120)

        # ------------------product frame

        pro_frame = Frame(self.root, bd=3, relief=RIDGE)
        pro_frame.place(x=0, y=450, relwidth=1, height=350)

        scrolly = Scrollbar(pro_frame, orient=VERTICAL)
        scrollx = Scrollbar(pro_frame, orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(pro_frame, columns=("pid", "name","cid"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("pid", text="Product Id")
        self.ProductTable.heading("name", text="Name")
        self.ProductTable.heading("cid", text="Category Id")



        self.ProductTable.column("pid", width=50)
        self.ProductTable.column("name", width=50)
        self.ProductTable.column("cid", width=50)



        self.ProductTable["show"] = "headings"
        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_pro_id.get() == "":
                messagebox.showerror("Error", "Id Must be required", parent=self.root)
            else:
                cur.execute("Select * from products where  proId=?", (self.var_pro_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Id already assigned, try diffrent", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO products( proId, name, catId ) VALUES (?, ?, ?)",
                        (
                            self.var_pro_id.get(),
                            self.var_name.get(),
                            self.var_cat_id.get(),

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "product added succesfully", parent=self.root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)},parent=self.root")

    def get_data(self, ev):
        f = self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        row = content['values']

        self.var_pro_id.set(row[0]),
        self.var_name.set(row[1]),


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from  products")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_pro_id.get() == "":
                messagebox.showerror("Error", "ID Must be required", parent=self.root)
            else:
                cur.execute("Select * from products where proId=?", (self.var_pro_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid product ID", parent=self.root)
                else:
                    op =messagebox.askyesno("Confirm","Do you real want to delete?")
                    if op == True:

                        cur.execute("delete from products where proId=?",(self.var_pro_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee deleted successfully",parent=self.root)

                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_pro_id.set(""),
        self.var_name.set(""),

        self.show()

if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()


