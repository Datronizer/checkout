# Task: We want to create a checkout system that's threefold:
#   1. Allows checkin/checkout of cables/headphones in the lab
#   2. Shows current inventory
#   3. Assigns a card swipe and name to an item being borrowed

# Update 0.0: File created. Simple checkin/checkout system seems to work.
# Update 0.1: Have a log system that tracks when someone checks in and out
# Update 0.2: Make the Inventory class directly change the inventory count so that it is consistent even after the code exits

import csv
import sys
import datetime
import os

class Inventory:
    def __init__(self, dictionaryofthings):
        self.dictionaryofthings = dictionaryofthings

    def showInventory(self):
        print("Here are the items we currently have:")
        print(" ======= Current Inventory ======= ")
        for item, count in self.dictionaryofthings.items():
            print("{:>22}: {} ".format(item, count))
        print("")

    def lendItem(self, requesteditem):
        requesteditemcount = self.dictionaryofthings.get(requesteditem) # Just to make things more readable
        if requesteditemcount > 0:
            self.dictionaryofthings.update({requesteditem: requesteditemcount-1})
            print("The item you requested has now been borrowed.")
            print("Please let the front desk staff know. Thank you!\n")

    def readdItem(self, requesteditem):
        requesteditemcount = self.dictionaryofthings.get(requesteditem)
        self.dictionaryofthings.update({requesteditem: requesteditemcount+1})
        print("Thank you for returning this item. Have a great day!\n")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def loadcsvOntoDict(filename):
    loadeddict = {}
    with open(os.path.join(__location__, filename), "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            loadeddict.update({row['items']: int(row['count'])})
        csvfile.close()
    return loadeddict

def infoPrompt():
    name = input("Please enter your name: ")
    uid = input("Please enter your USF ID: ")
    item = input("Enter the name of the item (case-sensitive): ")
    return str(name), str(uid), str(item)

def appendToLog(filename, name, uid, requesteditem, time, status):
    with open(os.path.join(__location__, filename), "a", newline = "") as log:
        logwriter = csv.writer(log)
        logwriter.writerow([name, uid, requesteditem, time, status])
        log.close()

def main():
    loadeddict = loadcsvOntoDict("SGCS_inventory.csv")
    inventory = Inventory(loadeddict)

    sessiondone = False
    while sessiondone == False:
        print(""" ====== SGCS Lending System ======
        1. Show current inventory
        2. Borrow an item
        3. Return an item
        4. Exit
              """)
        choice = int(input("Enter Choice: "))
        if choice == 1:
            inventory.showInventory()

        if choice == 2:
            prompt = infoPrompt()
            inventory.lendItem(prompt[2])
            appendToLog("checkout_log.csv", prompt[0], prompt[1], prompt[2], datetime.datetime.now(), "Borrow")

        if choice == 3:
            prompt = infoPrompt()
            inventory.readdItem(prompt[2])
            appendToLog("checkout_log.csv", prompt[0], prompt[1], prompt[2], datetime.datetime.now(), "Return")

        if choice == 4:
            print("Thank you for using our service!")
            sessiondone = True
            sys.exit()

main()
