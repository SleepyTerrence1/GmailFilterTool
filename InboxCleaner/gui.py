import tkinter as tk
from main import gmail_login, load_filters

def run_app():
    root = tk.Tk()
    root.title("Inbox Cleaner GUI")
    root.geometry("500x400")

    tk.Label(root, text="Inbox Cleaner").pack()

    filters = load_filters()
    tk.Label(root, text="Loaded Filters:").pack()

    tk.Button(root, text="Apply Filters", command=lambda: print("Applying filters...") )


    root.mainloop()
if __name__ == '__main__':
    run_app()