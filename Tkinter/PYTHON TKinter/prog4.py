import tkinter as tk
window=tk.Tk()
CheckIn1=tk.IntVar()
CheckIn2=tk.IntVar()
CheckIn3=tk.IntVar()
CheckIn4=tk.IntVar()
CheckIn5=tk.IntVar()
lbl1=tk.Label(window,text="Selcet the details you would like to share")
c1=tk.Checkbutton(window,text="Instituion",variable=CheckIn1,
                  onvalue=1,offvalue=0,height=3,width=20)
c2=tk.Checkbutton(window,text="City",variable=CheckIn2,
                  onvalue=1,offvalue=0,height=3,width=20)
c3=tk.Checkbutton(window,text="Course",variable=CheckIn3,
                  onvalue=1,offvalue=0,height=3,width=20)
c4=tk.Checkbutton(window,text="Mobile Number",variable=CheckIn4,
                  onvalue=1,offvalue=0,height=3,width=20)
c5=tk.Checkbutton(window,text="Email ID",variable=CheckIn5,
                  onvalue=1,offvalue=0,height=3,width=20)
lbl1.pack()
c1.pack()
c2.pack()
c3.pack()
c4.pack()
c5.pack()

window.mainloop()
