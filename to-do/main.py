import tkinter
from tkinter import END
 
Arjun=tkinter.Tk()

Arjun.title("To Do App")
Arjun.geometry("350x450")
Arjun.resizable(0,0)
Arjun_color="#737CA1"

Arjun.config(bg=Arjun_color)
Arjun_font=("Ariel",28,"bold")
bcolor="#007C80"
bfont=("Times New Roman",12)


def add_task():
    task=add_entry.get()
    show_box.insert(END,task)
    add_entry.delete(0,END)

def remove_task():
    first=show_box.curselection()
    show_box.delete(first)

def clr_task():
    show_box.delete(0,END)

def save_task():
    second=show_box.get(0,END)
    with open("task.txt","w") as f:
        for tasks in second:
            f.write(tasks+"\n")

def todo():
    try:
      with open("task.txt","r") as f:
           third=f.readlines()
           for tasks in third:
               show_box.insert(END,tasks)
    except FileNotFoundError:
        pass
    

def quit():
    Arjun.destroy()



frame_title=tkinter.Frame(Arjun,bg=Arjun_color)
label_title=tkinter.Label(frame_title, text="MY TO-DO LIST",bg=Arjun_color,font=Arjun_font)

frame_input=tkinter.Frame(Arjun,bg=Arjun_color)
add_entry=tkinter.Entry(frame_input,width=25,font=bfont)
B1=tkinter.Button(frame_input,text="Add Task",command=add_task,bg=bcolor,font=bfont)

frame_output=tkinter.Frame(Arjun)
srlbar=tkinter.Scrollbar(frame_output)
show_box=tkinter.Listbox(frame_output,width=48,height=15)

frame_management=tkinter.Frame(Arjun,bg=Arjun_color)
B2=tkinter.Button(frame_management,text="Remove",font=bfont,bg=bcolor,command=remove_task)
B3=tkinter.Button(frame_management,text="Clear",font=bfont,bg=bcolor,command=clr_task)
B4=tkinter.Button(frame_management,text="Save",font=bfont,bg=bcolor,command=save_task)
B5=tkinter.Button(frame_management,text="Quit",font=bfont,bg=bcolor,command=quit)



label_title.grid(row=0,column=1)
add_entry.grid(row=0,column=0,padx=5)
B1.grid(row=0,column=1,padx=5,ipadx=10)
show_box.grid(row=0,column=0)
srlbar.grid(row=0,column=1,sticky="NS")
B2.grid(row=0,column=0,padx=7,ipadx=7)
B3.grid(row=0,column=1,padx=8,ipadx=6)
B4.grid(row=0,column=2,padx=10,ipadx=5)
B5.grid(row=0,column=3,padx=12,ipadx=5)


show_box.config(yscrollcommand=srlbar.set)
srlbar.config(command=show_box.yview)


frame_title.pack(padx=10,pady=10)
frame_input.pack(padx=10,pady=10)
frame_output.pack(padx=10,pady=10)
frame_management.pack(padx=10,pady=10)

todo()
Arjun.mainloop()