import tkinter as tk
from tkinter import messagebox
import os
from tkinter import *

# Window
root = tk.Tk()
root.title("MiniBlog")
root.geometry("1300x1000")
root.config(bg="lightblue")

# ----------- Functions -----------

def save_post():
    name = name_entry.get()
    title = title_entry.get()
    content = content_text.get("1.0", "end-1c")

    if title == "" or content == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    with open(name+"_"+title+".txt", "x") as file:
        file.write("Blog Title: " + title + "\n")
        file.write("Content:\n" + content)

    messagebox.showinfo("Success", "Post Saved Successfully!")

def open_post():
    files = os.listdir()
    print(files)
    item = []
    for file in files:
        if file.endswith(".txt"):
            item.append(file)

    root.title("My List")
    listbox = tk.Listbox(root)
            
    for items in item:
        listbox.insert(tk.END, items)
        listbox.grid(row=0, column=0)

folder_path = "."

file_name_entry = tk.Entry(root, width=40)
file_name_entry.grid(row=2,column=1)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=3,column=0)

def load_files():
    listbox.delete(0, tk.END)
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith(".txt"):
            listbox.insert(tk.END, file)

def delete_file():
    selected = listbox.curselection()

    if not selected:
        print("File is Not Selected?")
        messagebox.showwarning("File","File is Not Selected!")
        return
    
    file_name = listbox.get(selected)
    file_path =os.path.join(folder_path, file_name)

    os.remove(file_path)
    print(f"{file_name} is Deleted")

    messagebox.showinfo("Delete",f"Delete {file_name} Successfully!")

    load_files()

def view_file():
    selected = listbox.curselection()
    if not selected:
        print("file is not Selected!")
        return

    file_name = listbox.get(selected)
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "r") as f:
        content = f.read()

    text_box.delete("1.0",tk.END)
    text_box.insert(tk.END, content)

    file_name_entry.delete(0, tk.END)
    file_name_entry.insert(0, file_name)


def save_file(file_name, content):
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path,"w") as f:
        f.write(content)

    print(f"{file_name} save ho gayi")

    messagebox.showinfo("File","File Update Successfully!")

def save_post():
    file_name = file_name_entry.get()
    content = text_box.get("1.0",tk.END)

    if not file_name:
        print("Enter File Name")
        return

    save_file(file_name, content)

    load_files()

# ----------- UI Design -----------

# Name
tk.Label(root, text="Enter Your Name:", bg="lightblue", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=20, pady=10, sticky="w")
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=0, column=1, padx=20, pady=10)

# Title
tk.Label(root, text="Enter Blog Title:", bg="lightblue", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=20, pady=10, sticky="w")
title_entry = tk.Entry(root, width=40)
title_entry.grid(row=1, column=1, padx=20, pady=10)

# Content
tk.Label(root, text="Enter Content:", bg="lightblue", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=20, pady=10, sticky="nw")
content_text = tk.Text(root, height=15, width=50)
content_text.grid(row=2, column=1, padx=20, pady=10)

# Button
tk.Button(root, text="Save Post", command=save_post, bg="white", font=("Arial", 12, "bold")).grid(row=3, column=1, pady=20)
tk.Button(root, text="View Post", command=open_post, bg="white", font=("Arial", 12, "bold")).grid(row=4, column=1, pady=20)

delete_btn = tk.Button(root, text="Delete",command=delete_file)
delete_btn.grid(row=4,column=0)

text_box = tk.Text(root, width=60,height=15)
text_box.grid(row=2,column=2)

view_btn = tk.Button(root, text="View", command=view_file)
view_btn.grid(row=3,column=2)

save_btn = tk.Button(root, text="Save", command=save_post)
save_btn.place(x=850,y=425)

# Run
load_files()

root.mainloop()