import os
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

class salesBillClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Sale Page")
        self.root.geometry("1100x700+220+130")

        self.var_invoice = StringVar()
        self.var_product = StringVar()

        self.var_catId = StringVar()
        self.var_quantity = StringVar()
        self.var_EmpId = StringVar()







        # Create labels and entry fields for invoice number, product name, category ID, quantity, and supplier
        self.invoice_label = Label(self.root, text="Invoice No.:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.invoice_entry = Entry(self.root,textvariable= self.var_invoice)
        self.product_label = Label(self.root, text="Product Name:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.product_entry = Entry(self.root,textvariable= self.var_product)
        self.category_label = Label(self.root, text="Category ID:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.category_entry = Entry(self.root,textvariable= self.var_catId)
        self.quantity_label = Label(self.root, text="Quantity:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.quantity_entry = Entry(self.root,textvariable= self.var_quantity)
        self.Emp_label = Label(self.root, text="Emp:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.Emp_entry = Entry(self.root,textvariable=self.var_EmpId)

        # Create sale button
        self.sale_button = Button(self.root, text="Sale", command=self.sale_item, bg='darkgreen', fg='white', cursor='hand2').place(x=10, y=300, width=280)

        # Layout widgets using grid layout manager
        self.invoice_label.grid(row=0, column=0, padx=10, pady=10)
        self.invoice_entry.grid(row=0, column=1, padx=10, pady=10)
        self.product_label.grid(row=1, column=0, padx=10, pady=10)
        self.product_entry.grid(row=1, column=1, padx=10, pady=10)
        self.category_label.grid(row=2, column=0, padx=10, pady=10)
        self.category_entry.grid(row=2, column=1, padx=10, pady=10)
        self.quantity_label.grid(row=3, column=0, padx=10, pady=10)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)
        self.Emp_label.grid(row=4, column=0, padx=10, pady=10)
        self.Emp_entry.grid(row=4, column=1, padx=10, pady=10)

        # -------------------------------------sale frame

        sale_frame = Frame(self.root, bd=3, relief=RIDGE)
        sale_frame.place(x=0, y=450, relwidth=1, height=350)

        scrolly = Scrollbar(sale_frame, orient=VERTICAL)
        scrollx = Scrollbar(sale_frame, orient=HORIZONTAL)

        self.saleTable = ttk.Treeview(sale_frame, columns=("invoice", "product_name", "catId", "quantity", "emp_id",),
                                     yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.saleTable.xview)
        scrolly.config(command=self.saleTable.yview)

        self.saleTable.heading("invoice", text="invoice")
        self.saleTable.heading("product_name", text="Name")
        self.saleTable.heading("catId", text="Cat Id")
        self.saleTable.heading("quantity", text="quantity")
        self.saleTable.heading("emp_id", text="Emp_Id")


        self.saleTable.column("invoice", width=100)
        self.saleTable.column("product_name", width=200)
        self.saleTable.column("catId", width=100)
        self.saleTable.column("quantity", width=100)
        self.saleTable.column("emp_id", width=100)

        self.saleTable.pack(fill=BOTH, expand=1)
        #self.show_data()  # Call show_data() function to populate the table


        self.saleTable["show"] = "headings"
        self.saleTable.pack(fill=BOTH, expand=1)
        self.saleTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()

    def show_data(self):
        # Connect to database
        conn = sqlite3.connect("ims.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sale")
        rows = cursor.fetchall()

        # Delete previous data in the table
        for i in self.saleTable.get_children():
            self.saleTable.delete(i)

        # Insert data into the table
        for row in rows:
            self.saleTable.insert('', END, values=row)

        conn.close()


    def sale_item(self):
        # Get values from entry fields
        invoice = self.invoice_entry.get()
        product_name = self.product_entry.get()
        category_id = int(self.category_entry.get())
        quantity = int(self.quantity_entry.get())
        Emp = self.Emp_entry.get()

        # Validate data
        if not invoice or not product_name or not category_id or not quantity or not Emp:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Insert data into the database
        conn = sqlite3.connect("ims.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sale (invoice, product_name, catId, quantity, Emp_id) VALUES (?, ?, ?, ?, ?)",
                       (invoice, product_name, category_id, quantity, Emp))
        conn.commit()
        conn.close()

        # Show success message
        messagebox.showinfo("Success", "Item sold successfully.")
        self.show_data()  # Refresh the table after adding new data

        # Clear entry fields
        self.invoice_entry.delete(0, END)
        self.product_entry.delete(0, END)
        self.category_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.Emp_entry.delete(0, END)


        # Create bills directory if it doesn't exist
        if not os.path.exists("bills"):
            os.makedirs("bills")

        # Generate text file with information
        with open(f"bills/{invoice}.txt", "w") as f:
            f.write(f"Invoice No.: {invoice}\n")
            f.write(f"Product Name: {product_name}\n")
            f.write(f"Category ID: {category_id}\n")
            f.write(f"Quantity: {quantity}\n")
            f.write(f"Employee Id: {Emp}\n")

            # Create bills directory if it doesn't exist
            if not os.path.exists("bills"):
                os.makedirs("bills")

    def get_data(self, ev):
        f = self.saleTable.focus()
        content = (self.saleTable.item(f))
        row = content['values']

        self.var_invoice.set(row[0]),
        self.var_product.set(row[1]),
        self.var_catId.set(row[2]),
        self.var_quantity.set(row[3]),
        self.var_EmpId.set(row[4])

        self.show_data()










# Create main window and run application
if __name__=="__main__":
    root = Tk()
    obj = salesBillClass(root)
    root.mainloop()