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
        letter_tuple_asci = {}
        name_in_asci_tuples=[]
        names_in_asci = []
        flag = 0
        if property == "average" or property == "id":
            arr = self.parse(property)
            print("The average value of the property: " + str(property) + "," + " is: " + str(np.average(arr)))
        if property == "name":
            for word in arr: # for every name in arr of names
                if word.isalpha():  # checks if letter is alphabetic before converting to asci
                    ob_temp = Matrix(names_in_asci)
                    for letter in word: # for every letter in name
                        number = ord(letter) - 96 #convertion to asci
                        print(str(letter) + " in asci:" + str(number))
                        letter_tuple_asci.update({"name": number})
                        name_in_asci_tuples.append(letter_tuple_asci) #append asci value for each letter of name to a list
                    print(name_in_asci_tuples)
                    ob_temp = Matrix(name_in_asci_tuples)
                    names_in_asci.append(str({"name":ob_temp.total("name")}))
                    print("bla"+ str(names_in_asci))

            # ob_temp_final = Matrix(names_in_asci)
            # ob_temp_final.average("name")
            print("asd")




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
ob.total("name")

# except MatrixException as e:
#     print(e.message)
#
# finally:
file.close()