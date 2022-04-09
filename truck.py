"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: truck.py
"""
import globals
import path_algo as p
import database as db

class Truck:
    def __init__(self, name):
        self.truck = name
        self.gas = "Unlimit"
        self.driver_seat = []
        self.cargo = []
        self.mileage = 0
        self.MPH = 18

    def driver(self, person):
        if len(self.driver_seat) == 0:
            self.driver_seat.append(person)
        else:
            print("ERROR: DRIVER SEAT IS FULL")

    # load Max of 16 packages
    def load(self, ID):
        if len(self.cargo) < 16:
            self.cargo.append(ID)
        else:
            print("ERROR: CARGO IS FULL")

    # Get delivery location nodes base on lookup ID address
    def get_delivery_nodes(self, map=globals.mymap):
        if len(self.cargo) != 0:
            nodelist = []
            for ID in self.cargo:
                pacakgeaddress = globals.mydb.lookup('ID', ID)[1]
                for node in map.index:
                    if pacakgeaddress in map.index[node]:
                        if node in nodelist:
                            continue
                        else:
                            nodelist += [node]
            return nodelist
        else:
            print("ERROR: CARGO IS EMPTY")

    # Get Route From Path Algo
    def getroute(self):
        self.algoroute = p.Path(self.get_delivery_nodes()).get_route()


    # Called Get Route
    # Update Packages Status when Each Node Hit Time = Mileage / 40MPH
    def go(self, time, map=globals.mymap):
        print(self.truck, 'depart at', str(time))
        self.getroute()
        route = self.algoroute
        for ID in list(self.cargo):
            globals.mydb.updateenroute(ID, time)
        drivetime = 0

        for k in range(len(route) - 2):
            i = route[k]
            j = route[(k + 1)]
            eachdist = map.matrix[i][j]
            self.mileage += eachdist
            secs = round((eachdist / self.MPH) * 60 * 60)
            drivetime += secs
            time = db.addSecs(time,secs)
            for ID in list(self.cargo):
                pacakgeaddress = globals.mydb.lookup('ID', ID)[1]
                arrivednode = j
                if pacakgeaddress in map.index[arrivednode]:
                    globals.mydb.updatedelivered(ID, time)
                    self.cargo.remove(ID)
        print(self.truck, 'is back at', str(time))