from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as sq_connector 
import password 

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Library Management System")
        self.window.geometry("830x550")
        self.window.config(bg = "white")
        self.window.iconbitmap("arc.ico.ico")
        self.window.resizable(False, False)
        self.user_password = password.password
        
        #Creating customizing objects......... 
        self.color_1 = "cyan"
        self.color_2 = "gray95"
        self.color_3 = "black"
        self.color_4 = "white"
        self.font_1 = "times new roman"
        self.font_2 = "helvetica"
        self.columns = ('Books Name', 'Books Field', 'Quantity')
        self.columns1 = ('FirstName', 'LastName', 'AdmissionNumber', 'RollNo', 'BookName', "BookField", 'PhoneNumber', "Quantity")
        
        #Creating connecting objects........... 
        self.host = "localhost"
        self.user = "root"
        self.password = "tahil"
        self.database = "Library_books1"
        self.database1 = "Library_user_data1"
        
        # Creating Left Frame..........
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight = 1)

        # Creating Right Frame................
        self.frame_2 = Frame(self.window, bg = self.color_2)
        self.frame_2.place(x=540,y=0,relwidth=1, relheight=1)

        # Creating Buttons.................
        self.add_bt = Button(self.frame_2, text='Display books', font=(self.font_1, 12), bd=2, command=self.display_books, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=80,y=50,width=130, height=40)
        
        self.view_bt = Button(self.frame_2, text='Issue Books', font=(self.font_1, 12), bd=2, command=self.book_issue_func, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=80,y=120,width=130, height=40)
        
        self.update_bt = Button(self.frame_2, text='Return Books', font=(self.font_1, 12), bd=2, command=self.book_return_func, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=80,y=190,width=130, height=40)
        
        self.delete_bt = Button(self.frame_2, text='Update Books', font=(self.font_1, 12), bd=2, command=self.update_books,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=80,y=260,width=130, height=40)
        
        self.clear_bt = Button(self.frame_2, text='Delete Books', font=(self.font_1, 12), bd=2, command=self.delete_books, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=80,y=330,width=130, height=40)

        self.exit_bt1 = Button(self.frame_2, text='Show Records', font=(self.font_1, 12), bd=2, cursor="hand2", command=self.show_records, bg=self.color_2,fg=self.color_3).place(x=80,y=400,width=130, height=40)
        
        self.exit_bt2 = Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2, command=self.Exit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=80,y=470,width=130, height=40)
    
    def database_books_cretion(self):
        #Creating table for books data........... 
        self.DB_NAME = 'Library_books1'

        self.TABLES = {}
        self.TABLES['library_books_data'] = (
            "CREATE TABLE `library_books_data` ("
            "  `BooksName` varchar(200) NOT NULL,"
            "  `BooksField` varchar(200) NOT NULL,"
            "  `Quantity` int(250) NOT NULL,"
            "PRIMARY KEY (`BooksName`)"
            ") ENGINE=InnoDB")
        
        #Creating data for insertion......... 
        # self.library_books_data_insert = ('INSERT INTO library_books_data VALUES (%s, %s, %s)')
        
        #use this if the database is not created in the system................ 
        self.database_connection = sq_connector.connect(host=self.host, user=self.user, passwd=self.password)
        
        #use this if the database is created in the system...........  
        self.database_connection = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
        
        #Creating Cursor................ 
        self.cursor1 = self.database_connection.cursor()
        
        # self.library_books_data_insert_data = ('Concepts of Physics HC Verma', 'Physics', 20)
        
        # self.cursor1.execute(self.library_books_data_insert, self.library_books_data_insert_data)
        
        try: 
            self.cursor1.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
            self.cursor1.execute("USE {}".format(self.DB_NAME))
            
            for table_name in self.TABLES:
                table_description = self.TABLES[table_name]
    
                print("Creating table {}: ".format(table_name), end='')
                self.cursor1.execute(table_description)
            pass
        
        except Exception as e:
            print(e)
            self.database_connection.database = self.DB_NAME
            
        self.database_connection.commit()
        self.database_connection.close()
        
    def database_user_creation(self):
        #Creating table for user data........ 
        self.DB_NAME1 = 'Library_user_data1'

        self.TABLES1 = {}
        self.TABLES1['library_userdata'] = (
            "CREATE TABLE `library_userdata` ("
            "  `First_Name` varchar(100) NOT NULL,"
            "  `Last_Name` varchar(100) NOT NULL,"
            "  `Admission_Number` int(100) NOT NULL,"
            "  `Roll_Number` int(100) NOT NULL,"
            "  `Book_Name` varchar(200) NOT NULL,"
            "  `Book_Field` varchar(200) NOT NULL,"
            "  `Phone_Number` int(150) NOT NULL,"
            "  `Quantity` int(250) NOT NULL,"
            "PRIMARY KEY (`Admission_Number`)"
            ") ENGINE=InnoDB")
        
        #Creating data for insertion........... 
        # self.library_user_data = ("INSERT INTO library_userdata VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        
        #Creating connection........... 
        #use this if the database is created in the system...........  
        self.database_connection1 = sq_connector.connect(host=self.host, user=self.user, passwd=self.password)
        
        #use this if the database is not created in the system...........  
        self.database_connection1 = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database1)
        
        #creating cursor.........
        self.cursor2 = self.database_connection1.cursor()
        
        # self.cursor2.execute(self.library_user_data, self.library_user_data_data)
        
        try:
            self.cursor2.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME1))
            self.cursor2.execute("USE {}".format(self.DB_NAME1))
            
            ##For loop to insert data into the tables.............. 
            for table_name1 in self.TABLES1:
                table_description1 = self.TABLES1[table_name1]
    
                print("Creating table {}: ".format(table_name1), end='')
                self.cursor2.execute(table_description1)
            
        except Exception as e:
            print(e) 
            self.database_connection1.database = self.DB_NAME1 
            
        self.database_connection1.commit()
        self.database_connection1.close()
            
    def display_books(self):
        self.ClearScreen()
        
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=self.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        scroll_x.pack(side=BOTTOM, fill=X)

        # Setting tables data...........
        self.tree.heading('Books Name', text='Books Name', anchor=W)
        self.tree.heading('Books Field', text='Books Field', anchor=W)
        self.tree.heading('Quantity', text='Quantity', anchor=W)
        self.tree.pack()
        self.tree.bind('<Double-Button-1>')
        
        try: 
            self.connection = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
            
            self.connection_cursor = self.connection.cursor()
            
            self.connection_cursor.execute("select * from library_books_data")
            
            self.data1 = self.connection_cursor.fetchall()
            
            for i in range(len(self.data1)):
                self.tree.insert("", 'end', text=(i), values=(self.data1[i]))
            
            if self.connection.is_connected():
                print("Successfully Connected to MySQL Database")
                messagebox.showinfo("Connection Successfull", "Successfully Connected to MySQL Database", parent=self.window)
        
        except Exception  as e: 
            print(e)
            
            
    def show_records(self):
        self.ClearScreen()
        
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree1 = ttk.Treeview(self.frame_1, columns=self.columns1, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree1.yview)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree1.xview)
        scroll_x.pack(side=BOTTOM, fill=X)

        # Setting tables data...........
        self.tree1.heading('FirstName', text='First Name', anchor=W)
        self.tree1.heading('LastName', text='Last Name', anchor=W)
        self.tree1.heading('AdmissionNumber', text='Admission Number', anchor=W)
        self.tree1.heading('RollNo', text='Roll No', anchor=W)
        self.tree1.heading('BookName', text='Book Name', anchor=W)
        self.tree1.heading('BookField', text='Book Field', anchor=W)
        self.tree1.heading('PhoneNumber', text='Phone Number', anchor=W)
        self.tree1.heading('Quantity', text='Quantity', anchor=W)
        self.tree1.pack()
        self.tree1.bind('<Double-Button-1>')
        
        try: 
            self.connection1 = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database1)
            
            self.connection1_cursor = self.connection1.cursor()
            
            self.connection1_cursor.execute("select * from library_userdata") 
            
            self.data0 = self.connection1_cursor.fetchall()
            for i in range(len(self.data0)):
                self.tree1.insert("", 'end', text=(i), values=(self.data0[i]))
            
            if self.connection1.is_connected():
                print("Successfully Connected to MySQL Database")
                messagebox.showinfo("Connection Successfull", "Successfully Connected to MySQL Database", parent=self.window)
        
        except Exception  as e: 
            print(e)
            
    
    def book_issue_func(self):
        self.ClearScreen()
        
        self.first_name1 = Label(self.frame_1, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.first_name_entry1 = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.first_name_entry1.place(x=40,y=60, width=200)

        self.last_name1 = Label(self.frame_1, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.last_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.last_name_entry.place(x=300,y=60, width=200)

        self.admission_number = Label(self.frame_1, text="Admission Number", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.admission_number_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.admission_number_entry.place(x=40,y=130, width=200)

        self.roll_no = Label(self.frame_1, text="Roll No", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.roll_no_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.roll_no_entry.place(x=300,y=130, width=200)

        self.books_name = Label(self.frame_1, text="Book Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.books_name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.books_name_entry.place(x=40,y=200, width=200)

        self.books_field = Label(self.frame_1, text="Books Field", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.books_field_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.books_field_entry.place(x=300,y=200, width=200)

        self.phone_number = Label(self.frame_1, text="Phone Number", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.phone_number_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.phone_number_entry.place(x=40,y=270, width=200)

        self.quantity = Label(self.frame_1, text="Quantity", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.quantity_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.quantity_entry.place(x=300,y=270, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='SUBMIT DATA', font=(self.font_1, 12), bd=2, command=self.issue_submit ,bg=self.color_2,fg=self.color_3).place(x=40,y=350,width=455, height=50)

    def book_return_func(self):
        self.ClearScreen() 
        
        self.first_name1 = Label(self.frame_1, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.first_name_entry1_return = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.first_name_entry1_return.place(x=40,y=60, width=200)

        self.last_name1 = Label(self.frame_1, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.last_name_entry_return = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.last_name_entry_return.place(x=300,y=60, width=200)

        self.admission_number = Label(self.frame_1, text="Admission Number", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.admission_number_entry_return = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.admission_number_entry_return.place(x=40,y=130, width=200)

        self.roll_no = Label(self.frame_1, text="Roll No", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.roll_no_entry_return = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.roll_no_entry_return.place(x=300,y=130, width=200)

        self.books_name = Label(self.frame_1, text="Book Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.books_name_entry_return = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.books_name_entry_return.place(x=40,y=200, width=200)

        self.books_field = Label(self.frame_1, text="Books Field", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.books_field_entry_return = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.books_field_entry_return.place(x=300,y=200, width=200)

        self.phone_number = Label(self.frame_1, text="Phone Number", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.phone_number_entry_return = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.phone_number_entry_return.place(x=40,y=270, width=200)

        self.email = Label(self.frame_1, text="Quantity", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.email_entry_return = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry_return.place(x=300,y=270, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='SUBMIT DATA', font=(self.font_1, 12), bd=2, command=self.return_submit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=40,y=350,width=455, height=50)

    '''Updating the books........'''
    def update_books(self):
        self.ClearScreen()

        self.get_phone_details = Label(self.frame_1, text="Enter The Password", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=163,y=70)
        self.get_phone_details_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.get_phone_details_entry.place(x=163, y=110, width=200, height=30)
        
        self.get_book_name = Label(self.frame_1, text="Enter Book Name", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=163,y=160)
        self.get_book_name_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.get_book_name_entry.place(x=163, y=200, width=200, height=30)
        
        self.get_book_field = Label(self.frame_1, text="Enter Book Field", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=163,y=250)
        self.get_book_field_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.get_book_field_entry.place(x=163, y=300, width=200, height=30)
        
        self.get_book_quantity = Label(self.frame_1, text="Quantity", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=163,y=350)
        self.get_book_quantity_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.get_book_quantity_entry.place(x=163, y=400, width=200, height=30)
        
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, cursor="hand2", command=self.update_book_button, bg=self.color_2,fg=self.color_3).place(x=163,y=460,width=200, height=30)

    '''delete the books........'''
    def delete_books(self):
        self.ClearScreen()

        self.get_password_details = Label(self.frame_1, text="Enter Password", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=163,y=70)
        self.get_password_details_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.get_password_details_entry.place(x=163, y=110, width=200, height=30)
        
        self.get_book_name_delete = Label(self.frame_1, text="Enter Book Name", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=163,y=160)
        self.get_book_name_delete_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.get_book_name_delete_entry.place(x=163, y=200, width=200, height=30)
        
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, cursor="hand2", command=self.delete_book_button, bg=self.color_2,fg=self.color_3).place(x=163,y=280,width=200, height=30)

    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    def Exit(self):
        self.window.destroy()
    
    #creating button for issue function........        
    def issue_submit(self):
        #Connecting with database1......... 
        self.issue_database_connection = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
        #Connecting with database2........... 
        self.issue_database_connection1 = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database1)
        
        #creating cursor for both databases.........
        self.cursor1 = self.issue_database_connection.cursor()
        self.cursor2 = self.issue_database_connection1.cursor()
        
        #Extracting data from entry widget...........
        data1 = self.first_name_entry1.get()
        data2 = self.last_name_entry.get()
        data3 = self.admission_number_entry.get()
        data4 = self.roll_no_entry.get() 
        data5 = self.books_name_entry.get()
        data6 = self.books_field_entry.get()
        data7 = self.phone_number_entry.get()
        data8 = self.quantity_entry.get()
        
        self.cursor1.execute("select * from library_books_data where BooksName='"+str(data5)+"'")
        data = self.cursor1.fetchall()
        for i in data:
            book_name = i[0]
            book_field = i[1]
            book_quantity = i[2]
        
        try:
            if str(data5) in book_name and int(data8)<=int(book_quantity) and str(data6) in book_field:
                new_books_quantity = (int(book_quantity)-int(data8))
                query = "insert into library_userdata values(%s, %s, %s, %s, %s, %s, %s, %s)"
                self.cursor2.execute(query, (data1, data2, data3, data4, data5, data6, data7, data8))
                
                query0 = "insert into library_books_data values(%s, %s, %s)"
                query1 = "delete from library_books_data where BooksName=%s"
                self.cursor1.execute(query1, (book_name,))
                self.cursor1.execute(query0, (book_name, book_field, new_books_quantity))
                messagebox.showinfo("Data Submittion Successfull", "Library Database System Have Been Activated")
                
                if new_books_quantity==0:
                    query3 = "delete from library_books_data where BooksName=%s"
                    self.cursor1.execute(query3, (book_name, ))
                    messagebox.showinfo("Data Submittion Successfull", "Library Database System Have Been Activated")
                
                else:
                    None 
                    
            else:
                messagebox.showerror("Error", "The Data you enter is not correct according to the Library")
        
        except Exception as e:
            print(e)
        
        self.issue_database_connection1.commit()
        self.issue_database_connection.commit()
        self.issue_database_connection1.close()
        self.issue_database_connection.close()
    
    #creating button for return function........... 
    def return_submit(self):
        #Connecting with database1......... 
        self.return_database_connection = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
        #Connecting with database2........... 
        self.return_database_connection1 = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database1)
        
        #creating cursor for both databases.........
        self.cursor1_return = self.return_database_connection.cursor()
        self.cursor2_return = self.return_database_connection1.cursor()
        
        #Getting data from entry widgets.............. 
        data1 = self.first_name_entry1_return.get()
        data2 = self.last_name_entry_return.get()
        data3 = self.admission_number_entry_return.get() 
        data4 = self.roll_no_entry_return.get()
        data5 = self.books_name_entry_return.get()
        data6 = self.books_field_entry_return.get()
        data7 = self.phone_number_entry_return.get()
        data8 = self.email_entry_return.get()
        
        print(data1, data2, data3, data4, data5, data6, data7, data8)
        
        #reading data from user table.......... 
        self.cursor2_return.execute("select * from library_userdata where Admission_Number='"+str(data3)+"'")
        data = self.cursor2_return.fetchall()
        for i in data:
            user_admission_no = i[2]
            user_roll_no = i[3]
            user_books_quantity = i[7]
            user_books_name = i[4]
                    
        print(user_admission_no, user_roll_no, user_books_quantity)
        
        #reading data from books table.............
        self.cursor1_return.execute("select * from library_books_data where BooksName='"+str(user_books_name)+"'")
        user_data = self.cursor1_return.fetchall()
        for i0 in user_data:
            user_book_name = i0[0]
            user_book_field = i0[1]
            user_book_quantity = i0[2]
           
        try:
            if int(data3)==user_admission_no and int(data4)==user_roll_no and int(data8)<=user_books_quantity:
                new_books_quantity0 = (int(user_books_quantity)+int(data8))
                query6 = "insert into library_books_data values(%s, %s, %s)" 
                self.cursor1_return.execute(query6, (user_book_name, user_book_field,new_books_quantity0))
                messagebox.showinfo("Data Submittion Successfull", "Library Database System Have Been Activated")
                  
                if new_books_quantity0<int(data8):
                    query5 = "insert into library_books_data values(%s, %s, %s)" 
                    self.cursor1_return.execute(query5, (user_book_name, user_book_field,new_books_quantity0))
                    messagebox.showinfo("Data Submittion Successfull", "Library Database System Have Been Activated")
                    
                    new_books_quantity1 = int(int(user_books_quantity)-int(new_books_quantity0))
                    print(new_books_quantity1)
                 
                if new_books_quantity0==int(data8):
                    new_books_quantity3 = (int(user_books_quantity+new_books_quantity0))
                    query4 = "insert into library_books_data values(%s, %s, %s)" 
                    self.cursor1_return.execute(query4, (user_book_name, user_book_field,new_books_quantity3))
                
                    messagebox.showinfo("Data Submittion Successfull", "Library Database System Have Been Activated")
                
            else:
                messagebox.showerror("Error", "The Data you enter is not correct according to the Library")
        
        except Exception as e:
            print(e)
        
        self.return_database_connection1.commit()
        self.return_database_connection.commit()
        self.return_database_connection1.close()
        self.return_database_connection.close()

    def update_book_button(self):
        #Connecting with database1......... 
        self.update_database_connection = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
        
        #creating cursor for both databases.........
        self.cursor1 = self.update_database_connection.cursor()
        
        #Getting data from entry widgets.............. 
        data1 = self.get_phone_details_entry.get()
        data2 = self.get_book_name_entry.get()
        data3 = self.get_book_field_entry.get()
        data4 = self.get_book_quantity_entry.get()
        
        if str(data1)==self.user_password:
            query = "insert into library_books_data value(%s, %s, %s)"
            self.cursor1.execute(query, (data2, data3, data4))
            self.update_database_connection.commit()
            messagebox.showinfo("Data Submission Successfull", "Library Databases system have been activated") 
        
        else:
            messagebox.showerror("Error", "Submittion Failed due to incorrect password")
    
    def delete_book_button(self):
        #Connecting with database1......... 
        self.delete_database_connection = sq_connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
        
        #creating cursor for both databases.........
        self.cursor1 = self.delete_database_connection.cursor()
        
        #getting data from entry widgets......... 
        data1 = self.get_password_details_entry.get()
        data2 = self.get_book_name_delete_entry.get()
        
        if str(data1)==self.user_password:
            query = "delete from library_books_data where BooksName=%s"
            self.cursor1.execute(query, (str(data2),))
            self.delete_database_connection.commit()
            messagebox.showinfo("Data Submission Successfull", "Library Database System have been activated") 
            
        else:
            messagebox.showerror("Error", "Data Submission Failed Due to incorrect password") 
        
if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    obj.database_books_cretion()
    obj.database_user_creation()
    root.mainloop()
    
    