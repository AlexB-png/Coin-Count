#Function for top of the screen#
def UI():
    print("______________________________________________________________")
    print("                           Coin Count                         ")
#function for end of sequence#
def endUI():
    clear()
    print("")
    print("                Thank you for using coin count!                ")
    print("______________________________________________________________")
def clear(): #This clears the terminal and prints the UI#
    os.system("CLS")
    UI()
def write(): #This is a repeatable way of writing to Master.txt
    with open("Files\MasterFile.txt","a") as Master: Master.write(Write)
def admin():
    with open(f"Volunteer\{volunteer_number}.json", "r") as file:
        Failure=False
        thisdict = json.load(file) #Loads the dictionary#
        Successful_Bags = thisdict["success"] #This is the amount of successful attempts
        Total_Bags = thisdict["total"] #This is the total amount of attempts
        try:efficiency = Successful_Bags / Total_Bags
        except:
            print("You have a 0% efficiency")
            Failure = True
        if Failure != True:
            efficiency*=100 #Makes 1.0 to 100.0#
            math.trunc(efficiency)
            print(f"{volunteer_number} has an efficiency of {efficiency}")
            try: open("Files\Admin.txt","r") #Creates the admin.txt file#
            except: open("Files\Admin.txt","w")
            with open("Files\Admin.txt","a") as admin:
                admin.write("\n")#Writes a new line so there arent multiple results on one line#
                admin.write(f"{volunteer_number} has an efficiency of {efficiency}") #Efficiency > 0#
        else:
            with open("Files\Admin.txt","a") as admin:
                admin.write("\n") #Writes a new line so there arent multiple results on one line#
                admin.write(f"{volunteer_number} has an efficiency of 0") #If efficiency == 0#
        time.sleep(10)
def New_Leader():
    with open(f"Volunteer\{volunteer_number}.json", "r") as file:
        thisdict = json.load(file)
        Total_Attempts = thisdict["total"] #This is the total amount of attempts
    Leading_Score = Old_Leader["efficiency"]
    if Total_Attempts >= 5:
        if Leading_Score > efficiency:
            print("You did not beat the highscore :(") #Nothing changes with leaderboard.json#
            
        elif Leading_Score == efficiency:
            print("You tied the leader!")
            OldLeader.update({"Name":volunteer_number,"efficiency":efficiency})#
            add()
            json.dump(OldLeader,open("Files\LeaderBoard.json","w")) #The leaderboard shows the MOST RECENT leader#
        else:
            clear()
            print("NEW HIGHSCORE")
            print(f"The old leader:{Old_Leader}")
            add()
            json.dump(OldLeader,open("Files\LeaderBoard.json","w"))
            x=json.load(open("Files\LeaderBoard.json","r"))
            print(f"The new leader:{x}") ; time.sleep(5)
    else:
        print("You haven't counted enough bags to be added to the leaderboard <5")



def add():
    OldLeader.update({"Name":volunteer_number,"efficiency":efficiency}) #This adds the new dictionary to a variable so it can be added to the leaderboard#

import os ; import unittest ; import math ; import time ; import json

Float = False
int = False
Fail=False
Failure =  False
#This is the dictionary that shows the expected weights of each coin type#
two_pound = {"coin_weight":12,"expected_weight":120}
one_pound = {"coin_weight":8.75,"expected_weight":175}
fifty = {"coin_weight":8,"expected_weight":160}
twenty= {"coin_weight":5,"expected_weight":250}
ten = {"coin_weight":6.5,"expected_weight":325}
five = {"coin_weight":2.35,"expected_weight":235}
two = {"coin_weight":7.12,"expected_weight":356}
one = {"coin_weight":3.56,"expected_weight":356}
Type_Of_coin = ["two_pound","one_pound","fifty_pence","twenty_pence","ten_pence","five_pence","two_pence","one_pence"]
clear()

#This loops until a valid volunteer number is input#
volunteer_number = ""
while volunteer_number == "":
    volunteer_number=input("What is the volunteer number? \n")
volunteer_number=volunteer_number.upper()
try: #This bit will create the masterfile#
    open("Files\MasterFile.txt","r") 
except: 
    with open("Files\MasterFile.txt","w") as Fix: print("MasterFile has been created")

try: open(f"Volunteer\{volunteer_number}.json","r") #This part creates the volunteer json file#
except: open(f"Volunteer\{volunteer_number}.json","w")

try:
    old = json.load(open(f"Volunteer\{volunteer_number}.json")) #This checks to see if the volunteer file exists#
    print("Success!")
    time.sleep(2)
except:
    print("New to the company?")
    dict = {"success":0,"total":0,"Efficiency":0}
    json.dump(dict,open(f"Volunteer\{volunteer_number}.json","w")) ; time.sleep(3)

clear()

Choice = input("Would you like to ADD or CONTENTS \n")
Choice = Choice.upper()

if Choice == "ADD": #This works with lowercase and uppercase#
    clear()
    Find_Success = False
    while Find_Success != True:
        Coin_type=input("What coin? two_pound , one_pound , fifty_pence , twenty_pence , ten_pence , five_pence ,two_pence , one_pence \n") #loops over a dictionary#
        Coin_type = Coin_type.lower()
        clear()
        for i in Type_Of_coin:
            if i == Coin_type:
                print("Success")
                Find_Success = True
    
    match Coin_type:
        case "two_pound":
            CoinWeight = two_pound["coin_weight"]
            ExpectedWeight=two_pound["expected_weight"]
        case "one_pound":
            CoinWeight = one_pound["coin_weight"]
            ExpectedWeight=one_pound["expected_weight"]
        case "fifty_pence":
            CoinWeight = fifty["coin_weight"]
            ExpectedWeight=fifty["expected_weight"]
        case "twenty_pence":
            CoinWeight = twenty["coin_weight"]
            ExpectedWeight=twenty["expected_weight"]
        case "ten_pence":
            CoinWeight = ten["coin_weight"]
            ExpectedWeight=ten["expected_weight"]
        case "five_pence":
            CoinWeight = five["coin_weight"]
            ExpectedWeight=five["expected_weight"]
        case "two_pence":
            CoinWeight = two["coin_weight"]
            ExpectedWeight=two["expected_weight"]
        case "one_pence":
            CoinWeight = one["coin_weight"]
            ExpectedWeight=one["expected_weight"]
        #CoinWeight is the weight of one coin#
        #ExpectedWeight is the weight of an entire bag#
    Bag_weight = input("What is the weight of the bag")
    try: int(Bag_weight) ; int = True
    except:
        try: float(Bag_weight) ; Float = True
        except: Fail = True ; print("Invalid bag weight") ; time.sleep(5) #The code will end after this#
    if Fail != True:
        if Float == True:
            Bag_weight = float(Bag_weight)
        elif int == True:
            Bag_weight = int(Bag_weight)
        else:
            print("There is an issue with conversion") ; time.sleep(5)
        
        if Bag_weight - ExpectedWeight != 0:    
            clear()
            print("Something is wrong")
            if (Bag_weight-ExpectedWeight)% CoinWeight == 0:
                Strange_Amount=(Bag_weight-ExpectedWeight)/CoinWeight
                if Strange_Amount <=0:
                    Strange_Amount*=-1 
                    Strange_Amount = math.trunc(Strange_Amount) #This removes the decimals from the efficiency#
                    Write=f"{volunteer_number} has {Strange_Amount} too few coins {Coin_type}\n"
                    print(Write)
                    write()
                    admin()
                else: 
                    Write=f"{volunteer_number} has {Strange_Amount} too many coins {Coin_type}\n"
                    print(Write)
                    write()
                    admin()
            else:
                Strange_Amount = Bag_weight - ExpectedWeight
                if Strange_Amount < 0:
                    Strange_Amount*=-1
                    Write = f"{volunteer_number} made a mistake. Your bag is off by {Strange_Amount}g Coin type was {Coin_type}\n"
                    print(Write)
                    write()
                    admin()
                else:
                    Write = f"{volunteer_number} made a mistake. Your bag is over by {Strange_Amount}g Coin type was {Coin_type}\n"
                    print(Write)
                    write()
                    admin()
            
            with open(f"Volunteer\{volunteer_number}.json", "r") as file:
                thisdict = json.load(file)
            Successful_Bags = thisdict["success"] #This is the amount of successful attempts
            Total_Bags = thisdict["total"] #This is the total amount of attempts
            Total_Bags+=1
            thisdict["success"] = Successful_Bags #Reads from the volunteers dictionary#
            thisdict["total"] = Total_Bags #Reads from the volunteers dictionary#
            print(thisdict)
            json.dump(thisdict, open(f"Volunteer\{volunteer_number}.json","w")) #This writes the dictionary to a json file#
        else:
            print("It is all right :)")
            Write = f"{volunteer_number} did something right! {Coin_type} \n" #If the coin weight matches expected weight#
            write()
            with open(f"Volunteer\{volunteer_number}.json", "r") as file:
                thisdict = json.load(file)
            Successful_Bags = thisdict["success"] #This is the amount of successful attempts
            Total_Bags = thisdict["total"] #This is the total amount of attempts
            Total_Bags+=1
            Successful_Bags+=1
            thisdict["success"] = Successful_Bags
            thisdict["total"] = Total_Bags
            print(thisdict)
            json.dump(thisdict, open(f"Volunteer\{volunteer_number}.json","w"))
            admin()
elif Choice=="CONTENTS":
    admin()
else:
    print("Make sure that you input something correct") #
    Fail = True #This is so that it doesn't try to write an empty file to the masterfile#
    time.sleep(2)
endUI()

if Fail == False:
    try: open("Files\LeaderBoard.json","r")
    except: 
        open("Files\LeaderBoard.json","w")
        Board = {"Name":"Admin","efficiency":0}
        json.dump(Board,open("Files\LeaderBoard.json","w"))
    with open("Files\LeaderBoard.json","r") as leaderboard:
        OldLeader = json.load(leaderboard)
        print(f"The old leader was {OldLeader}")
        with open(f"Volunteer\{volunteer_number}.json", "r") as file:
            thisdict = json.load(file)
        Successful_Bags = thisdict["success"] #This is the amount of successful attempts
        Total_Bags = thisdict["total"] #This is the total amount of attempts
        thisdict["success"] = Successful_Bags
        thisdict["total"] = Total_Bags
        try: efficiency = math.trunc((Successful_Bags/Total_Bags)*100)#Calculates the efficiency for writing to leaderboard and volunteer json#
        except: efficiency=0 #If there is a divide by 0 error#
        
        with open("Files\LeaderBoard.json") as leaderboard:
            
            Old_Leader = json.load(leaderboard)#This loads the json file of the leaderboard#
            Leader_Name = Old_Leader["Name"]
            if Leader_Name == volunteer_number:
                print("Welcome back!")
                time.sleep(3)
                clear()
                Leading_Score = Old_Leader["efficiency"]
                print(f"The old leader:{Old_Leader}")
                if Leading_Score > efficiency:
                    print("You've lost some of your efficiency")
                    OldLeader.update({"Name":volunteer_number,"efficiency":efficiency})
                    add()
                    print(f"{OldLeader} is the new leader")
                    json.dump(OldLeader,open("Files\LeaderBoard.json","w"))
                else:
                    New_Leader()
            else:
                New_Leader()

with open(f"Volunteer\{volunteer_number}.json", "r") as file:
    EfficiencyCalc = json.load(file)
    success = EfficiencyCalc["success"]
    total = EfficiencyCalc["total"]
    try: x = math.trunc((success/total)*100)
    except: print("Failed to add efficiency") ; x=0
    NewDict = {"success":success,"total":total,"Efficiency":x}
    json.dump(NewDict,open(f"Volunteer\{volunteer_number}.json","w"))

#This is the testplan that checks for empty files#
with open("Files\MasterFile.txt","r") as master:
        with open(f"Volunteer\{volunteer_number}.json") as volunteer:
            with open("Files\LeaderBoard.json") as Leader:
                with open("Files\Admin.txt","r") as admin:
                    read2=volunteer.read() ; read3=Leader.read() ; read4=admin.read()
class TestJson(unittest.TestCase):
    def test_user(self):
        self.assertNotEqual(read2, "", "The 'Volunteer File' should not be empty.")#This prints if this fails#
        time.sleep(1)
    def test_leaderboard(self):
        self.assertNotEqual(read3, "", "The 'Leaderboard' should not be empty.")#This prints if this fails#
        time.sleep(1)
    def test_Admin(self):
        self.assertNotEqual(read4, "", "The 'Admin'document should not be empty")#This prints if this fails#
if __name__ == '__main__':
    unittest.main()
    unittest.main()
