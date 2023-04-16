from tkinter import *
import sqlite3
from tkinter import ttk,messagebox



class suppliersClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x700+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ------------------------
        # All variable------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_desc= StringVar()


        self.var_name = StringVar()







        # ---frame
        self.lbl_clock = Label(self.root, text="Manage suppliers Details", font=("times new roman", 15, "bold"), bg="blue",
                               fg="AntiqueWhite2").place(x=10, y=100, width=800, height=30)

        # ---------content--------------------------------------------------------- row2
        lbl_Inv_no = Label(self.root, text="Invoice No.", font=("times new roman", 11, "bold"), bg="white",
                          fg="black").place(x=50, y=150)

        lbl_suppl = Label(self.root, text="Suppliers Name", font=("times new roman", 11, "bold"), bg="white",
                           fg="black").place(x=350, y=150)

        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 11, "bold"), bg="white",
                            fg="black").place(x=750, y=150)

        txt_inv_no = Entry(self.root, textvariable=self.var_sup_invoice, bg="lightyellow", fg="black").place(x=150, y=150,
                                                                                                       width=180)

        txt_supply = Entry(self.root, textvariable=self.var_name, bg="lightyellow", fg="black").place(x=500, y=150,
                                                                                                  width=180)



        txt_contact = Entry(self.root, textvariable=self.var_contact, bg="lightyellow", fg="black").place(x=850, y=150,
                                                                                                          width=180)

        lbl_desc = Label(self.root, text="Description", font=("times new roman", 11, "bold"), bg="white",
                            fg="black").place(x=40, y=250)

        txt_desc = Entry(self.root, textvariable=self.var_desc, bg="lightyellow", fg="black").place(x=150, y=250,height=75,
                                                                                                        width=400)

        # -------------------------button
        btn_add = Button(self.root, text='Save',command= self.add, bg='darkgreen', fg='white', cursor='hand2').place(x=550, y=305,
                                                                                                   width=110)
        btn_update = Button(self.root, text='Update',command= self.update, bg='grey', fg='white', cursor='hand2').place(x=700, y=305,
                                                                                                   width=110)
        btn_delete = Button(self.root, text='Delete',command= self.delete, bg='darkred', fg='white', cursor='hand2').place(x=850, y=305,
                                                                                                      width=110)
        btn_clear = Button(self.root, text='clear',command= self.clear, bg='darkblue', fg='white', cursor='hand2').place(x=1000, y=305,
                                                                                                     width=110)

        # ------------------suppliers frame

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=350)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frame, columns=("sid", "invno", "name", "contact"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.SupplierTable.heading("sid", text="Invoices")
        self.SupplierTable.heading("invno", text="Contact")
        self.SupplierTable.heading("name", text="Name")
        self.SupplierTable.heading("contact", text="Description")

        self.SupplierTable.column("sid", width="50")
        self.SupplierTable.column("invno", width="50")
        self.SupplierTable.column("name", width="50")
        self.SupplierTable.column("contact", width="50")



        self.SupplierTable["show"] = "headings"
        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice Must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This invoice already assigned, try diffrent", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO supplier( invoice, name, contact,desc) VALUES (?, ?, ?, ?)",
                        (
                            self.var_sup_invoice.get(),
                            self.var_name.get(),
                            self.var_contact.get(),
                            self.var_desc.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added succesfully", parent=self.root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)},parent=self.root")

    def get_data(self, ev):
        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content['values']

        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_desc.set(row[3]),



    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid invoice number", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?",
                        (
                            self.var_name.get(),
                            self.var_contact.get(),
                            self.var_desc.get(),
                            self.var_sup_invoice.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice Must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice", parent=self.root)
                else:
                    op =messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op == True:

                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier deleted successfully",parent=self.root)

                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.var_desc.set("")



if __name__=="__main__":
    root = Tk()
    obj = suppliersClass(root)
    root.mainloop()


