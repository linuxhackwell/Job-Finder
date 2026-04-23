import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import webbrowser

url = "https://remotive.com/api/remote-jobs"
SEARCH_DELAY_MS = 500

after_id = None

def fetch_jobs():
    global url
    query = search_input.get().strip().lower()
    tree.delete(*tree.get_children())
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        jobs = data["jobs"]
        for job in jobs:
            job_title = job["title"].lower()
            if query in job_title:
                tree.insert("", tk.END, values=(job["title"], job["company_name"], job['url']))
    else:
        messagebox.showerror(f"{response.status_code}")

def schedule_search(event=None):
    global after_id
    
    if after_id is not None:
        root.after_cancel(after_id)
    
    after_id = root.after(SEARCH_DELAY_MS, fetch_jobs)

def clear_search(event=None):
    search_input.delete(0, tk.END)
    for item in tree.get_children():
        tree.delete(item)
    status_label.config(text="Ready - enter a search term above")
    search_input.focus()


def open_job_link(event)    :
    selected_url = tree.selection()
    if not selected_url:
        return
    
    value = tree.item(selected_url, 'values')
    link = value[2]
    webbrowser.open(link)


root = tk.Tk()
root.title("Job Finder")
root.geometry("850x500")
root.minsize(600, 400)

root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

title_label = tk.Label(root, text="Job Finder", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))

search_label = tk.Label(root, text="Search:")
search_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

search_input = tk.Entry(root, font=("Arial", 11))
search_input.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="ew")

clear_button = tk.Button(root, text="Clear", command=clear_search)
clear_button.grid(row=1, column=2, padx=(0, 10), pady=10, sticky="w")

status_label = tk.Label(root, text="Type to search for jobs", font=("Arial", 9), fg="gray")
status_label.grid(row=2, column=0, columnspan=3, padx=10, pady=(0, 5), sticky="w")

tree_frame = tk.Frame(root)
tree_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)
tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)

tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.grid(row=0, column=1, sticky="ns")

tree = ttk.Treeview(
    tree_frame, 
    columns=('Job Title', 'Company', 'Link'), 
    show='headings', 
    height=12,
    yscrollcommand=tree_scroll.set
)

tree.heading('Job Title', text='Job Title')
tree.heading('Company', text='Company')
tree.heading('Link', text='Link')

tree.column('Job Title', width=300)
tree.column('Company', width=200)
tree.column('Link', width=250)

tree.grid(row=0, column=0, sticky="nsew")
tree_scroll.config(command=tree.yview)

search_input.bind("<KeyRelease>", schedule_search)
tree.bind("<Double-1>", open_job_link)

root.mainloop()