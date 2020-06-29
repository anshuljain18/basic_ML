import tkinter as tk
import pickle

with open('mileage_data.pkl', 'rb') as fp:
    model = pickle.load(fp)
    fp.close()

root = tk.Tk()

hp = tk.DoubleVar()
disp = tk.DoubleVar()
weight = tk.DoubleVar()
font = ('monospace',25,'italic')

def clear():
    hp.set('')
    disp.set('')
    weight.set('')
clear()


f1 = tk.Frame(root)
l1 = tk.Label(f1, text='HorsePower : ')
l1.config(bg='white', fg='#123456', font=font)
l1.pack(side=tk.LEFT, expand=tk.YES)

e1 = tk.Entry(f1, textvariable=hp)
e1.config(bg='white', fg='#123456', font=font)
e1.pack(fill=tk.X, expand=tk.YES)
f1.pack(fill=tk.BOTH, expand=tk.YES)

f2 = tk.Frame(root)
l2 = tk.Label(f2, text='Displacement : ')
l2.config(bg='white', fg='#123456', font=font)
l2.pack(side=tk.LEFT, expand=tk.YES)

e2 = tk.Entry(f2, textvariable=disp)
e2.config(bg='white', fg='#123456', font=font)
e2.pack(fill=tk.X, expand=tk.YES)
f2.pack(fill=tk.BOTH, expand=tk.YES)

f3 = tk.Frame(root)
l3 = tk.Label(f3, text='Weight : ')
l3.config(bg='white', fg='#123456', font=font)
l3.pack(side=tk.LEFT, expand=tk.YES)

e3 = tk.Entry(f3, textvariable=weight)
e3.config(bg='white', fg='#123456', font=font)
e3.pack(fill=tk.X, expand=tk.YES)
f3.pack(fill=tk.BOTH, expand=tk.YES)

pred = tk.Button(root, text='Predict Mileage', command=lambda :predict())
pred.config(bg='white', fg='#123456', font=font)
pred.pack(fill=tk.X, expand=tk.YES)

exitb = tk.Button(root, text='Exit', command=lambda :root.quit())
exitb.config(fg='white', bg='#123456', font=font)
exitb.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.YES)

def predict():
    h = hp.get()
    dis = disp.get()
    w = weight.get()
    
    mpg = model.predict([ [h, dis, w] ])[0]
    clear()
    top = tk.Toplevel(root)
    top.grab_set()
    text = f'''
        HorsePower   : {h}
        Displacement : {dis}
        Weight       : {w}
        Mileage      : {mpg}
    '''
    msg = tk.Message(top, text=text)
    msg.config(font=('monospace', 25, 'bold'))
    msg.pack(fill=tk.BOTH, expand=tk.YES)
    eb = tk.Button(top, text='Exit', command=lambda : top.destroy())
    eb.config(fg='white', bg='red', font=('monospace', 25, 'bold'))
    eb.pack(fill=tk.X, expand=tk.YES)
    e1.focus()

root.title('Mileage Predict')
root.mainloop()