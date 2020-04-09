import tkinter as tk
import MCSim

def run_sim():
    MCSim.init(int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()))


master = tk.Tk()
tk.Label(master, text="Population Size",width=20,anchor='w').grid(row=0)
tk.Label(master, text="R naught",width=20,anchor='w').grid(row=1)
tk.Label(master, text="Speed", width=20,anchor='w').grid(row=2)

tk.Label(master,text="Social Distance Effect",width=20,anchor='w').grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.insert(10, 100)
e2.insert(10,10)
e3.insert(10, 2)
e4.insert(10,10)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=2, sticky=tk.W, pady=10,padx = 0)

tk.Button(master, text='Run Simulation', command=run_sim).grid(row=5, column=0, sticky=tk.W, pady=4)

master.mainloop()

tk.mainloop()