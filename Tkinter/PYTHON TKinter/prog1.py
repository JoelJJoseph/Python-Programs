import tkinter as tk
window=tk.Tk()
msg=tk.Label(text="Hello Christite")
msg.pack()
#window.mainloop()#control the events

label1=tk.Label(text="Hello,Christite",foreground="purple",background="Orange")
label2=tk.Label(text="Hello,MCA",fg="red",bg="white")
label3=tk.Label(text="Gateways is here!!",fg="Orange",bg="purple")
label1.pack()
label2.pack()
label3.pack()
#window.mainloop()

button1=tk.Button(text="Login",width=25,height=8,bg="red",fg="yellow")
button1.pack()


