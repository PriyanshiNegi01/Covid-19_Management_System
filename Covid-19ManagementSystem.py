import mysql.connector as s

mydb = s.connect(host='localhost', user='root', passwd='admin', database='priyanshidb')

if mydb.is_connected():
    print('Database is successfully connected.')

mycursor = mydb.cursor()
g = 0
h = 0
m = 0

# TABLE CREATION

'''
mycursor.execute("create table ward(ward varchar(20), ward_stat varchar(20),beds varchar(20));")
mycursor.execute("create table bill (b_name varchar(20), b_day int, b_room int, b_pd int, b_pl int, b_mtd varchar(3));")
mycursor.execute("create table transport (t_ambno int, t_drv varchar(20), t_mob bigint);")
mycursor.execute("create table patient(p_name varchar(20),p_admt varchar(20) ,p_age int,p_mob bigint,p_add varchar(30),p_stat varchar(1));")
mycursor.execute("create table family (k varchar(20), n varchar(20), d varchar(20));")
mycursor.execute("create table doctor (d_name varchar(20), d_dept int, d_mob bigint);")
mycursor.execute("create table vaccine_detail (v_date varchar(20), v_no float, v_pat float, v_left float);")
'''

users = ["Priyanshi", "Ruhi"]

print("**********************************************")
print("                                              ")
print("     WELCOME TO COVID-19 MANAGEMENT SYSTEM    ")
print("                                              ")
print("**********************************************")
print("                                              ")
print("      MAKING HEALTHCARE BETTER TOGETHER.      ")
print("                                              ")
print("**********************************************")
print("                                              ")
print("================")
print("Press 1 to LOGIN")
print("================")
print("Press 2 to EXIT")
print("================")

mainchoice = int(input("Enter your choice:"))

print("**********************************************")
print("                                              ")
print("                  LOGIN PAGE                  ")
print("                                              ")
print("**********************************************")

users = ["Priyanshi", "Ruhi"]

if mainchoice == 1:
    user1 = input("Admin name:")
    pwd1 = input("Password:")
    
    if user1 in users and pwd1 == '1234':               # to check if correct username and password is entered
        print("Logged in succesfully...")
        print("************************")
        print("      WELCOME ADMIN     ")
        print("************************")

        # MAIN MENU
        print("                                            ")
        print("============================================")
        print("                  MAIN MENU                 ")
        print("============================================")
        print("1. Reception details")
        print("============================================")
        print("2. Transport details")
        print("============================================")
        print("3. Patient and family details")
        print("============================================")
        print("4. Doctor details")
        print("============================================")
        print("5. Vaccine details")
        print("============================================")
        print("6. View all records")
        print("============================================")

        choice = int(input('ENTER YOUR CHOICE from the main menu:'))
        
    while user1 in users and pwd1 == '1234':

        if choice == 1:  # 1. Reception details              # SUB MENU for 1st choice (SUB MENU 1)
            
            print('1. Insert Wards Data')
            print("___________________________________")
            print('2.Insert Patient Transaction Details')
            print("____________________________________________")

            ch1 = int(input('ENTER YOUR CHOICE:'))           # This is the choice in SUB MENU 1

            if ch1 == 1:  # Wards Data	
                ward = input('Ward no:')
                ward_stat = input('Occupied or Vacant:')
                beds = int(input('Enter the no. of beds in ward:'))
                q = "insert into ward values('{}','{}',{})".format(ward, ward_stat, beds)
                mycursor.execute(q)
                mydb.commit()
                print('SUCCESSFULLY REGISTERED!')

            elif ch1 == 2:  # Patient Transaction details
                b_name = input("Enter the name of patient:")
                b_day = int(input("Enter the no. of days patient was admitted for:"))
                b_room = int(input("Enter room no. of patient:"))
                b_pd = int(input("Enter the amount already deposited:"))
                b_pl = b_day * 30000 - b_pd
                b_mtd = input("Enter the payment method\a=cash\b=check\ c=online:")
                q = "insert into bill values('{}',{},{},{},{},'{}')".format(b_name, b_day, b_room, b_pd, b_pl, b_mtd)
                mycursor.execute(q)
                mydb.commit()
                print('SUCCESSFULLY REGISTERED!')
            
            else:
                print("Please choose a valid option.")

        elif choice == 2:  # 2. Transport details
            
            t_ambno = int(input("Enter the ambulance no.:"))
            t_drv = input("Enter the name of driver:")
            t_mob = int(input("Enter the mobile no. of driver:"))
            mycursor.execute("insert into transport values({},'{}',{})".format(t_ambno, t_drv, t_mob))
            mydb.commit()
            print('SUCCESSFULLY REGISTERED!')

        elif choice == 3:  # 3. Patient and family details       # SUB MENU for 3rd choice (SUB MENU 2)
            
            print("============================================")
            print("1. Insert Patient Details")
            print("============================================")
            print("2. Insert Patients family details")
            print("============================================")
            print("3. Total no. of patients tested positive")
            print("============================================")
            print("4. Total Patients Recovered")
            print("============================================")
            print("5. Total Patients Dead")
            print("============================================")
            print("6. Total Patients Under Treatment")
            print("============================================")
            print("7. Update Patient Status")
            print("============================================")

            ch2 = int(input('ENTER YOUR CHOICE:'))                # This is the choice in SUB MENU 2

            if ch2 == 1:  # Patient details
                p_name = input("Enter Patient Name:")
                p_admt = input("Enter the admit date of patient:")
                p_age = int(input("Enter Age:"))
                p_mob = int(input("Enter Phone number:"))
                p_add = input("Enter patients locality:")
                p_stat = input("Enter the present condition of patient => Under Treatment(U)/Recovered(R)/Dead(D):")
                q = "insert into patient value('{}','{}',{},{},'{}','{}')".format(p_name, p_admt, p_age, p_mob, p_add, p_stat)
                mycursor.execute(q)
                mydb.commit()
                print('SUCCESSFULLY REGISTERED!')

            elif ch2 == 2:  # Family details
                k = int(input("No. of family members in contact with patient:"))
                n = int(input("No. of family members tested positive if any:"))
                d = int(input("No. of family members undergoing medical treatment:"))
                q = "insert into family values({},{},{})".format(k, n, d)
                mycursor.execute(q)
                mydb.commit()
                print('SUCCESSFULLY REGISTERED!')

            elif ch2 == 3:  # Total positive patients
                mycursor.execute("select count(p_name) as covid_patients from patient")
                c = mycursor.fetchone()
                for i in c:
                    print(i, "is the no. of covid payients till date")

            elif ch2 == 4:  # Recovered patients
                mycursor.execute("select count(p_stat) from patient where p_stat = 'recovered'")
                s = mycursor.fetchone()
                for i in s:
                    print(i, "is the no. of covid patients recovered")

            elif ch2 == 5:  # Total deaths
                mycursor.execute("select count(p_stat) from patient where p_stat = 'dead'")
                s = mycursor.fetchone()
                for i in s:
                    print(i, "is the no. of covid related deaths")

            elif ch2 == 6:  # Under treatment
                mycursor.execute("select count(p_stat) from patient where p_stat = 'under treatment'")
                s = mycursor.fetchone()
                for i in s:
                    print(i, "is the no. of covid patients under treatment")

            elif ch2 == 7:  # Update patient status
                l = input("Enter the name of the patient for whom records are to be updated")
                k = input("Enter new status")
                q = "update patient set p_stat = '{}' where p_name = '{}'".format(k, l)
                mycursor.execute(q)
                mydb.commit()
                print('SUCCESSFULLY REGISTERED!')

            else:
                print("Please choose a valid option.")

        elif choice == 4:  # 4. Doctor details
                               
            d_name = input('Enter Doctor Name:')
            d_dept = int(input('Enter the Department:'))
            d_mob = int(input('Enter Phone number:'))
            mycursor.execute("insert into doctor values('{}',{},{})".format(d_name, d_dept, d_mob))
            print('SUCCESSFULLY REGISTERED!')
            mydb.commit()

        elif choice == 5:  # 5. Vaccine details                # SUB MENU for 5th choice (SUB MENU 3)
                               
            print("============================================")
            print('1. Vaccine details')
            print("============================================")
            print('2. Total vaccinated patients')
            print("============================================")
            print('3. Check for aviliable vaccines')
            print("============================================")
                               
            ch3 = int(input('ENTER YOUR CHOICE:'))

            if ch3 == 1:  # Vaccine details                    # This is the choice in SUB MENU3
                v_date = input("Enter the date of arrival:")
                v_no = int(input("Enter the no. of vaccine arrived on perticular day:"))
                v_pat = int(input("Enter the no. of patients vaccinated on the day:"))
                v_left = v_no - v_pat
                mycursor.execute("insert into vaccine_details values('{}',{},{},{})".format(v_date, v_no, v_pat, v_left))
                mydb.commit()
                print('SUCCESSFULLY REGISTERED!')

            elif ch3 == 2:  # Total vaccinated patients
                mycursor.execute("select sum(v_pat) as total_vaccinated_patient from vaccine_detail")
                c = mycursor.fetchone()
                for i in c:
                    print(i, "is the no. of total patients vccinated.")

            elif ch3 == 3:  # Check for available vaccines
                mycursor.execute("select sum(v_left) as total_vaccines_left from vaccine_detail")
                c = mycursor.fetchone()
                for i in c:
                    print(i, "are the total no. of vaccines left.")

            else:
                print("Please choose a valid option.")

        elif choice == 6:  # 6. View all records               #SUB MENU4
                        
            print("============================================")
            print("1. Bill records")
            print("============================================")
            print("2. Transport records")
            print("============================================")
            print("3. Patient records")
            print("============================================")
            print("4. Family records")
            print("============================================")
            print("5. Doctor  records")
            print("============================================")
            print("6. Vaccine records")
            print("============================================")

            ch4 = int(input('ENTER YOUR CHOICE:'))             #This is the choice in SUB MENU 4

            if ch4 == 1:  # Reception: Ward & Bill records
                print("--------Bill details---------")
                mycursor.execute("select * from bill")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 2:  # Transport records
                print("--------Transport details--------")
                mycursor.execute("select * from transport")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 3:  # Patient records
                print("--------Patient details--------")
                mycursor.execute("select * from patient")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 4:  # Family records
                print("--------Family details--------")
                mycursor.execute("select * from family")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 5:  # Doctor records
                print("--------Doctor details--------")
                mycursor.execute("select * from doctor")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 6:  # Vaccine records
                print("--------Vaccine details--------")
                mycursor.execute("select * from vaccine_detail")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            else:
                print("Please choose a valid option.")
    else:
        print("Invalid username or password.")

if mainchoice == 2:
    exit()
