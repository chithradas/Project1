from tkinter import *
from tkinter import ttk


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
        self.var_salary = StringVar()




        #------------search frame--------------
        SearchFrame = LabelFrame(self.root,text="Search Employee",bg= "white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #-------option
        cmb_saerch = ttk.Combobox(SearchFrame,textvariable= self.var_searchby,values= ("Select","Email","Name","Contact"),state= 'readonly',justify=CENTER,)
        cmb_saerch.place(x=10,y=10,width=180)
        cmb_saerch.current(0)

        txt_search = Entry(SearchFrame,bg='lightyellow').place(x=200,y=10)
        btn_srch = Button(SearchFrame,text='Search',bg='darkgreen',fg='white',cursor='hand2').place(x=400,y=10,width=150)

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



        self.txt_address = Text(Entry(self.root, bg="lightyellow", fg="black").place(x=150, y=270))

        txt_salary= Entry(self.root, textvariable=self.var_salary, bg="lightyellow", fg="black").place(x=500, y=270,width=180)

        #-------------------------button
        btn_add = Button(self.root, text='Save', bg='darkgreen', fg='white', cursor='hand2').place(x=500, y=305,width=110)
        btn_update = Button(self.root, text='Update', bg='grey', fg='white', cursor='hand2').place(x=650, y=305,
                                                                                                      width=110)
        btn_delete = Button(self.root, text='Delete', bg='darkred', fg='white', cursor='hand2').place(x=800, y=305,width=110)
        btn_clear = Button(self.root, text='clear', bg='darkblue', fg='white', cursor='hand2').place(x=950, y=305,width=110)


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



















if __name__=="__main__":
    root = Tk()
    obj = epmployeeClass(root)
    root.mainloop()


