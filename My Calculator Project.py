from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title('My New Calculator') #sets the window title, geometry, background color, and size (non-resizable)
        master.geometry('390x460+0+0')
        master.config(bg='violet')
        master.resizable(False,False)

        self.equation = StringVar() #nitializes self.equation with a StringVar to display the input and result
        self.entry_value = ''
        Entry(width=25,bg='#ccddff',font=('Times New Roman',32),textvariable=self.equation).place(x=0,y=0)#The Entry widget displays the current input and result at the top

        Button(width=15,height=4,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=0,y=50)
        Button(width=15,height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90,y=50)
        Button(width=11,height=4,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=180,y=50)
        Button(width=11,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0,y=125)
        Button(width=11,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90,y=125)
        Button(width=11,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180,y=125)
        Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0,y=200)
        Button(width=11,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90,y=200)
        Button(width=11,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=180,y=200)
        Button(width=11,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0,y=275)
        Button(width=11,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=90,y=275)
        Button(width=11,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=180,y=275)
        Button(width=11,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90,y=350)
        Button(width=11,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180,y=350)
        Button(width=11,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270,y=275)
        Button(width=11,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270,y=200)
        Button(width=11,height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270,y=50)
        Button(width=11,height=4,text='*',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270,y=125)
        Button(width=11,height=4,text='=',relief='flat',bg='lightblue',command=self.solve).place(x=270,y=350)
        Button(width=11,height=4,text='C',relief='flat',bg='white',command=self.clear).place(x=0,y=350)
        
    def show(self, value): #Updates the displayed equation by appending the button's value
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
    
    def clear(self): #Resets the input
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self): #Evaluates the expression using eval() and displays the result
        result = eval(self.entry_value)
        self.equation.set(result)



root = Tk()
calculator = Calculator(root)
root.mainloop()
#The root = Tk() and root.mainloop() lines initialize and display the main window, starting the event loop that keeps the application running