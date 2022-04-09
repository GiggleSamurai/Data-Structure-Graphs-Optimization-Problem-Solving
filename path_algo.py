"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: path_algo.py
"""
import globals

class Path:
    def __init__(self, nodeslist):
            self.unvisited_nodes = nodeslist
            self.visited_nodes = [0]

    # Move Unvisited to Visit Item
    def visit(self, node):
        self.unvisited_nodes.remove(node)
        self.visited_nodes.append(node)

    # Base on All Available Nodes, Get Next Short Aka.Greedy Algorithm
    def next_shortest(self, map=globals.mymap):
        current = self.visited_nodes[-1]
        compare = {}
        for j in self.unvisited_nodes:
            compare[j] = map.matrix[current][j]
        min_distance = min(compare, key=compare.get)
        return min_distance

    # Get the Design Full Route
    def get_route(self):
        for i in range(len(self.unvisited_nodes)):
            self.visit(self.next_shortest())
        route = self.visited_nodes + [self.visited_nodes[0]]
        return route

    # Sum of All Distance from Design Route
    def sumofdist(self, route, map=globals.mymap):
        sum = 0
        for k in range(len(route)-2):
            i = route[k]
            j = route[(k+1)]
            sum += map.matrix[i][j]
        return sum