# This file has been used for testing
import tkinter as tk
from tkinter import filedialog

def select_folder():
    folder_path = tk.filedialog.askdirectory()
    app.quit() 
    return folder_path

if __name__ == '__main__':
    app = tk.Tk()
    app.withdraw()
    
    folder_path = select_folder()
    if folder_path:
        print("Selected Folder:", folder_path)



