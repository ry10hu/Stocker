import tkinter as tk
import tkinter.ttk as ttk

def close_tab(event, notebook):
    current = notebook.select()
    notebooktext = notebook.tab(current, 'text')
    if current and notebooktext != "Main Menu":
        notebook.forget(current)

def bind_shortcuts(root, notebook):
    root.bind("<Control-w>", lambda event: close_tab(event, notebook))
