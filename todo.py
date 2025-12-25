import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import os
import json
from datetime import datetime


class ToDoApp:
    def __init__(self,master):
        self.master = master
        master.title ("To-Do-List")
        master.geometry ("500x700")
        master.resizable (False,False)
        master.configure (bg="#fadadd" )
        
        self.tasks = []
        self.tasks_file = os.path.join(os.path.dirname(__file__), "tasks.json")
        self.priority_var = tk.StringVar(value = "medium")
        
        #HEADER
        header_frame = tk.Frame(master, bg = "#e68fac", height = 60)
        header_frame.pack(fill="x", padx=0, pady=(0,0), side ="top")    #this is to make the header border on the top of master window
        
        title_label = tk.Label(
            header_frame,
            text = "To-Do List",
            font = ("Arial", 20, "bold"),
            bg = "#e68fac",
            fg = "#3d0c02"
        )
        title_label.pack(pady = 12)
        
        
        
        
   
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()