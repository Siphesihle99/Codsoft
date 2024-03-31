import tkinter as tk
from tkinter import*
import string
import random as r

class Password:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.config(bg ='gray20')
        self.root.geometry("650x450")
        choice = IntVar()

        def generate():
            lowercase_l = string.ascii_lowercase
            uppercase_l = string.ascii_uppercase
            numbers = string.digits
            symbols = string.punctuation

            combination = lowercase_l+uppercase_l+numbers+symbols
            password_len = int(self.Length_box.get())

            if choice.get()==1:
                self.Password_Entry.insert(END,r.sample(lowercase_l,password_len))

            if choice.get()==2:
                self.Password_Entry.insert(END,r.sample(lowercase_l+uppercase_l,password_len))
                
            if choice.get()==3:
                self.Password_Entry.insert(END,r.sample(combination,password_len))

        def delete():
            self.Password_Entry.delete(1.0, END)
                
        
        self.label_1 = Label(self.root, text = "PASSWORD GENERATOR", font ="ariel, 18 bold", width = 12, bd=5, bg = "black", fg= "white" )
        self.label_1.pack(side = "top",fill=BOTH)

        self.label_2 = Label(self.root, text = "Select password strength:", fg = "white", bg = "gray20", font = "ariel, 15 bold")
        self.label_2.pack(pady=5)

        self.Rbutton_1 = Radiobutton(self.root, text = "WEAK", value=1, variable=choice,fg = "black", bg = "white", font = "ariel, 13 bold")
        self.Rbutton_1.pack(pady=5)

        self.Rbutton_2 = Radiobutton(self.root, text = "MEDIUM", value=2, variable=choice,fg = "black", bg = "white", font = "ariel, 13 bold")
        self.Rbutton_2.pack(pady=5)

        self.Rbutton_3 = Radiobutton(self.root, text = "STRONG", value=3, variable=choice,fg = "black", bg = "white", font = "ariel, 13 bold")
        self.Rbutton_3.pack(pady=5)

        self.label_3 = Label(self.root, text = "Password length", fg = "white", bg = "gray20", font = "ariel, 15 bold")
        self.label_3.pack(pady=5)

        self.Length_box = Spinbox(self.root, from_=5,to_=10, width=5, font=12)
        self.Length_box.pack()

        
        

        self.Generate = Button(self.root, text = "Generate", font = "ariel, 15 bold", width = 10, bd = 5, bg = "gray2",fg = "white" , command=generate)
        self.Generate.pack(pady=8)

        self.Password_Entry = Text(self.root, height = 1, width =15, font= "ariel, 18 bold")
        self.Password_Entry.pack()

        self.Delete = Button(self.root, text = "Clear", font = "ariel, 15 bold", width = 10, bd = 5, bg = "gray2",fg = "white" , command=delete)
        self.Delete.pack(pady=5) 

           

def main():
    root = tk.Tk()
    u2 = Password(root)
    root.mainloop()

if __name__=="__main__":
    main()
