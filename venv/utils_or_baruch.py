import sys
import math
import json
import numpy as np


with open("data.json",'r') as file:
    file_data = file.read()
    converted_data = json.loads(file_data) # receives a str object that represents txt in JSON and translates it

class Matrix:
    arr = []
    def __init__(self, file_data):
        self.file_data = file_data

    def parse(self, property):
        arr = []
        for tup in self.file_data:
            for key in tup:
                if key == property:
                    arr.append(dict(tup)[key])
                # else throw exception bad property
        arr = np.array(arr,dtype=object) #mainly to handle the string array
        return arr

    def average(self, property):
        arr =[]
        arr = self.parse(property)
        names_in_ascii = []
        if property == "average" or property == "id":
            arr = self.parse(property)
            print("The average value of the property: " + str(property) + "," + " is: " + str(np.average(arr)))
        if property == "name":
            for word in arr: # for every name in arr of names
                if word.isalpha():  # checks if word(name) is alphabetic before converting to ascii
                    for letter in word: # for every letter in name
                        number = ord(letter) - 96 #convertion to ascii
                        names_in_ascii.append(number)
            print("The average value of the property: "
                  + str(property) + "," + " is: " + str(round(np.average(names_in_ascii),4)))

    def min(self, property):
        arr = []
        arr = self.parse(property)
        print("The min value of the property: " + str(property) + "," + " is: " + str(np.min(arr)))

    def max(self, property):
        arr = []
        arr = self.parse(property)
        print("The max value of the property: " + str(property) + "," + " is: " + str(np.max(arr)))

    def total(self, property):
        arr = []
        arr = self.parse(property)
        # if property != "name":
        print("The total value of the property: " + str(property) + "," + " is: " + str(np.sum(arr)))
        # if property == "name": return np.sum(arr)

class MatrixException(Exception):
    pass

    def __init__(self, txt):
        self.message = txt


ob = Matrix(converted_data)
ob.average("name")

# except MatrixException as e:
#     print(e.message)
#
# finally:
file.close()

#
#
# d = dict()
# years = []
#
# (get 2 column list of years and values)
#
# for line in list:
#     year = line[0]
#     value = line[1]
#
# for line in list:
#     if year in d.keys():
#         d[value].append(value)
#     else:
#         d[value] = value
#         d[year] = year
#
# years_dict = dict()
#
# for line in list:
#     if line[0] in years_dict:
#         # append the new number to the existing array at this slot
#         Matrix["name"].append(line[1])
#     else:
#         # create a new array in this slot
#         years_dict[line[0]] = [line[1]]