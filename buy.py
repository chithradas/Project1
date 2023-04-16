import os
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

class BuyClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Buy Page")
        self.root.geometry("1100x700+220+130")

        self.var_invoice = StringVar()
        self.var_product = StringVar()

        self.var_catId = StringVar()
        self.var_quantity = StringVar()
        self.var_supId = StringVar()







        # Create labels and entry fields for invoice number, product name, category ID, quantity, and supplier
        self.invoice_label = Label(self.root, text="Invoice No.:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.invoice_entry = Entry(self.root,textvariable= self.var_invoice)
        self.product_label = Label(self.root, text="Product Name:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.product_entry = Entry(self.root,textvariable= self.var_product)
        self.category_label = Label(self.root, text="Category ID:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.category_entry = Entry(self.root,textvariable= self.var_catId)
        self.quantity_label = Label(self.root, text="Quantity:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.quantity_entry = Entry(self.root,textvariable= self.var_quantity)
        self.supplier_label = Label(self.root, text="Supplier:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.supplier_entry = Entry(self.root,textvariable=self.var_supId)

        # Create buy button
        self.buy_button = Button(self.root, text="Buy", command=self.buy_item, bg='darkgreen', fg='white', cursor='hand2').place(x=10, y=300, width=280)

        # Layout widgets using grid layout manager
        self.invoice_label.grid(row=0, column=0, padx=10, pady=10)
        self.invoice_entry.grid(row=0, column=1, padx=10, pady=10)
        self.product_label.grid(row=1, column=0, padx=10, pady=10)
        self.product_entry.grid(row=1, column=1, padx=10, pady=10)
        self.category_label.grid(row=2, column=0, padx=10, pady=10)
        self.category_entry.grid(row=2, column=1, padx=10, pady=10)
        self.quantity_label.grid(row=3, column=0, padx=10, pady=10)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)
        self.supplier_label.grid(row=4, column=0, padx=10, pady=10)
        self.supplier_entry.grid(row=4, column=1, padx=10, pady=10)

        # -------------------------------------buy frame

        buy_frame = Frame(self.root, bd=3, relief=RIDGE)
        buy_frame.place(x=0, y=450, relwidth=1, height=350)

        scrolly = Scrollbar(buy_frame, orient=VERTICAL)
        scrollx = Scrollbar(buy_frame, orient=HORIZONTAL)

        self.buyTable = ttk.Treeview(buy_frame, columns=("invoice", "product_name", "catId", "quantity", "sup_id",),
                                     yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.buyTable.xview)
        scrolly.config(command=self.buyTable.yview)

        self.buyTable.heading("invoice", text="invoice")
        self.buyTable.heading("product_name", text="Name")
        self.buyTable.heading("catId", text="Cat Id")
        self.buyTable.heading("quantity", text="quantity")
        self.buyTable.heading("sup_id", text="Sup Id")


        self.buyTable.column("invoice", width=100)
        self.buyTable.column("product_name", width=200)
        self.buyTable.column("catId", width=100)
        self.buyTable.column("quantity", width=100)
        self.buyTable.column("sup_id", width=100)

        self.buyTable.pack(fill=BOTH, expand=1)
        #self.show_data()  # Call show_data() function to populate the table


        self.buyTable["show"] = "headings"
        self.buyTable.pack(fill=BOTH, expand=1)
        self.buyTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()

    def show_data(self):
        # Connect to database
        conn = sqlite3.connect("ims.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM buy")
        rows = cursor.fetchall()

        # Delete previous data in the table
        for i in self.buyTable.get_children():
            self.buyTable.delete(i)

        # Insert data into the table
        for row in rows:
            self.buyTable.insert('', END, values=row)

        conn.close()


    def buy_item(self):
        # Get values from entry fields
        invoice = self.invoice_entry.get()
        product_name = self.product_entry.get()
        category_id = int(self.category_entry.get())
        quantity = int(self.quantity_entry.get())
        supplier = self.supplier_entry.get()

        # Validate data
        if not invoice or not product_name or not category_id or not quantity or not supplier:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Insert data into the database
        conn = sqlite3.connect("ims.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO buy (invoice, product_name, catId, quantity, sup_id) VALUES (?, ?, ?, ?, ?)",
                       (invoice, product_name, category_id, quantity, supplier))
        conn.commit()
        conn.close()

        # Show success message
        messagebox.showinfo("Success", "Item bought successfully.")
        self.show_data()  # Refresh the table after adding new data

        # Clear entry fields
        self.invoice_entry.delete(0, END)
        self.product_entry.delete(0, END)
        self.category_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.supplier_entry.delete(0, END)


        # Create bills directory if it doesn't exist
        if not os.path.exists("bills"):
            os.makedirs("bills")

        # Generate text file with information
        with open(f"bills/{invoice}.txt", "w") as f:
            f.write(f"Invoice No.: {invoice}\n")
            f.write(f"Product Name: {product_name}\n")
            f.write(f"Category ID: {category_id}\n")
            f.write(f"Quantity: {quantity}\n")
            f.write(f"Supplier: {supplier}\n")

            # Create bills directory if it doesn't exist
            if not os.path.exists("bills"):
                os.makedirs("bills")

    def get_data(self, ev):
        f = self.buyTable.focus()
        content = (self.buyTable.item(f))
        row = content['values']
        print(row)
        self.var_invoice.set(row[0]),
        self.var_product.set(row[1]),
        self.var_catId.set(row[2]),
        self.var_quantity.set(row[3]),
        self.var_supId.set(row[4]),










# Create main window and run application
if __name__=="__main__":
    root = Tk()
    obj = BuyClass(root)
    root.mainloop()