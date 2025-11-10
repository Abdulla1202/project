import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

# ---------- DATABASE CONNECTION ----------
def connect_db():
    try:
        conn = psycopg2.connect( # create new database connection with PostgreSQL server
            host="localhost",
            database="company",
            user="postgres",
            password="7523Abdulla&"
        )
        return conn
    except Exception as e: # agr try block mein koi bhi exception (error) aata hai, control yahan aayega
        messagebox.showerror("DB Error", f"Cannot connect to PostgreSQL:\n{e}")
        exit()

conn = connect_db()
cur = conn.cursor()

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("900x500")
root.resizable(True, True)

# ---------- VARIABLES ----------
name_var = tk.StringVar()
cat_var = tk.StringVar()
qty_var = tk.StringVar()
price_var = tk.StringVar()
sup_var = tk.StringVar()

# ---------- FUNCTIONS ----------
def refresh_table():
    """Reload data from PostgreSQL and show in Treeview."""
    for i in tree.get_children():
        tree.delete(i)

    cur.execute("SELECT * FROM items ORDER BY id ASC;")
    rows = cur.fetchall()

    # Show continuous serial numbers for display but keep DB id hidden
    for i, row in enumerate(rows, start=1):
        display_row = (i, row[0], row[1], row[2], row[3], row[4], row[5])
        tree.insert("", "end", values=display_row)

        # 🔴 Low stock check
        if int(row[3]) < 5:  # quantity column (index 3)
            tree.item(tree.get_children()[-1], tags=('low_stock',))

    # 🔧 Red color tag configuration (once)
    tree.tag_configure('low_stock', background='#FFB6B6')  # light red/pink

def add_item():
    name = name_var.get()
    cat = cat_var.get()
    qty = qty_var.get() or 0
    price = price_var.get() or 0.0
    sup = sup_var.get()

    if name.strip() == "":
        messagebox.showwarning("Input Error", "Item name is required!")
        return

    try:
        cur.execute(
            "INSERT INTO items (name, category, quantity, price, supplier) VALUES (%s,%s,%s,%s,%s)",
            (name, cat, qty, price, sup)
        )
        conn.commit()
        messagebox.showinfo("Success", f"Item '{name}' added!")
        clear_fields()
        refresh_table()
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", f"Failed to add item:\n{e}")

def delete_item():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a row to delete")
        return

    values = tree.item(selected)["values"]
    db_id = values[1]  # 2nd column me actual DB id hota hai wo bhi unique

    try:
        cur.execute("DELETE FROM items WHERE id=%s", (db_id,))
        conn.commit()
        messagebox.showinfo("Deleted", f"Item ID {db_id} deleted successfully!")
        refresh_table()
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", f"Delete failed:\n{e}")

def update_item():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a row to update")
        return

    values = tree.item(selected)["values"] # values is a list of all column values of selected row
    db_id = values[1]  # (2nd column) me id h

    # --- Step 1: Fetch current values from DB ---
    cur.execute("SELECT name, category, quantity, price, supplier FROM items WHERE id=%s", (db_id,))
    current = cur.fetchone()
    if not current:
        messagebox.showerror("Error", "Record not found!")
        return

    # --- Step 2: Use old values if new input is blank ---
    name = name_var.get().strip() or current[0]
    cat = cat_var.get().strip() or current[1]
    qty = qty_var.get().strip() or current[2]
    price = price_var.get().strip() or current[3]
    sup = sup_var.get().strip() or current[4]

    try:
        cur.execute("""
            UPDATE items
            SET name=%s, category=%s, quantity=%s, price=%s, supplier=%s
            WHERE id=%s
        """, (name, cat, qty, price, sup, db_id))
        conn.commit()
        messagebox.showinfo("Updated", f"Item ID {db_id} updated successfully!")
        refresh_table()
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", f"Update failed:\n{e}")


def clear_fields():
    name_var.set("")
    cat_var.set("")
    qty_var.set("")
    price_var.set("")
    sup_var.set("")

# ---------- UI LAYOUT ----------
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.X)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame, textvariable=name_var, width=20).grid(row=0, column=1)

tk.Label(frame, text="Category").grid(row=0, column=2)
tk.Entry(frame, textvariable=cat_var, width=15).grid(row=0, column=3)

tk.Label(frame, text="Qty").grid(row=0, column=4)
tk.Entry(frame, textvariable=qty_var, width=10).grid(row=0, column=5)

tk.Label(frame, text="Price").grid(row=0, column=6)
tk.Entry(frame, textvariable=price_var, width=10).grid(row=0, column=7)

tk.Label(frame, text="Supplier").grid(row=1, column=0)
tk.Entry(frame, textvariable=sup_var, width=20).grid(row=1, column=1)

# ---------- Buttons ----------
tk.Button(frame, text="Add", command=add_item, bg="#4CAF50", fg="white").grid(row=1, column=2, padx=5)
tk.Button(frame, text="Update", command=update_item, bg="#2196F3", fg="white").grid(row=1, column=3, padx=5)
tk.Button(frame, text="Delete", command=delete_item, bg="#E30BEB", fg="white").grid(row=1, column=4, padx=5)
tk.Button(frame, text="Clear", command=clear_fields , bg="#E34F19" , fg="white").grid(row=1, column=5, padx=5)
tk.Button(frame, text="Refresh", command=refresh_table, bg="#7536F4", fg="white").grid(row=1, column=6, padx=5)

# ---------- Table ----------
cols = ("S.No", "ID", "Name", "Category", "Quantity", "Price", "Supplier")
tree = ttk.Treeview(root, columns=cols, show="headings", height=15)

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor=tk.CENTER)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

refresh_table()
root.mainloop()
