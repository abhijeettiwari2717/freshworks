#import threading
#from threading import Thread, Lock
# I build below code on python 3.8.1, use import thread for python2.0 versions....
import time
import json

data= {}  # dictionary in which we store data

#syntax to RUN below create code create(key_name,value)
def create(key, value, timeout=0):
    if key in data:
        print("SORRY! This key already exist")
    else:
        if (key.isalpha()):
            if len(data) < (1024 * 1020 * 1024) and value <= (
                    16 * 1024 * 1024):
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                if len(key) <= 32:
                    data[key] = l
                    print("Congratulations! Your key-value created successfully!")

                    with open('data.txt', 'w') as outfile:
                        json.dump(data, outfile)
            else:
                print("OOPS! Memory limit exceeded!! ")
        else:
            print(
                "OOPS! Invalind keyName, keyName must contain only alphabets and no special characters or numbers")

#syntax to RUN below read code "read(key_name)"
def read(key):
    if key not in data:
        print("SORRY! Given key does not exist in database. Please enter a valid key")
    else:
        b = data[key]
        if b[1] != 0:
            if time.time() < b[1]:
                stri = str(key) + ":" + str(
                    b[0])
                print(stri)
                return stri
            else:
                print("OOPS! time to live for", key, "has expired")
        else:
            stri = str(key) + ":" + str(b[0])
            print(stri)
            return stri

#syntax to RUN below delete code "delete(key_name)"
def delete(key):
    if key not in data:
        print("SORRY! Given key does not exist in database. Please enter a valid key")
    else:
        b = data[key]
        if b[1] != 0:
            if time.time() < b[1]:
                del data[key]
                print("GREAT! Your key is successfully deleted")
            else:
                print("OOPS! time to live for", key, "has expired")
        else:
            del data[key]
            print("GREAT ! Your key is successfully deleted")

#syntax to RUN below update code "update(key_name,new_value)"
def update(key, value):
    b = data[key]
    if b[1] != 0:
        if time.time() < b[1]:
            if key not in data:
                print("OOPS! Given key does not exist in database. Please enter a valid key")
            else:
                l = []
                l.append(value)
                l.append(b[1])
                data[key] = l
                print("Success! Your key updates successfully")
        else:
            print("OOPS! time to live for", key, "has expired")
    else:
        if key not in data:
            print("OOPS! Given key does not exist in database. Please enter a valid key")
        else:
            l = []
            l.append(value)
            l.append(b[1])
            data[key] = l