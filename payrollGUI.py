from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from data import search_row,add_row
class Application(Frame):

    
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWidgets()
        self.master.title('Payroll')
        self.master.iconbitmap('payroll.ico')
        self.master.maxsize(500,700)
        self.style = Style()
        self.style.configure('BW.TLabel',font=('Roboto',12))

    def set_male(self):
        self.new_gender.set('male')
    
    def set_female(self):
        self.new_gender.set('female')

    def add_data(self):
        name = self.add_name_entry.get()
        eid = int(self.add_eid_entry.get())
        gender = self.new_gender.get() 
        salary = int(self.add_salary_entry.get())
        new_row = [eid,name,gender,salary]
        print(eid,name,gender,salary)
        add_row(new_row)
        self.add_eid_entry.delete(0,'end')
        self.add_name_entry.delete(0,'end')
        self.add_salary_entry.delete(0,'end')
        self.add_eid_entry.delete(0,'end')

    def searchEmp(self):
        try:
            self.eid = int(self.eid_entry.get())
            self.name = self.name_entry.get()
            self.dat = search_row(self.eid)
        except ValueError:
            mb.showerror(title='Error!',message='Enter a Valid Employee Id')
        if(self.dat == None):
            mb.showerror(title='Not Found',message='Invalid Input')
            return
        elif(not self.dat):
            mb.showwarning(title='Not Found',message='The instance doesn\'t exist in csv.')
            return
        
        root = Tk()
        root.title('Search')
        root.iconbitmap('payroll.ico')

        #Employee ID Label widget
        self.eid_label = Label(root,text='Employee ID',font=('Calibri',12))
        self.eid_label.grid(row=0,column=0,padx=10,pady=(10,0),sticky='W')

        #Employee Name Label widget
        self.name_label = Label(root,text='Name',font=('Calibri',12))
        self.name_label.grid(row=1,column=0,padx=10,sticky='W')

        #Employee ID text widget
        self.eid_text = Text(root,height=1,width=20)
        self.eid_text.grid(row=0,column=1,padx=10,pady=(10,0),sticky='W')
        self.eid_text.configure(font='calibri 12')
        self.eid_text.insert(END,str(self.dat[0]))

        #Employee Name text Widget
        self.name_text = Text(root,height=1,width=20)
        self.name_text.grid(row=1,column=1,padx=10,sticky='W')
        self.name_text.configure(font='calibri 12')
        self.name_text.insert(END,str(self.dat[1]))

        #Employee Gender Label Widget
        self.gender_label = Label(root,text='Gender',font=('Calibri',12))
        self.gender_label.grid(row=2,column=0,padx=10,sticky='W')

        #Employee Salary Label Widget
        self.salary_label = Label(root,text='Salary',font=('Calibri',12))
        self.salary_label.grid(row=3,column=0,padx=10,sticky='W')

        #Employee Gender Text Widget
        self.gender_text = Text(root,height=1,width=20)
        self.gender_text.grid(row=2,column=1,padx=10,sticky='W')
        self.gender_text.configure(font='calibri 12')
        self.gender_text.insert(END,str(self.dat[2]))

        #Employee Salary Text Widget
        self.salary_text = Text(root,height=1,width=20)
        self.salary_text.grid(row=3,column=1,padx=10,sticky='W')
        self.salary_text.configure(font='calibri 12')
        self.salary_text.insert(END,str(self.dat[3]))

                

    def addEmp(self):
        root=Tk()
        root.title('Add New Employee')
        root.iconbitmap('payroll.ico')
        self.style = Style()
        self.style.configure('BW.TLabel',font=('Roboto',12))
        self.new_eid = StringVar()
        self.new_name = StringVar()
        self.new_salary = StringVar()
        self.new_gender = StringVar()

        #Employee ID Label Widget
        self.add_eid_label = Label(root,text='Employee ID',style='BW.TLabel')
        self.add_eid_label.grid(row=0,column=0,pady=10,padx=10,sticky='W')

        #Employee Name Lable Widget
        self.add_name_label = Label(root,text='Employee Name',style='BW.TLabel')
        self.add_name_label.grid(row=1,column=0,padx=10,pady=(0,10),sticky='W')

        #Employee Gender Label Widget
        self.add_gender_label = Label(root,text='Gender',style='BW.TLabel')
        self.add_gender_label.grid(row=2,column=0,padx=10,pady=(0,10),sticky='W')

        #Employee Salary Label Widget
        self.add_salary_label = Label(root,text='Salary',style='BW.TLabel')
        self.add_salary_label.grid(row=4,column=0,padx=10,pady=(0,10),sticky='W')

        #Employee ID entry Widget
        self.add_eid_entry = Entry(root,width=20,textvariable=self.new_eid)
        self.add_eid_entry.grid(row=0,column=1,sticky='W',pady=10,padx=(0,10),columnspan=2)

        #Employee Name Entry Widget
        self.add_name_entry = Entry(root,width=20,textvariable=self.new_name)
        self.add_name_entry.grid(row=1,column=1,sticky='W',padx=(0,10),pady=(0,10),columnspan=2)

        #Employee Gender Radio Widget
        self.add_gender_radio_m = Radiobutton(root,text='Male',value='male',variable=self.new_gender,command=self.set_male)
        self.add_gender_radio_m.grid(row=2,column=1,sticky='W',padx=(0,10),pady=(0,10))

        self.add_gender_radio_f = Radiobutton(root,text='Female',value='female',variable=self.new_gender,command=self.set_female)
        self.add_gender_radio_f.grid(row=2,column=2,sticky='W',padx=(0,10),pady=(0,10))
        
        #Employee Salary Entry Widget
        self.add_salary_entry = Entry(root,width=20,textvariable=self.new_salary)
        self.add_salary_entry.grid(row=4,column=1,sticky='W',padx=(0,10),pady=(0,10),columnspan=2)

        #ADD new button
        self.add_new_button = Button(root,text='Add to Database',command=self.add_data)
        self.add_new_button.grid(row=5,column=0,pady=(0,10),padx=10,columnspan=3,ipadx=5)
        
        
    def createWidgets(self):

        self.empId = StringVar()
        self.name = StringVar()

        #Employee ID Label widget
        self.eid_label = Label(self.master,text='Employee ID',font=('Calibri',12))
        self.eid_label.grid(row=0,column=0,padx=10,pady=(10,0),sticky='W')

        #Employee Name Label widget
        self.name_label = Label(self.master,text='Name',font=('Calibri',12))
        self.name_label.grid(row=1,column=0,padx=10,pady=(0),sticky='W') 

        #Employee ID Entry Widget
        self.eid_entry = Entry(self.master, width=20,textvariable=self.empId)
        self.eid_entry.grid(row=0,column=1,sticky='W',pady=(10,0),padx=(0,10))

        #Employee Name Entry Widget
        self.name_entry = Entry(self.master, width=20,textvariable=self.name)
        self.name_entry.grid(row=1,column=1,pady=(10,10),padx=(0,10),sticky='W')

        #Search Button
        self.search_button = Button(self.master,text='Search',width=18,command=self.searchEmp)
        self.search_button.grid(row=2,column=0,pady=(0,10),padx=10,columnspan=2)

        #Add new Employee Button
        self.add_button = Button(self.master,text='Add New Employee',command=self.addEmp)
        self.add_button.grid(row=3,column=0,pady=(0,10),padx=10,columnspan=2,ipadx=5)


root =Tk()
app = Application(master=root)
app.mainloop()