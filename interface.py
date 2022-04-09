import globals

mydb = globals.mydb

"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: interface.py
"""
# Create Main Screen
def mainscreen():
    while True:
        try:
            print(
                '\n--- THE MAIN MENU ---\n Enter A Number: \t1.Get_All_Packages \t2.Get_Package_By_ID \t3.Get_Total_Mileage')
            userinput = input()
            if int(userinput) == 1:
                getallpackages_screen()
            elif int(userinput) == 2:
                getpackagebyID_screen()
            elif int(userinput) == 3:
                gettotalmilieage_screen()
            break
        except:
            continue

# Create All Package Screen
def getallpackages_screen():
    while True:
        try:
            print('Enter the Time(HH:MM:SS): ')
            usertime = input()
            mydb.settime(usertime)
            for package in mydb.getall():
                print('ID: ', package[0],
                      '  Address: ', package[1], package[2], package[3], package[4],
                      '  Deadline: ', package[5],
                      '  Weight: ', package[6],
                      '  Note: ', package[7],
                      '  Status & Time: ', package[8])
            mainscreen()
            break
        except:
            print('Entry Invalid!')
            continue

# Create Total Mileage Screen
def gettotalmilieage_screen():
    while True:
        try:
            totalmileage = round(globals.truck1.mileage + globals.truck2.mileage + globals.truck3.mileage)
            print('Total Mileage Driven: ', totalmileage)
            mainscreen()
            break
        except:
            print('Entry Invalid!')
            continue

# Get Package By ID Screen
def getpackagebyID_screen():
    while True:
        try:
            print('Enter the Time(HH:MM:SS): ')
            usertime = input()
            print('Enter the Package ID #: ')
            userID = input()
            mydb.settime(usertime)
            package = mydb.lookup('ID', int(userID))
            print('ID: ', package[0],
                  '  Address: ', package[1], package[2], package[3], package[4],
                  '  Deadline: ', package[5],
                  '  Weight: ', package[6],
                  '  Note: ', package[7],
                  '  Status & Time: ', package[8])
            mainscreen()
            break
        except:
            print('Entry Invalid!')
            continue