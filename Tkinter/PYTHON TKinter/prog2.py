import tkinter as tk
window=tk.Tk()
label1=tk.Label(window,text="Institution").grid(row=0)
label2=tk.Label(window,text="Course").grid(row=1)
label3=tk.Label(window,text="Event").grid(row=2)


i1=tk.Entry(window)
i2=tk.Entry(window)
i3=tk.Entry(window)
i1.grid(row=0,column=10)
i2.grid(row=1,column=10)
i3.grid(row=2,column=10)
window.mainloop()
