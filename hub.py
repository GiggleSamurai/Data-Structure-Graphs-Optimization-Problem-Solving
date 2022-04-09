"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: hub.py
"""
import globals

class Hub:
    def __init__(self):
        self.inventory = globals.mydb.getID()

    # Load Packages with Note First
    def load2truck(self, truck1, truck2, truck3):
        for ID in list(self.inventory):
            packagenote = globals.mydb.lookup('ID', ID)[7]

            if "delivered with" in packagenote:
                # load to truck 1
                truck1.load(ID)
                self.inventory.remove(ID)
            elif "truck 2" in packagenote:
                # load to truck 2
                truck2.load(ID)
                self.inventory.remove(ID)
            elif ("not arrive" or "wrong address") in packagenote:
                # load to truck 3
                truck3.load(ID)
                self.inventory.remove(ID)


        # Load Rest of the Packages to Truck
        for ID in list(self.inventory):
            if len(truck1.cargo) < 16:
                truck1.load(ID)
                self.inventory.remove(ID)
                continue
            if len(truck2.cargo) < 16:
                truck2.load(ID)
                self.inventory.remove(ID)
                continue
            if len(truck3.cargo) < 16:
                truck3.load(ID)
                self.inventory.remove(ID)
                continue
        return truck1, truck2, truck3