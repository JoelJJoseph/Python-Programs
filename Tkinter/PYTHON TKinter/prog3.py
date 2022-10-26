import tkinter as tk
window=tk.Tk()
label1=tk.Label(window,text="Enter Your Name")
label1.pack()
def msg():
    text=entry1.get()
    print(text)
entry1=tk.Entry(window,width=25)
entry1.pack()
bt1=tk.Button(window,text="Button",command=msg)
bt1.pack()
window.mainloop()
