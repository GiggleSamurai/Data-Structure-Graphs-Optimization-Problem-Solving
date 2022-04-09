"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: main.py
"""
import globals
import database as db
globals.initialize()
import truck as t
import hub as h
import path_algo as p
import interface

#### Main Operation ###

# Import Global Database
mydb = globals.mydb
myhub = h.Hub()

# Create Trucks
truck1, truck2, truck3 = t.Truck("Truck 1"), t.Truck("Truck 2"), t.Truck("Truck 3")
globals.globalTrucks(truck1, truck2, truck3)

# Load Packages to Truck
truck1, truck2, truck3 = myhub.load2truck(truck1,truck2,truck3)

# Get Route
truck1nodes, truck2nodes, truck3nodes = truck1.get_delivery_nodes(), truck2.get_delivery_nodes(), truck3.get_delivery_nodes()
truck1route, truck2route, truck3route = p.Path(truck1nodes).get_route(), p.Path(truck2nodes).get_route(), p.Path(truck3nodes).get_route()

# Depart
truck1depart_time = db.maketime('8:00:00')
truck1.go(truck1depart_time)
truck2depart_time = db.maketime('8:00:00')
truck2.go(truck2depart_time)
mydb.updateaddress(9, '410 S State St', 'Salt Lake City', 'UT', 84111) # Address Correction at 10:20:00
truck3depart_time = db.maketime('10:24:20') # Truck 1 Driver is back at 10:24:20
truck3.go(truck3depart_time)


#####################################################

# Initiate Interface Screen
interface.mainscreen()