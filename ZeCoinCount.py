#Function for top of the screen#
def UI():
    print("______________________________________________________________")
    print("                           Coin Count                         ")

#function for end of sequence#
def endUI():
    print("                Thank you for using coin count!                ")
    print("______________________________________________________________")

#importing as required#
import os

#define variables#
bag=0
value=0
fail=0
correct = False
Major = True
wrongtype = False
strange=0
person=0
typecoin=0
weight=0
coin =0
volunteernumber = False
content1=True
content2=True
content3=True

#Clears the terminal#
os.system("CLS")

#This will add the UI back after terminal cleared#
UI()

#This will open OR create a file depending on the volunteer#
volunteernumb= input("What is your volunteer code \n")
volunteernumb = volunteernumb.upper()

directory = r"Coin-Count "+volunteernumb
os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist


#The volunteer code is their name#

#Clears the volunteer number so someone doesn't steal it#
os.system("CLS")

#Brings back the UI#
UI()

#Converts volunteer number to an integer / Preventing an error#
try:
    
    volunteernumber=True
    totalfile=volunteernumb
except:
    print("Strange error")

#Checks if the volunteer number is valid#
if volunteernumber == True:
    successbags = totalfile+"success.txt" #Amount of successful bags#
    totalbags = totalfile+"total.txt"   #total of attempts#
    totalfile = totalfile+".txt" #Entire text file'
    
    successbags = directory+"/"+successbags
    totalbags = directory+"/"+totalbags
    totalfile = directory+"/"+totalfile
    
    #Gives the option to read the text file or whether to add to the file#
    choice = input("Would you like the CONTENTS or to ADD \n")
    choice = choice.upper()
    #Clears the terminal#
    os.system("CLS")
    
    #Will allow the volunteer to see the text file#
    if choice == "CONTENTS":
        #Will print a UI#
        UI()
        
        #Will open the text files for writing / creating new files to prevent an error#
        try:
            test=open(successbags,"x")
            notexist=1
        except:
            print("volunteer code found")
        try:
            test2=open(totalbags,"x")
        except:
            print(".")
        try:
            test3=open(totalfile,"x")
        except:
            print(".")
        
        
        
        try:
            entire=open(totalfile,"r")
            test=entire.read()
            if test=="":
                print("Have you counted any coins?")
        except:
            print("Have you even counted any coins?")
        try:
            success=open(successbags,"r")
            test2=success.read()

        except:
            print("")
        try:
            total=open(totalbags,"r")
            test3=total.read()
        except:
            print("")
        
        #This will fix an error when trying to read from an empty file#
        x=0
        
        entire = open(totalfile,"r")
        total = open(totalbags,"r")
        success = open(successbags,"r")


        x=entire.read()
        
        if x=="":
            
            content1=False
        x=0
        
        x=total.read()
        if x=="":
            content2=False
            
        x=0
        
        x=success.read()
        if x=="":
            content3=False
            
        
        #Prints the contents of 1.txt and calculates an average ( 1success.txt / 1total.txt )
        
        #This was the only way i could get the code to not return an error
        entire.close()
        total.close()
        success.close()
        total=open(totalbags,"r")
        success=open(successbags,"r")
        entire=open(totalfile,"r")
        
        
        if content1 !=False:
            print(entire.read())
            
        if content2 != False and content3 != False:
            successfull = success.read() #Successful#
            faill = total.read() #failures#
            
            faill=int(faill)
            successfull=int(successfull)
            print("The average is",(successfull/faill)*100,"%")
    
    #If choice was to add a coin bag to the text file#
    elif choice == "ADD":
        entire = open(totalfile,"a")
        g=open(successbags,"a")
        h= open(totalbags,"a")
        
        #adds the UI back after terminal cleared
        UI()

        #Input Parameters
        person = input("What is the volunteers name? \n")
        typecoin = input("What type of coin is in the bag \n")
        weight = input("What is the weight of the bag? \n")

        #Check that the weight is an integer#
        try:
            weight = float(weight)
        except:
            print("Failure converting weight to integer")
            fail = 1

        #Checks whether the type of coin is correct and if the weight is correct#
        if fail != 1:  
            match typecoin:
                
                case "£2":
                    bag=20
                    value=2
                    coin= 12
                    expect = 120
                    if weight % 12 != 0:
                        
                        correct = False
                    else:
                        
                        correct = True        
                case "£1":
                    bag=20
                    value=1
                    coin = 8.75
                    expect = 175
                    if weight % 8.75 != 0:
                        
                        correct = False
                    else:
                        
                        correct = True
                case "50p":
                    bag = 10
                    value = 0.5
                    coin = 8
                    expect = 160
                    if weight % 8 != 0:
                        
                        correct = False
                    else:
                        
                        correct = True
                case "20p":
                    bag = 10
                    value = 0.2
                    coin = 5
                    expect = 250
                    if weight % 5 != 0:
                        
                        correct = False
                    else:
                        
                        correct = True
                case "10p":
                    bag = 5
                    value = 0.1
                    coin = 6.5
                    expect = 325
                    if weight % 6.50 != 0:
                        
                        correct = False
                    else:
                        
                        correct = True
                case "5p":
                    bag = 5
                    value = 0.05
                    coin = 2.35
                    expect = 235
                    if weight % 2.35 != 0:
                        
                        correct = False
                    else:
                        print("Its all 5p coins")
                        correct = True
                case "2p":
                    bag = 1
                    value = 0.02
                    coin = 7.12
                    expect = 356
                    if weight % 7.12 != 0:
                        
                        correct = False
                    else:
                        print("It is all 2p coins")
                        correct = True
                case "1p":
                    bag = 1
                    value = 0.01
                    coin = 3.56
                    expect =356
                    if weight % 3.56 != 0:
                        
                        correct = False
                    else:
                        print("It is all 1p coins")
                        correct = True
                case _:
                    print("Misinput detected / Coin type not detected")
                    Major = False
                    fail =1
                    print("reinput to fix the issue")


        if fail != 1:
            wrongtype = False
            #major will equal True if there is a completely **incorrect coin type** and it will not run#
            while Major != False :
                if weight == expect:
                    correct = True
                else:
                    incorrect=weight
                    while incorrect > coin:
                        print(incorrect)
                        incorrect = incorrect - coin
                    wrong2 = incorrect

                
                

            #This will tell you what coins are missing or if there are too many#
            
            if weight != expect:
                print("Something is wrong")
                strange = expect - weight
                strange = strange / coin
                if strange % 1 == 0:
                    if strange < 0:
                        print("You have",strange * -1,"too many coins")
                        uhoh = f"{person} made a mistake //   They had {strange} too many coins   //   The type of coin was {typecoin} with a weight of {weight} grams \n"
                    else:
                        print("You have",strange,"too few coins")
                        uhoh = f"{person} made a mistake //   They had {strange} too few coins   //   The type of coin was {typecoin} with a weight of {weight} grams \n"
                    if strange != 0:
                        entire.write(uhoh)

            #This is the part where each mistake is tallied up
            if wrongtype == True:
                uhoh = f"{person} made a mistake   //   Their total was off by {wrong2} grams   //   The type of coin was {typecoin} with a weight of {weight} grams \n"
                entire.write(uhoh)
            
            #It increments the 1.txttotal to calculate an average#
            #Reminder that if you mess with this it will never work again#
            fix=False
            att=0
            total=open(totalbags,"r")
            x=total.read()
            if x=="":
                total.close()
                h=open(totalbags,"w")
                h.write("1")
                fix=True
            if fix == False:
                x= int(x)
                total.close()
                h=open(totalbags,"w")
                x += 1
                x= str(x)
                h.write(x)
                total.close()
            

            #This bit will increment if it is successful and will write to the text file that they did it right#
            if wrongtype != True and correct == True and strange == 0:
                fix=False
                att=0
                success=open(successbags,"r")
                x=success.read()
                if x=="": #Will return true if the text file is empty
                    success.close()
                    g=open(successbags,"w") #reopens file to write instead of read#
                    g.write("1") #If file is empty then it will add 1 to the text file#
                    fix=True
                if fix == False: #If the text file is not empty#
                    x= int(x) #converts the returned string to an integer so it can be incremented#
                    success.close() #closes the file for reading#
                    g=open(successbags,"w") #opens file for writing#
                    x += 1 #Integer is incremented#
                    x= str(x) #Converts integer to string so it can be written to the text file#
                    g.write(x)
                    success.close()
                yess=f"{person} did something right!   //   The coins weighed {weight}   //   They weighed {typecoin} coins \n" #Writes success to the text file
                
                entire.write(yess)
                
                
            
            
    else:
        print("Invalid Input ( ADD or CONTENTS )")

#Prints the end UI#
endUI()

