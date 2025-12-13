import tkinter as tk
from main import gmail_login, load_filters

def run_app():
    service = gmail_login()
    filters = load_filters()

    root = tk.Tk()
    root.title("Inbox Cleaner(Gmail)")
    root.geometry("500x400")





    root.mainLoop()
run_app()