"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: database.py
"""
import csv
import datetime as dt
import hash_table as ht

# Time function to make time conversion easier
def addHours(time, hours):
    fulldate = dt.datetime(100, 1, 1, time.hour, time.minute, time.second)
    fulldate = fulldate + dt.timedelta(hours=hours)
    return fulldate.time()

def addSecs(time, secs):
    fulldate = dt.datetime(100, 1, 1, time.hour, time.minute, time.second)
    fulldate = fulldate + dt.timedelta(seconds=secs)
    return fulldate.time()

def maketime(HHMMSS):
    time = dt.datetime.strptime(HHMMSS, '%H:%M:%S').time()
    return time

# Create Hash Table that hold all packages data
class DataBase:
    def __init__(self):
        self.currenttime = dt.datetime.strptime('8:00:00', '%H:%M:%S').time()
        self.starttime = dt.datetime.strptime('8:00:00', '%H:%M:%S').time()
        self.table = self.csv2table()
        self.ID = list(range(1, 41))
        self.HashTable = ht.HashTable(10)
        self.RenderedHashTable = ht.HashTable(10)
        for row in self.table:
            row.append({})
            row[8]['hub'] = self.starttime
            row[8]['enroute'] = 'Not Yet'
            row[8]['delivered'] = 'Not Yet'
            self.HashTable.insert(row)

        # Render A Separate Hash Table to Display Factor in base on Set Time
        self.rendertime()

    # Read the csv table
    def csv2table(self):
        with open('WGUPS Package File.csv') as file:
            table = []
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                row[0] = int(row[0])
                row[4] = int(row[4])
                row[6] = int(row[6])
                table += [row]
            return table

    # Get ID
    def getID(self):
        return list(self.ID)

    # Function to Set Current Time
    def settime(self, HHMMSS):
        self.currenttime = dt.datetime.strptime(HHMMSS, '%H:%M:%S').time()
        self.rendertime()

    def setstarttime(self, HHMMSS):
        self.starttime = dt.datetime.strptime(HHMMSS, '%H:%M:%S').time()

    def getall(self):
        all = []
        for ID in self.ID:
            package = self.RenderedHashTable.lookup(ID)
            all.append(package)
        return all

    # Look up function by ID, address, deadline, city, zip, weight, note , (status, time)
    # Return all that matches
    def lookup(self, parameter, value):
        matchpackages = []
        for ID in self.ID:
            package = self.RenderedHashTable.lookup(ID)
            if parameter == 'ID':
                if package[0] == value:
                    matchpackages = package
            elif parameter == 'address':
                if package[1] == value:
                    matchpackages.append(package)
            elif parameter == 'deadline':
                if package[5] == value:
                    matchpackages.append(package)
            elif parameter == 'city':
                if package[2] == value:
                    matchpackages.append(package)
            elif parameter == 'zip':
                if package[4] == value:
                    matchpackages.append(package)
            elif parameter == 'weight':
                if package[6] == value:
                    matchpackages.append(package)
            elif parameter == 'note':
                if package[7] == value:
                    matchpackages.append(package)
            elif parameter == 'status':
                if package[8] == value:
                    matchpackages.append(package)

        return matchpackages

    # Specify Update Method
    def update(self, ID, value):
        self.HashTable.update(ID, value)
        self.rendertime()

    def updatehub(self, ID, time):
        package = self.HashTable.lookup(ID)
        package[8]['hub'] = time
        self.HashTable.update(ID, package)

    def updateenroute(self, ID, time):
        package = self.HashTable.lookup(ID)
        package[8]['enroute'] = time
        self.HashTable.update(ID, package)


    def updatedelivered(self, ID, time):
        package = self.HashTable.lookup(ID)
        package[8]['delivered'] = time
        self.HashTable.update(ID, package)

    def updateaddress(self, ID, address, city, state, zip):
        package = self.HashTable.lookup(ID)
        package[1] = address
        package[2] = city
        package[3] = state
        package[4] = zip
        self.HashTable.update(ID, package)
        self.rendertime()

    # Create A Display Table Base on Time Setting
    def rendertime(self):
        self.RenderedHashTable = ht.HashTable(10)
        for ID in self.ID:
            package = self.HashTable.lookup(ID)
            status = package[8]

            if self.currenttime >= status['hub']:
                try:
                    if self.currenttime >= status['enroute']:
                        try:
                            if self.currenttime >= status['delivered']:
                                row = package[:-1] + ['Delivered @ ' + str(status['delivered'])]
                            else:
                                row = package[:-1] + ['Enroute @ ' + str(status['enroute'])]
                        except:
                            row = package[:-1] + ['Enroute @ ' + str(status['enroute'])]
                    else:
                        row = package[:-1] + ['Hub @ ' + str(status['hub'])]
                except:
                    row = package[:-1] + ['Hub @ ' + str(status['hub'])]

            else:
                if '9:05' in str(status['hub']):
                    row = package[:-1] + ['Delayed Arriving Hub @ 9:05:00']
                else:
                    row = package[:-1] + ['Expect Arriving Hub @ 8:00:00']

            self.RenderedHashTable.insert(row)