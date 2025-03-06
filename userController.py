import tkinter as tk  
from tkinter import messagebox 
import dashboard 

class UserController:
    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.userdata = {"name": '', "age": '', "email": '', "password": ''}  # Moved userdata here

    def start_gui(self):
        self.root = tk.Tk()
        self.root.title("hello to first py oop project")
        self.show_main_menu()
        self.root.mainloop()

    def show_main_menu(self):
        self.clear_window()
        self.root.geometry("500x500")  # Set window size to 500x500
        self.root.configure(bg="#f0f0f0")  # Set background color
        tk.Label(self.root, text="Welcome to User Controller").pack(pady=20)
        tk.Button(self.root, text="Register", command=self.show_registration,width=30 , bg="#228df2", fg="white").pack(pady=2)
        tk.Button(self.root, text="Login", command=self.show_login,width=30 , bg="#228df2", fg="white").pack(pady=2)
        tk.Button(self.root, text="Exit", command=self.root.quit,width=30 , bg="#fdd835", fg="white").pack(pady=2)

    def show_registration(self):
        self.clear_window()
        self.root.geometry("500x500")  # Set window size to 500x500
        self.root.configure(bg="#f0f0f0")  # Set background color

        tk.Label(self.root, text="Register", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)

        name_frame = tk.Frame(self.root, bg="#f0f0f0")
        name_frame.pack(pady=5, padx=20, fill='x')
        tk.Label(name_frame, text="Name", bg="#f0f0f0", font=("Arial", 12)).pack(anchor='w')  # Align left
        self.name_entry = tk.Entry(name_frame, width=100, font=("Arial", 12),  bd=2, relief="groove")
        self.name_entry.pack(pady=5,anchor='w')

        age_frame = tk.Frame(self.root, bg="#f0f0f0")
        age_frame.pack(pady=5, padx=20, fill='x')
        tk.Label(age_frame, text="Age", bg="#f0f0f0", font=("Arial", 12)).pack(anchor='w')  # Align left
        self.age_entry = tk.Entry(age_frame, width=100, font=("Arial", 12), bd=2, relief="groove")
        self.age_entry.pack(pady=5,anchor='w')

        email_frame = tk.Frame(self.root, bg="#f0f0f0")
        email_frame.pack(pady=5, padx=20, fill='x')
        tk.Label(email_frame, text="Email", bg="#f0f0f0", font=("Arial", 12)).pack(anchor='w')  # Align left
        self.email_entry = tk.Entry(email_frame, width=100, font=("Arial", 12), bd=2, relief="groove")
        self.email_entry.pack(pady=5,anchor='w')

        password_frame = tk.Frame(self.root, bg="#f0f0f0")
        password_frame.pack(pady=5, padx=20, fill='x')
        tk.Label(password_frame, text="Password", bg="#f0f0f0", font=("Arial", 12)).pack(anchor='w')  # Align left
        self.password_entry = tk.Entry(password_frame, width=100, font=("Arial", 12), bd=2, relief="groove")
        self.password_entry.pack(pady=5,anchor='w')

        tk.Button(self.root, text="Submit", command=self.register, bg="#4CAF50", fg="white").pack(pady=20)
    
    def show_login(self):
        self.clear_window()
        self.root.geometry("500x500")  # Set window size to 500x500
        self.root.configure(bg="#f0f0f0")  # Set background color

        tk.Label(self.root, text="Login", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)

        # Create a frame for the email input
        email_frame = tk.Frame(self.root, bg="#f0f0f0")
        email_frame.pack(pady=5, padx=20, fill='x')
        tk.Label(email_frame, text="Email", bg="#f0f0f0", font=("Arial", 12)).pack(anchor='w')  # Align left
        self.email_entry = tk.Entry(email_frame, width=100, bd=2, font=("Arial", 12), relief="groove")
        self.email_entry.pack(pady=5,anchor='w')

        # Create a frame for the password input
        password_frame = tk.Frame(self.root, bg="#f0f0f0")
        password_frame.pack(pady=5, padx=20, fill='x')
        tk.Label(password_frame, text="Password", bg="#f0f0f0", font=("Arial", 12)).pack(anchor='w')  # Align left
        self.password_entry = tk.Entry(password_frame, show='*', font=("Arial", 12), width=100, bd=2, relief="groove")
        self.password_entry.pack(pady=5,anchor='w')

        tk.Button(self.root, text="Login", command=self.login, bg="#4CAF50", fg="white").pack(pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register(self):
        print(self.name_entry.get())
        print(self.age_entry.get())
        print(self.email_entry.get())
        print(self.password_entry.get())
        
        if (self.name_entry.get().isalpha() and self.age_entry.get().isnumeric() and "@" in self.email_entry.get() and len(self.password_entry.get()) >= 8):

            self.userdata['name'] = self.name_entry.get()
            self.userdata['age'] = self.age_entry.get()
            self.userdata['email'] = self.email_entry.get()
            self.userdata['password'] = self.password_entry.get()
            messagebox.showinfo("Registration", f"User {self.userdata['name']} registered successfully.")
            self.show_main_menu()

        elif not self.name_entry.get().isalpha():
            messagebox.showinfo("Error", "The name is required and must contain only letters.")
        elif not self.age_entry.get().isnumeric():
            messagebox.showinfo("Error", "Age must be a number.")
        elif "@" not in self.email_entry.get():
            messagebox.showinfo("Error", "That is not a valid email '@'.")
        elif len(self.password_entry.get()) < 8:
            messagebox.showinfo("Error", "Password must be at least 8 characters long.")



    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if self.Login(email, password):
            messagebox.showinfo("Login", "Login successful! Redirecting to dashboard...")
            dashboard.Dashboard()  # Call the Dashboard class
        else:
            messagebox.showerror("Login", "The email or password is incorrect. Please try again.")

    def Login(self, email, password):
        if email == self.userdata['email'] and password == self.userdata['password']:
            return True
        else:
            return False

# Start the program
if __name__ == "__main__":
    UserController('', '', '', '').start_gui()
