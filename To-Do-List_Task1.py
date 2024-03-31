from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do-List")
        self.root.geometry("650x410+300+150")
        
        self.label_1 = Label(self.root, text = "To-Do-List-App", font ="ariel, 25 bold", width = 12, bd=5, bg = "blue", fg= "black" )
        self.label_1.pack(side = "top",fill=BOTH)
        
        self.label_2 = Label(self.root, text = "Add task", font = "ariel, 18 bold", width = 12, bd = 5, bg = "blue",fg = "black" )
        self.label_2.place(x=40,y=54)
        
        self.label_3 = Label(self.root, text = "My Tasks", font = "ariel, 18 bold", width = 12, bd = 5, bg = "blue",fg = "black" )
        self.label_3.place(x=320,y=54)
        
        self.tasks = Listbox(self.root, height =10, bd=5, width =20, font="ariel, 18 bold")
        self.tasks.place(x=320,y=100)
        
        self.text = Text(self.root, height = 1, width =15, font= "ariel, 18 bold")
        self.text.place(x=40, y= 120)

        scrollbar = Scrollbar(self.root, orient= "vertical")

        self.tasks.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tasks.yview)
        scrollbar.place(x=573.2, y=100, height=303)
        
        def add_task():
            data = self.text.get(1.0, "end")
            self.tasks.insert("end", data)
            file_dir = "tasks.txt"
            with open(file_dir, 'w') as file:
                file.write(data)
                file.seek(0)
                file.close()
            self.text.delete(1.0, "end")
            
        def del_task():
            select_ln = self.tasks.curselection()
            search = self.tasks.get(select_ln)
            file_dir = "tasks.txt"
            with open(file_dir, 'r+') as file:
                 new_tk = file.readlines()
                 file.seek(0)
                 for line in new_tk:
                     item = str(search)
                     if item not in line:
                         file.write(line)
                 file.truncate()
            self.tasks.delete(select_ln)
            
        with open("tasks.txt", 'r') as file:
            lines_ = file.readlines()
            for i in lines_:
                read = i.split()
                self.tasks.insert(END, read)
            file.close()

    
            
        self.button = Button(self.root, text = "Save", font = "ariel, 18 bold", width = 10, bd = 5, bg = "blue",fg = "black" , command=add_task)
        self.button.place(x=40,y=180)
        
        self.button_2 = Button(self.root, text = "Delete", font = "ariel, 18 bold", width = 10, bd = 5, bg = "blue",fg = "black" , command=del_task)
        self.button_2.place(x=40,y=250)
            
                       
    
def main():
    root = Tk()
    u1 =todo(root)
    root.mainloop()
    
if __name__=="__main__":
    main()

