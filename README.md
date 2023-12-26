# Library-Management-System-Created By Tahil 
This is a Simple Library management system using tkinter and mysql-connector

..............Please Read Requrements.txt file First..................

1.) Display the Data from MySQL Database....
![Screenshot (8)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/86da7299-7238-42bd-b7a8-61bc6e3fea7b)

2.) Issue the book and Save Data to MySQL Database....
![Screenshot (9)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/ba816c8a-eefb-4b38-ae28-fedc0f98b656)

3.) ADD A New Book to Library Database....
![Screenshot (10)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/8b814198-6d88-4900-9d42-0d1184565859)

4.) Delete Book From Library Database...
![Screenshot (11)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/e9449966-da12-4948-8985-e9e62e7ebe8a)

5.) Show The Records of Issued Persons
![Screenshot (12)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/5abd063b-09ef-4cb4-92f9-3d4b0685e543)

6.) Books Data in MySQL DataBase....
![Screenshot (13)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/d15227ab-cecd-4495-8b47-6051322b76e4)

7.) User data in MySQL DataBase.....
![Screenshot (14)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/d07465ad-a08e-4226-b1ea-aa07c80e3743)

8.) Comment out this two functions objects after running the programme because the second time the database is already exists......
![Screenshot (16)_LI](https://github.com/Tahil40/Library-Management-System-/assets/116889476/0d3659ed-25c6-4613-a35f-ec576bd7144d)

EXPLANATION OF PROGRAMME=>>>>>>>>>MUST READ ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️  

LIBRARIES USED>>>>>>
1. tkinter (Already comes with python)
2. mysql-connector (Needed to be installed)

MEDIA USED>>>>>>>
1. arc.ico.ico(contains the icon image)
2. password.py(conatins the password)

EXPLANATION OF PROGRAMME.................>>>>>>
This project is created by using oops(Object Orientied Programming Language) in Python. 

![Screenshot (20)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/633fc9a2-a22b-415f-bd90-45572618b5be)
Importing libraries Creating Class By Giving The Name Management.
 
![Screenshot (21)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/f2ffd547-c194-4403-aef2-439e185e0704)
Inherited the class Management by The Class Tk() and creating the Variable named root in the Name function.

![Screenshot (23)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/f4480ab2-a298-41c5-9c8e-e7e61fbb9ab7)
Created Constructor(__init__).

1.) In this constructor the class variables are created for setting the   
     main windows configuration. 
2.) Customizing Obejcts are created to give to give the color to the 
    widgets and setting the columns for treeview widget. 

3.) Connection objects are created to store the Data of user of MySQL 
    database like- HostName, user, Password and Database Name. 

![Screenshot (33)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/b7671b69-7601-4d41-822c-948ae31b7e0c)
Creating Frames By Variables Name Frames_1(Left Frame) and Frame_2(Right Frame) and creating the Buttons in Frame_2 Variable.
Buttons are created in Right Frame.

FUNCTIONS CREATED=====>>>>>>

1.) database_books_cretion().
![Screenshot (25)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/29e6b072-0cde-4e4c-bf01-e75d98ff85a5)

WORKING => This Function Creates The Database Named 'Library_book1' and create the Table named 'library_book_data' to store the books Data in the MySQL Database.
 
2.) database_user_creation(). 
![Screenshot (26)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/3b5147f2-1432-4241-96f4-e63be347a057)

WORKING => This Function Creates The Database Named 'Library_user_data1' and create the Table named 'library_userdata' to store the user Data in the MySQL Database.

3.) display_books(). 
![Screenshot (27)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/71a323fd-9b46-49e5-9053-1d9c5ac135f5)

WORKING => This Function Creates (TreeView) and (Scrollbar) widget and store books data from MySQL Database to this treeview widget. 

4.) show_records(). 
![Screenshot (28)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/f80c138f-d7dd-4197-ac50-90f384a53312)

WORKING => This Function Creates (Treeview) and (Scrollbar) widget and store data user data from MySQL Database to this treeview widget.

5.) books_issue_func(). 
![Screenshot (29)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/168922fa-75fa-4c38-a070-22b625347bc7)

WORKING => Contains entry widgets that takes data of issued persons. 

6.) book_return_func(). 
![Screenshot (30)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/1dc12cd9-d9ea-4408-8c14-ed0cf9392a13)

WORKING => Contains entry widgets that takes data of those persons who retuned the book.

7.) update_books(). 
![Screenshot (34)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/c019a5e9-3429-4658-9458-9a3f06ab9626)

WORKING => Conatins entry widgets to take data from admin to update in MySQL books Database.

8.) delete_books(). 
![Screenshot (35)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/a158651e-1353-4d98-81f6-4949426dd8a9)

WORKING => Conatins entry widgets to take data from admin to delete in MySQL books Database.

9.) ClearScreen() and Exit(). 
![Screenshot (36)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/27653ad8-40f2-440b-9c18-3def649b58dd)

WORKING => To Clear the widgets and to exit from the main window.

10.) issue_submit().
![Screenshot (37)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/40ea8149-3789-4d67-af28-7af6aed05b8a)

WORKING => Connecting to MySQL Database and Store The data of person who issued the book to MySQL Database.

11.) return_submit(). 
![Screenshot (38)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/8741c774-f95b-4143-bd9d-652737909780)

WORKING => Connecting to MySQL Database and Store data of person who returned the book to MySQL Database.

12.) update_book_button(). 
![Screenshot (41)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/86c61c24-7c4c-4818-9aa3-eb32cc7806cb)

WORKING => Connecting to MySQL Database and Connecting to MySQW database and update the book according to data that is entered by the user.

13.) delete_book_button(). 
![Screenshot (42)](https://github.com/Tahil40/Library-Management-System-/assets/116889476/5ee0687f-da75-4321-ac65-1641a62ffade)

WORKING => Connecting to MYSQL database and delete the book according to the data that is entered by the user.

👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍
