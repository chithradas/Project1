from tkinter import *
from tkinter import ttk


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

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # ------------search frame--------------
        SearchFrame = LabelFrame(self.root, text="Invoice Number", bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)


        txt_search = Entry(SearchFrame, bg='lightyellow').place(x=200, y=10)
        btn_srch = Button(SearchFrame, text='Search', bg='darkgreen', fg='white', cursor='hand2').place(x=400, y=10,
                                                                                                        width=150)

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

        txt_inv_no = Entry(self.root, textvariable=self.var_emp_id, bg="lightyellow", fg="black").place(x=150, y=150,
                                                                                                       width=180)

        txt_supply = Entry(self.root, textvariable=self.var_gender, bg="white", fg="black").place(x=500, y=150,
                                                                                                  width=180)



        txt_contact = Entry(self.root, textvariable=self.var_contact, bg="lightyellow", fg="black").place(x=850, y=150,
                                                                                                          width=180)

        lbl_desc = Label(self.root, text="Description", font=("times new roman", 11, "bold"), bg="white",
                            fg="black").place(x=40, y=250)

        txt_inv_no = Entry(self.root, textvariable=self.var_emp_id, bg="lightyellow", fg="black").place(x=150, y=250,height=75,
                                                                                                        width=400)

        # -------------------------button
        btn_add = Button(self.root, text='Save', bg='darkgreen', fg='white', cursor='hand2').place(x=550, y=305,
                                                                                                   width=110)
        btn_update = Button(self.root, text='Update', bg='grey', fg='white', cursor='hand2').place(x=700, y=305,
                                                                                                   width=110)
        btn_delete = Button(self.root, text='Delete', bg='darkred', fg='white', cursor='hand2').place(x=850, y=305,
                                                                                                      width=110)
        btn_clear = Button(self.root, text='clear', bg='darkblue', fg='white', cursor='hand2').place(x=1000, y=305,
                                                                                                     width=110)

        # ------------------employee frame

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=350)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("sid", "invno", "name", "contact"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("sid", text="Supp Id")
        self.EmployeeTable.heading("invno", text="Inv No.")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("contact", text="Contact")

        self.EmployeeTable.column("sid", width="50")
        self.EmployeeTable.column("invno", width="50")
        self.EmployeeTable.column("name", width="50")
        self.EmployeeTable.column("contact", width="50")



        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.pack(fill=BOTH, expand=1)


if __name__=="__main__":
    root = Tk()
    obj = suppliersClass(root)
    root.mainloop()


