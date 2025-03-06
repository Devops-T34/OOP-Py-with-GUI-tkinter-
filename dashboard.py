import tkinter as tk 

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dashboard")
        self.root.attributes('-fullscreen', True)  # Make the window full screen
        self.show_dashboard()
        self.root.mainloop()

    def show_dashboard(self):
        tk.Label(self.root, text="Welcome to the Dashboard!", font=("Arial", 36), fg="black").pack(pady=50)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="#fdd835", fg="white").pack(pady=20)