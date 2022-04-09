"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: distance.py
"""
import csv

# Return Distance Matrix
class Matrix:
    # Create a Distance Matrix & Index Dictionary
    def __init__(self):
        with open('WGUPS Distance Table.csv') as file:
            self.matrix = []
            self.index = {}
            reader = csv.reader(file)
            headers = next(reader)[2:]
            for row in reader:
                del row[0]
                del row[0]
                for item in row:
                    if item != '':
                        row[row.index(item)] = float(item)
                    else:
                        row[row.index(item)] = None
                self.matrix += [row]

            for i, value in enumerate(headers):
                self.index[i] = value

            # Fill the Empty to Create Birectional Matrix
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    self.matrix[i][j] = self.matrix[j][i]

    def getvalue(self, iandj): # format 'i5j3' -> i = 5, j = 3
            parse = iandj.split('i')[1].split('j')
            i = int(parse[0])
            j = int(parse[1])
            return self.matrix[i][j]


