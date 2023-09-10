import tkinter as tk 

cal=""

def add_to_cal(symbol):
    global cal
    cal += str(symbol)
    t_rlt.delete(1.0,"end")
    t_rlt.insert(1.0, cal)


def evale_calculation():
    global cal
    try:
        cal = str(eval(cal))
        t_rlt.delete(1.0,"end")
        t_rlt.insert(1.0,  cal)
  
    except:
        clr_field()
        t_rlt.insert(1.0,"Error")
            

def clr_field():
    global cal
    cal=""
    t_rlt.delete(1.0,"end")
    


A= tk.Tk()
A.geometry("590x525")
A.resizable(0,0)
A.title("Basic Calculator")

t_rlt = tk.Text(A, height=4, width=32 ,font=("Arial",24,"bold"),fg="white",bg="grey",border=5)
b_1 =tk.Button(A, text="1",command=lambda: add_to_cal(1),width=5,font=("Arial",28),fg="black",bg="#00AAFF")
b_2 =tk.Button(A, text="2",command=lambda: add_to_cal(2),width=5,font=("Arial",28),fg="black",bg="#00AAFF")
b_3 =tk.Button(A, text="3",command=lambda: add_to_cal(3),width=5,font=("Arial",28),fg="black",bg="#00AAFF")
b_4 =tk.Button(A, text="4",command=lambda: add_to_cal(4),width=5,font=("Arial",28),fg="black",bg="#007AFF")
b_5 =tk.Button(A, text="5",command=lambda: add_to_cal(5),width=5,font=("Arial",28),fg="black",bg="#007AFF")
b_6 =tk.Button(A, text="6",command=lambda: add_to_cal(6),width=5,font=("Arial",28),fg="black",bg="#007AFF")
b_7 =tk.Button(A, text="7",command=lambda: add_to_cal(7),width=5,font=("Arial",28),fg="black",bg="#0019FF")
b_8 =tk.Button(A, text="8",command=lambda: add_to_cal(8),width=5,font=("Arial",28),fg="black",bg="#0019FF")
b_9 =tk.Button(A, text="9",command=lambda: add_to_cal(9),width=5,font=("Arial",28),fg="black",bg="#0019FF")
b_0 =tk.Button(A, text="0",command=lambda: add_to_cal(0),width=5,font=("Arial",28),fg="black",bg="#00F3FF")




t_rlt.grid(columnspan=10)
b_1.grid(row=5,column=0,columnspan=2)
b_2.grid(row=5,column=2,columnspan=2)
b_3.grid(row=5,column=4,columnspan=2)
b_4.grid(row=4,column=0,columnspan=2)
b_5.grid(row=4,column=2,columnspan=2)
b_6.grid(row=4,column=4,columnspan=2)
b_7.grid(row=3,column=0,columnspan=2)
b_8.grid(row=3,column=2,columnspan=2)
b_9.grid(row=3,column=4,columnspan=2)
b_0.grid(row=6,column=2,columnspan=2)


 

## declaring arithmetic operation like (addition,subtraction,multiplication,division,parentheses,clear) 
b_11 =tk.Button(A, text="(",command=lambda: add_to_cal("("),width=5,font=("Arial",28),fg="black",bg="#00F3FF")
b_12 =tk.Button(A, text=")",command=lambda: add_to_cal(")"),width=5,font=("Arial",28),fg="black",bg="#00F3FF")
b_13=tk.Button(A, text="+",command=lambda: add_to_cal("+"),width=10,font=("Arial",28),fg="black",bg="#A300A3")
b_14 =tk.Button(A, text="-",command=lambda: add_to_cal("-"),width=10,font=("Arial",28),fg="black",bg="#A300A3")
b_15 =tk.Button(A, text="*",command=lambda: add_to_cal("*"),width=10,font=("Arial",28),fg="black",bg="#A300A3")
b_16 =tk.Button(A, text="/",command=lambda: add_to_cal("/"),width=10,font=("Arial",28),fg="black",bg="#A300A3")
b_17 =tk.Button(A, text="AC",command=lambda: clr_field(),fg="white",bg="red",width=10,font=("Arial",28))
b_18 =tk.Button(A, text="=",fg="black",bg="orange",command= evale_calculation ,width=10,font=("Arial",28,'bold'))
b_19=tk.Button(A, text="%" ,command=lambda:add_to_cal("%"),width=5,font=("Arial",28),fg="black",bg="#A300A3")


b_11.grid(row=6,column=0,columnspan=2)
b_12.grid(row=6,column=4,columnspan=2)
b_13.grid(row=3,column=6,columnspan=2)
b_14.grid(row=4,column=6,columnspan=2)
b_15.grid(row=5,column=6,columnspan=2)
b_16.grid(row=6,column=6,columnspan=2)
b_17.grid(row=2,column=4,columnspan=3)
b_18.grid(row=2,column=0,columnspan=4)
b_19.grid(row=2,column=7,columnspan=3)


A.mainloop()


