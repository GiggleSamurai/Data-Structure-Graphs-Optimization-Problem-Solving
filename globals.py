"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: globals.py
"""
import database as db
import distance as dt

# Global database & map matrix
def initialize():
    global mydb
    mydb = db.DataBase()
    global mymap
    mymap = dt.Matrix()
    # Correct Address '3575 W Valley Central Sta bus Loop' -> '3575 W Valley Central Station bus Loop'
    mymap.index[16] = 'West Valley Prosecutor\n 3575 W Valley Central Station bus Loop'
    # Delay
    delay = [6, 25, 28 ,32]
    delaytime = db.maketime('9:05:00')
    for ID in delay:
        mydb.updatehub(ID, delaytime)

# Global Trucks
def globalTrucks(*truck):
    global truck1, truck2, truck3
    truck1, truck2, truck3 = truck