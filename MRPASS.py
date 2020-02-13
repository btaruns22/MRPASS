import tkinter



# m = tkinter.Tk("800x500")
#
# m.mainloop()

window = tkinter.Tk()

window.geometry("800x500")
ProgName = tkinter.Label(window, font=('MR.PASS', 30, 'bold'), text="PassManager", fg="blue")
ProgName.grid(row=1, column=5, padx=330, pady=200)

window.mainloop()
