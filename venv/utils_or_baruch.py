# The progam reads a JSON type data file, uses numpy functions and throws Exceptions.

import sys
import math
import json
import numpy as np
import os.path

fileName = 'data.json'

class MatrixException(Exception):
    pass

    def __init__(self, txt):
        self.message = txt

class Matrix:
    arr = []
    def __init__(self, file_data):
        self.file_data = file_data

    def parse(self, property): # parsing data from json file to a list of dict for a specific given proprety
        arr = []
        for dictio in self.file_data: # for every dictionary in the list coming from data file
            for key in dictio:  # refers to the key of the current dictionary (from the list)
                if property != "name" and property != "id" and property != "average":
                    raise MatrixException("Wrong property")
                if key == property: # checks if that key from the dictionary matches the proprety argument
                    arr.append(dict(dictio)[key]) # if so, then append it to the final list we'll return
        arr = np.array(arr) # to handle a list of strings
        return arr

    def average(self, property):
        arr =[]
        arr = self.parse(property)
        names_in_ascii = []
        if property == "average" or property == "id":
            arr = self.parse(property)
            print("The average value of the property: " + str(property) + "," + " is: " + str(np.average(arr)))
        if property == "name":
            for word in arr: # for every name(word) in list of names
                if word.isalpha():  # checks if name(word) is alphabetic before converting to ascii
                    for letter in word: # for every letter in name
                        number = ord(letter) - 96 #convertion to ascii
                        names_in_ascii.append(number)
            print("The average value of the property: "
                  + str(property) + "," + " is: " + str(round(np.average(names_in_ascii),4)))

    def min(self, property):
        arr = []
        arr = self.parse(property)
        if property == "name":
            arr = np.array(arr, dtype=object)  # to handle strings list
        print("The min value of the property: " + str(property) + "," + " is: " + str(np.min(arr)))

    def max(self, property):
        arr = []
        arr = self.parse(property)
        if property == "name":
            arr = np.array(arr, dtype=object)  # to handle strings list
        print("The max value of the property: " + str(property) + "," + " is: " + str(np.max(arr)))

    def total(self, property):
        arr = []
        arr = self.parse(property)
        if property == "name":
            arr = np.array(arr, dtype=object) # to handle strings list
        print("The total value of the property: " + str(property) + "," + " is: " + str(np.sum(arr)))

def check_if_file_exists():
    if not os.path.isfile(fileName):
        raise MatrixException("File doesn't exist")

with open(fileName, 'r') as file:  # since file exists, open it
    file_data = file.read()        # taking the read data and save it as a string line
converted_data = json.loads(file_data) # converting the JSON type data string into a python string
ob = Matrix(converted_data) # creating an instande object of a Matrix class with given data file

def property_options():
    while True:
        option = input("Please enter a property to send the method:\n"
                       "1 for 'average'\n2 for 'id'\n3 for 'name'\n4 for 'typing a new one'\n5 for end\n")
        print(f'You chose option number: {option}')
        if option == '1': return "average"
        elif option == '2': return "id"
        elif option == '3': return "name"
        elif option == '4':
            temp = input("please enter a property\n")
            if temp != "average" and temp != "id" and temp != "name": # checks if giving
                                                                      # property is not 1 of the 3 that it'd be
                print(temp)
                raise MatrixException("Property is invalid")   # if it ain't 1 of the 3, then throw our exception
            else: return str(temp)  # if you chose to type by your own an existing property, then return that value
        elif option == '5': return '5'    # pressing 5 to exit the program
1

def method_options(argument): # argument gets the Property string value returning from property_options() that we chose
    print(f'You entered the property: {argument}')
    method = input("Please choose a method for your property:\n"
                  "1 for 'max'\n2 for 'min'\n3 for 'average'\n4 for 'total'\n")
    if method == '1': ob.max(argument)
    elif method == '2': ob.min(argument)
    elif method == '3': ob.average(argument)
    elif method == '4': ob.total(argument)

def menu():
    try:
        check_if_file_exists()
        while True:
            property_option = property_options() # gets the Property string value that we chose
            if property_option != '5':
                method_options(property_option)  # sending the Property to the
                                                 # methods_options() to choose what method we want
            else: break
    except MatrixException as e:
        print(e.message)
menu()

file.close()
