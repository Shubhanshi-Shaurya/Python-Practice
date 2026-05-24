import tkinter as tk

root=tk.Tk()
root.title("simple calculator")
root.geometry("400x400")
root.resizable(False,False)

entry=tk.Entry(root)
entry.pack(fill="both" ,ipadx=8,ipady=15,padx=10,pady=10)

def button_click(value):
    entry.insert(tk.END,value)

def clear():
    entry.delete(0,tk.END)

def calculate():
    try:
        result=eval(entry.get())
        clear()
        entry.insert(0,result)
    except:
        clear()
        entry.insert(0,"error")

frame=tk.Frame(root)
frame.pack()

buttons=[
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for row in buttons:
    button_row=tk.Frame(frame)
    button_row.pack(expand=True,fill="both")
    for btn in row:
        action=calculate if btn=='=' else lambda x=btn: button_click(x)
        tk.Button(
            button_row,
            text=btn,
            font=("Arial",16),
            command=action,
            height=2,
            width=5
        ).pack(side="left",expand=True,fill="both")

tk.Button(root,text="clear",command=clear,font=("Arial",16)).pack(fill="both",padx=10,pady=10)

root.mainloop()