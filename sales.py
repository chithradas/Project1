import os
from tkinter import *
import sqlite3
from tkinter import ttk,messagebox

class salesClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x700+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice = StringVar()

        lbl_title = Label(self.root, text="Customer Bill Area", font=("goudy old style", 25, "bold"), bg="blue",
                          fg="white", bd=3).pack(side=TOP, fill=X)

        lbl_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15, "bold"), bg="white",
                          fg="black", bd=3).place(x=50,y=100)

        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 15, "bold"), bg="lightyellow",
                            fg="black", bd=3).place(x=160, y=100)


        btn_search = Button(self.root,text="Search",command= self.search,  font=("goudy old style", 15, "bold"), bg="darkgreen",
                            fg="white",cursor="hand2" ,bd=3).place(x=370, y=100,height=28,)

        btn_clear = Button(self.root, text="Clear",command= self.clear,font=("goudy old style", 15, "bold"), bg="lightgrey",
                            fg="black", cursor="hand2", bd=3).place(x=450, y=100, height=28, )

        # -----------Bill List--------------
        sale_Frame = LabelFrame(self.root, text="Search Em",bd=3,relief=RIDGE)
        sale_Frame.place(x=50, y=140, width=200, height=330)

        scrolly=Scrollbar(sale_Frame,orient=VERTICAL)
        self.Sales_List=Listbox(sale_Frame, font=("goudy old style", 15, "bold"), bg="lightgrey",yscrollcommand=scrolly.set)

        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)
        self.show()


        # -----------Bill Area--------------

        bill_Frame = LabelFrame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)
        lbl_title2 = Label(bill_Frame, text="Customer Bill Area", font=("goudy old style", 15, "bold"), bg="orange",
                           fg="black", bd=3).pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, font=("goudy old style", 15, "bold"), bg="lightyellow",
                                  yscrollcommand=scrolly2.set)

        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)


    #---------------------------------------------------------
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0,END)
        for i in os.listdir('bill'):
            if i.split(".")[-1] == "txt":
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split(".")[0])

    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name = self.Sales_List.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be required",parent= self.root)

        else:
            if self.var_invoice.get() in self.bill_list:

                fp = open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()

            else:
                messagebox.showerror("Error","Invoice no. should be required",parent= self.root)

    def clear(self):
        self.show()
        self.bill_area.delete("1.0",END)















if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()