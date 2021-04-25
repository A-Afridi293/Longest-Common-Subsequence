# import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline
import plotly
import random

file = open("rand1000000.txt","r")
# Read in the file into an array and strip any extra characters.
data2 = file.read().split(" ")
for index,element in enumerate(data2):
    data2[index] = element.strip()
data2 = [x for x in data2 if x != '']

file.close()

class myDict:

    def __init__(self):
        # Create an empty array of size 10000
        self.data = [[] for i in range(10000)]
        self.counter = 0
        self.collision = {}
  
    def lcs(self,X, Y, m, n):
        self.counter+=1

        # Base case: If the lengths of the input strings are 0, return 0.
        if (m == 0 or n == 0):
            return 0
    
        # If the last characters of the input are the same, then recursively call lcs again and cut off the last characters of the input.
        if (X[m - 1] == Y[n - 1]):
            return 1 + self.lcs(X, Y, m - 1, n - 1)
        # Else, recursively call the function with the last two characters in the input string.
        else:
            return max(self.lcs(X, Y, m, n - 1),
                    self.lcs(X, Y, m - 1, n))
    # This hash function takes the string to compare with, then calls the lcs function to find least common subsequence. Returns the hash value of the counter object.
    def hash(self, element):
        self.counter = 0
        Y = "0123456789"
        self.lcs(element, Y, len(element), len(Y))
        return self.counter % 10000
    # This function inserts an element into the hash table given its hash value.
    def insert(self,element):
        index = self.hash(element)
        # If a collision is detected, then go up one index.
        if index in self.collision:
            self.collision[index] +=1
        else:
            self.collision[index] = 0 
        self.data[index].append(element)
        
obj = myDict()
# Test values used.
test = [str(x) for x in random.sample(range(1000000),10000)]

# Add every element in the data2 array into hash table.
for element in data2:
    obj.insert(element)

# x is the data to plot on x-axis, y is the data to plot on the y-axis.
x = [element[0] for element in obj.collision.items()]
y = [element[1] for element in obj.collision.items()]

# Plot all the values into a bar graph given the x and y values from before.
plot = plotly.graph_objs.Bar(x = x, y = y, marker = dict(color = ['rgba(0,0,255,255)']*len(x)),width = [5]*len(x))
# Lable all the terms in the graph.
layout = plotly.graph_objs.Layout(title = "LCS Hash Graph", xaxis = dict (title = "Hash Keys"), yaxis = dict (title="Number of Collisions Per Bucket"))

# Draw the graph to an html file.
figure = plotly.graph_objs.Figure(data = plot, layout = layout)
plotly.offline.plot(figure, filename = "test.html")
# [(hashKey1, keyValye1), (hashKey2, keyValue2), ..., ()]
# [hashKey1, hashKey2, etc...]
# [keyValue1, keyValue2, etc...]

# unzip tool for python lists
# combined = zip(x, y)

