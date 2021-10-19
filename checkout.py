# Task: We want to create a checkout system that's threefold:
#   1. Allows checkin/checkout of cables/headphones in the lab
#   2. Shows current inventory
#   3. Assigns a card swipe and name to an item being borrowed

# Update 0.0: File created. Simple checkin/checkout system seems to work.
# Update 0.1: Have a log system that tracks when someone checks in and out
# Update 0.2: Make the Inventory class directly change the inventory count so that it is consistent even after the code exits
# Update 0.3: Made the interface more readable with clearTerminal() and integrated a login loop

import csv, datetime, getpass, os, sys, time
#
# class Inventory:
#     def __init__(self, dictionaryofthings):
#         self.dictionaryofthings = dictionaryofthings
#
#     def showInventory(self):
#         print("Here are the items we currently have:")
#         print(" ======= Current Inventory ======= ")
#         for item, count in self.dictionaryofthings.items():
#             print("{:>22}: {} ".format(item, count))
#         print("")
#
#     def lendItem(self, requesteditem):
#         requesteditemcount = self.dictionaryofthings.get(requesteditem) # Just to make things more readable
#         print('{} {}'.format(requesteditem, requesteditemcount))
#         if requesteditemcount > 0:
#             self.dictionaryofthings.update({requesteditem: requesteditemcount-1})
#             print("The item you requested has now been borrowed.")
#             print("Please let the front desk staff know. Thank you!\n")
#
#     def readdItem(self, requesteditem):
#         requesteditemcount = self.dictionaryofthings.get(requesteditem)
#         self.dictionaryofthings.update({requesteditem: requesteditemcount+1})
#         print("Thank you for returning this item. Have a great day!\n")
#
# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))
#
# class Operations:
#     def __init__(self):
#         pass
#
#     def loadcsvOntoDict(self, filename):
#         self.filename = filename
#         loadeddict = {}
#         with open(os.path.join(__location__, self.filename), "r") as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 loadeddict.update({row['items']: int(row['count'])})
#             csvfile.close()
#         return loadeddict
#
#     def infoPrompt(self):
#         self.name = input("Please enter your name: ")
#         self.uid = input("Please enter your USF ID: ")
#         self.item = input("Enter the name of the item (case-sensitive): ")
#         return str(self.name), str(self.uid), str(self.item)
#
#     def appendToLog(self, filename, name, uid, requesteditem, time, status):
#         with open(os.path.join(__location__, filename), "a", newline = "") as log:
#             logwriter = csv.writer(log)
#             logwriter.writerow([name, uid, requesteditem, time, status])
#             log.close()
#
# # def loadcsvOntoDict(filename):
# #     loadeddict = {}
# #     with open(os.path.join(__location__, filename), "r") as csvfile:
# #         reader = csv.DictReader(csvfile)
# #         for row in reader:
# #             loadeddict.update({row['items']: int(row['count'])})
# #         csvfile.close()
# #     return loadeddict
# #
# # def infoPrompt():
# #     name = input("Please enter your name: ")
# #     uid = input("Please enter your USF ID: ")
# #     item = input("Enter the name of the item (case-sensitive): ")
# #     return str(name), str(uid), str(item)
# #
# # def appendToLog(filename, name, uid, requesteditem, time, status):
# #     with open(os.path.join(__location__, filename), "a", newline = "") as log:
# #         logwriter = csv.writer(log)
# #         logwriter.writerow([name, uid, requesteditem, time, status])
# #         log.close()
#
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def borrowItem():
    pass

def returnItem():
    pass

def checkInventory():
    pass

def logUser():
    pass

def login():
    global loggedin
    loggedin = False
    print('''
      ======== SGCS Checkout System ========
    Hello! Welcome to the SGCS Checkout System.
    Please sign in before using our services.
    ''')

    user_name = input('Full name: ')
    while user_name.strip() == '':
        print('Name cannot be empty. Try again.')
        user_name = input('Full name: ')

    user_email = input('USF email: ').strip() # takes input and process it
    substring = '@usf.edu'
    while substring not in user_email or user_email == '':
        print('Invalid format. Try again.')
        user_email = input('USF email: ')

    card_swipe = getpass.getpass(prompt='Please swipe your USF ID: ')

    loggedin = True
    return user_name, user_email, card_swipe, loggedin #figure out what to do with this

def letmein():
    global loggedin
    if loggedin == True:
        clearTerminal()
        main()

def main():
    # do = Operations()
    # loadeddict = do.loadcsvOntoDict("SGCS_inventory.csv")
    # print(loadeddict)
    # inventory = Inventory(loadeddict)
    global loggedin

    clearTerminal()
    sessiondone = False
    while sessiondone == False:
        clearTerminal()
        print('''
     ======= SGCS Checkout System =======
    Hello! Welcome to the SGCS Checkout System.
    What can I do for you today?
     ====================================
    1. Borrow an item
    2. Return an item
    3. Check current inventory
    4. Logout
         ''')
        choice = int(input("Enter Choice: "))
        if choice == 1:
            borrowItem()
            # inventory.showInventory()
            pass

        if choice == 2:
            returnItem()
            # prompt = do.infoPrompt()
            # inventory.lendItem(prompt[2])
            # do.appendToLog("checkout_log.csv", prompt[0], prompt[1], prompt[2], datetime.datetime.now(), "Borrow")
            pass

        if choice == 3:
            checkInventory()
            # prompt = do.infoPrompt()
            # inventory.readdItem(prompt[2])
            # do.appendToLog("checkout_log.csv", prompt[0], prompt[1], prompt[2], datetime.datetime.now(), "Return")
            pass

        if choice == 4:
            clearTerminal()
            login()

        if choice == 1638:
            print("Thank you for using our service!")
            sessiondone = True
            sys.exit()

clearTerminal()
login()
letmein()
# main()
#
# for i in range(10):
#     print(i)
#     time.sleep(2)
#     clearTerminal()
