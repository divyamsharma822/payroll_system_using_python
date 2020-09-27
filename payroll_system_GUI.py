from tkinter import *
from tkinter.ttk import *

def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.create_widgets()
        self.master.title('Payroll System')
        self.master.iconbitmap('payroll.ico')
        self.master.config(bg='#A0A0A0')

    def show_info(self):
            name = self.name_text.get()
            eid = self.eid_text.get()
            # print(name,eid)

    def create_widgets(self):

        self.label_style = Style()
        self.label_style.configure("BW.TLabel", foreground="black", background="#A0A0A0")

        self.name_label = Label(self.master,text='Name',style='BW.TLabel')
        # self.addr_label = Label(self.master,text='Address',style='BW.TLabel')
        self.eid_label = Label(self.master,text='Employee ID',style='BW.TLabel')
        # self.pcode_label = Label(self.master,text='Pin Code',style='BW.TLabel')

        self.name=StringVar(self.master)
        self.eid=StringVar(self.master)

        self.name_text = Entry(self.master,width=25,font='Calibri',textvariable=self.name)
        self.eid_text = Entry(self.master,width=25,font='Calibri',textvariable=self.eid)
        # self.addr_text = Text(self.master,width=25,height=1,font='Calibri',highlightbackground='black',highlightthickness=1)
        # self.pcode_text = Text(self.master,width=25,height=1,font='Calibri',highlightbackground='black',highlightthickness=1)

        self.name_label.grid(row=0,column=0,padx=10,pady=(10,10),sticky='W')
        self.eid_label.grid(row=1,column=0,padx=10,pady=(0,10),sticky='W')
        # self.addr_label.grid(row=2,column=0,padx=10,pady=(0,10),sticky='W')
        # self.pcode_label.grid(row=3,column=0,padx=10,pady=(0,10),sticky='W')

        self.name_text.grid(row=0,column=1,padx=(0,10),pady=(10,10),sticky='W')
        self.eid_text.grid(row=1,column=1,padx=(0,10),pady=(0,10),sticky='W')
        # self.addr_text.grid(row=2,column=1,padx=(0,10),pady=(0,10),sticky='W')
        # self.pcode_text.grid(row=3,column=1,padx=(0,10),pady=(0,10),sticky='W')

        self.name_text.bind("<Tab>", focus_next_widget)
        self.eid_text.bind("<Tab>", focus_next_widget)
        # self.addr_text.bind("<Tab>", focus_next_widget)
        # self.pcode_text.bind("<Tab>", focus_next_widget)

        self.button_style = Style()
        self.button_style.map('D.TButton',
        foreground=[('pressed','#000000'),('active','#000000')],
        background=[('pressed','!disabled','black'),('active','#000000')]
        )

        self.submit = Button(self.master,width=10,text='Submit',style='D.TButton')

        self.submit.grid(row=2,column=1,sticky='E',padx=(0,10))

        self.submit['command'] = self.show_info

        self.submit.bind("<Tab>", focus_next_widget)
        self.submit.bind("<Return>",self.submit['command'])\

        self.submit = Button(self.master,width=10,text='Add New',style='D.TButton')

        self.submit.grid(row=2,column=0,sticky='W',padx=(10,0))

        self.submit.bind("<Tab>", focus_next_widget)
        self.submit.bind("<Return>")

              



root=Tk()
app = Application(master=root)
app.mainloop()
