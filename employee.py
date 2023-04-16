from tkinter import *
from tkinter import ttk,messagebox
import sqlite3


class epmployeeClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x700+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #------------------------
        # All variable-------
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
        self.var_address = StringVar()
        self.var_salary = StringVar()





        #------------search frame--------------
        SearchFrame = LabelFrame(self.root,text="Search Employee",bg= "white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #-------option
        cmb_saerch = ttk.Combobox(SearchFrame,textvariable= self.var_searchby,values= ("Select","Email","Name","Contact"),state= 'readonly',justify=CENTER,)
        cmb_saerch.place(x=10,y=10,width=180)
        cmb_saerch.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt,bg='lightyellow').place(x=200,y=10)
        btn_srch = Button(SearchFrame,text='Search',command= self.search,bg='darkgreen',fg='white',cursor='hand2').place(x=400,y=10,width=150)

        #---frame
        self.lbl_clock = Label(self.root,text="Employee Details",font=("times new roman", 15, "bold"), bg="blue", fg="AntiqueWhite2").place(x=10, y=100,width=800,height=30)

        #---------content--------------------------------------------------------- row2
        lbl_empid = Label(self.root, text="Employee ID", font=("times new roman", 11, "bold"), bg="white",fg="black").place(x=50, y=150)

        lbl_gender = Label(self.root, text="Gender", font=("times new roman" ,11, "bold"), bg="white",fg="black").place(x=400, y=150)




        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 11, "bold"), bg="white",fg="black").place(x=750, y=150)

        txt_empid = Entry(self.root,  textvariable= self.var_emp_id , bg="lightyellow",fg="black").place(x=150, y=150,width=180)

        txt_gender = Entry(self.root, textvariable= self.var_gender, bg="white",fg="black").place(x=500, y=150,width=180)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select", "Male", "Female", "Other"), state='readonly', justify=CENTER, )
        cmb_gender.place(x=500, y=150,width=180)
        cmb_gender.current(0)

        txt_contact = Entry(self.root,textvariable= self.var_contact,  bg="lightyellow",fg="black").place(x=850, y=150,width=180)

        lbl_empid = Label(self.root, text="Employee ID", font=("times new roman", 11, "bold"), bg="white",
                          fg="black").place(x=50, y=150)


        # ---------content--------------------------------------------------------- row2
        lbl_name = Label(self.root, text="Name", font=("times new roman", 11, "bold"), bg="white",
                          fg="black").place(x=50, y=190)

        lbl_dob = Label(self.root, text="D.O.B", font=("times new roman", 11, "bold"), bg="white",
                           fg="black").place(x=400, y=190)

        lbl_doj = Label(self.root, text="D.O.J", font=("times new roman", 11, "bold"), bg="white",
                            fg="black").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, bg="lightyellow", fg="black").place(x=150, y=190,
                                                                                                       width=180)

        txt_dob = Entry(self.root, textvariable=self.var_dob, bg="lightyellow", fg="black").place(x=500, y=190,
                                                                                                  width=180)


        txt_doj = Entry(self.root, textvariable=self.var_doj, bg="lightyellow", fg="black").place(x=850, y=190,
                                                                                                          width=180)


 # ---------content--------------------------------------------------------- row3
        lbl_email= Label(self.root, text="Email", font=("times new roman", 11, "bold"), bg="white",
                          fg="black").place(x=50, y=240)

        lbl_password= Label(self.root, text="Password", font=("times new roman", 11, "bold"), bg="white",
                           fg="black").place(x=400, y=240)

        lbl_user = Label(self.root, text="User Type", font=("times new roman", 11, "bold"), bg="white",
                            fg="black").place(x=750, y=240)

        txt_email = Entry(self.root, textvariable=self.var_email, bg="lightyellow", fg="black").place(x=150, y=240,
                                                                                                       width=180)

        txt_password = Entry(self.root, textvariable=self.var_pass, bg="lightyellow", fg="black").place(x=500, y=240,
                                                                                                  width=180)


        txt_user = Entry(self.root, textvariable=self.var_utype, bg="lightyellow", fg="black").place(x=850, y=240,width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Select", "admin" ,"employee"),
                                  state='readonly', justify=CENTER, )
        cmb_utype.place(x=850, y=240,width=180)
        cmb_utype.current(0)

# ---------content--------------------------------------------------------- row3
        lbl_address= Label(self.root, text="Address", font=("times new roman", 11, "bold"), bg="white",
                          fg="black").place(x=50, y=270)

        lbl_salary= Label(self.root, text="Salary", font=("times new roman", 11, "bold"), bg="white",
                           fg="black").place(x=400, y=270)



        txt_address = Entry(self.root, textvariable=self.var_address,bg="lightyellow", fg="black").place(x=150, y=270)

        txt_salary= Entry(self.root, textvariable=self.var_salary, bg="lightyellow", fg="black").place(x=500, y=270,width=180)

        #-------------------------button
        btn_add = Button(self.root, text='Save',command= self.add, bg='darkgreen', fg='white', cursor='hand2').place(x=500, y=305,width=110)
        btn_update = Button(self.root, text='Update',command=self.update, bg='grey', fg='white', cursor='hand2').place(x=650, y=305,
                                                                                                      width=110)
        btn_delete = Button(self.root, text='Delete',command=self.delete, bg='darkred', fg='white', cursor='hand2').place(x=800, y=305,width=110)
        btn_clear = Button(self.root, text='clear',command=self.clear, bg='darkblue', fg='white', cursor='hand2').place(x=950, y=305,width=110)


        #------------------employee frame

        emp_frame = Frame(self.root,bd=3,relief= RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=350)

        scrolly= Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient= HORIZONTAL)


        self.EmployeeTable = ttk.Treeview(emp_frame,columns = ("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side= BOTTOM,fill=X)
        scrolly.pack(side= RIGHT,fill=Y )
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="Emp Id")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="DOB")
        self.EmployeeTable.heading("doj", text="DOJ")

        self.EmployeeTable.heading("pass", text="Emp Id")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable.column("eid", width=50)
        self.EmployeeTable.column("name", width=50)
        self.EmployeeTable.column("email", width=50)
        self.EmployeeTable.column("gender", width=50)
        self.EmployeeTable.column("contact", width=50)
        self.EmployeeTable.column("dob", width=50)
        self.EmployeeTable.column("doj", width=50)

        self.EmployeeTable.column("pass", width=50)
        self.EmployeeTable.column("utype", width=50)
        self.EmployeeTable.column("address", width=50)
        self.EmployeeTable.column("salary", width=50)


        self.EmployeeTable["show"]="headings"
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()




#-----------------------------------------------------------------------------------------------------------------
    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This employee ID already assigned, try diffrent", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO employee (eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.var_address.get(),
                            self.var_salary.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added succesfully", parent=self.root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)},parent=self.root")


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row = content['values']
        print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.var_address.set(row[9]),

        self.var_salary.set(row[10])

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid employee ID", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE employee set  name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? where eid=?",
                        (

                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.var_address.get(),
                            self.var_salary.get(),
                            self.var_emp_id.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee updated succesfully", parent=self.root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid employee ID", parent=self.root)
                else:
                    op =messagebox.askyesno("Confirm","Do you real want to delete?")
                    if op == True:

                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee deleted successfully",parent=self.root)

                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.var_address.set(""),

        self.var_salary.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Select Search by option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("search input required", parent=self.root)
            else:
                query = "SELECT * FROM employee WHERE " + self.var_searchby.get() + " LIKE '%"+self.var_searchtxt.get()+"%'"
                cur.execute(query)
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                    con.commit()
                else:
                    messagebox.showinfo("No search results found. Please try again", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error occurred while searching", parent=self.root, detail=ex)





if __name__=="__main__":
    root = Tk()
    obj = epmployeeClass(root)
    root.mainloop()


