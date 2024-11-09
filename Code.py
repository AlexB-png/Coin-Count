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

os.system("CLS")

#This will open or create a file depending on the volunteer#
x= input("What is your volunteer number \n")
try:
    int(x)
    volunteernumber=True
except:
    print("Failure verifying volunteer NUMBER >:(")


if volunteernumber == True:
    y = x+"success" #Amount of successful bags#
    z = x+"total"   #total of attempts#
    x = x+".txt" #Entire text file'

    choice = input("Would you like the CONTENTS or to ADD \n")

    os.system("CLS")

    if choice == "CONTENTS":
        f=open(x,"r")
        g=open(y,"r")
        h= open(z,"r")

        print(f.read())
        successfull = g.read() #Successful#
        faill = h.read() #failures#
        successfull=int(successfull)
        faill=int(faill)
        
        print("The average is",(successfull/faill)*100,"%")
    else:
        f = open(x,"a")
        g=open(y,"a")
        h= open(z,"a")
        
        #Input Parameters
        person = input("What is the volunteers name? \n")
        typecoin = input("What type of coin is in the bag \n")
        weight = input("What is the weight of the bag?")

        #Check that the weight is an integer#
        try:
            weight = int(weight)
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
                        print("FAIL")
                        correct = False
                    else:
                        print("It is all £2 coins")
                        correct = True        
                case "£1":
                    bag=20
                    value=1
                    coin = 8.75
                    expect = 175
                    if weight % 8.75 != 0:
                        print("FAIL")
                        correct = False
                    else:
                        print("It is all £1 coins")
                        correct = True
                case "50p":
                    bag = 10
                    value = 0.5
                    coin = 8
                    expect = 160
                    if weight % 8 != 0:
                        print("FAIL")
                        correct = False
                    else:
                        print("It is all 50p coins")
                        correct = True
                case "20p":
                    bag = 10
                    value = 0.2
                    coin = 5
                    expect = 250
                    if weight % 5 != 0:
                        print("FAIL")
                        correct = False
                    else:
                        print("It is all 20p coins")
                        correct = True
                case "10p":
                    bag = 5
                    value = 0.1
                    coin = 6.5
                    expect = 325
                    if weight % 6.50 != 0:
                        print("FAIL")
                        correct = False
                    else:
                        print("It is all 10p coins")
                        correct = True
                case "5p":
                    bag = 5
                    value = 0.05
                    coin = 2.35
                    expect = 235
                    if weight % 2.35 != 0:
                        print("FAIL")
                        correct = False
                    else:
                        print("It is all 5p coins")
                        correct = True
                case "2p":
                    bag = 1
                    value = 0.02
                    coin = 7.12
                    expect = 356
                    if weight % 7.12 != 0:
                        print("FAIL")
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
                        print("FAIL")
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
            while Major != False and correct == False:
                wrong = weight
                while wrong > coin:
                    wrong -= coin
                os.system("CLS")
                print("The coin stack is off by",wrong,"grams")
                wrongtype= True
                
                break

            #This will tell you what coins are missing or if there are too many#
            
            if weight != expect:
                strange = expect - weight
                strange = strange /12
                if strange % 1 == 0:
                    if strange < 0:
                        print("You have",strange * -1,"too many coins")
                        uhoh = f"{person} made a mistake //   They had {strange} too many coins   //   The type of coin was {typecoin} with a weight of {weight} grams \n"
                    else:
                        print("You have",strange,"too few coins")
                        uhoh = f"{person} made a mistake //   They had {strange} too few coins   //   The type of coin was {typecoin} with a weight of {weight} grams \n"
                    if strange != 0:
                        f.write(uhoh)

            





            #This is the part where each mistake is tallied up
            if wrongtype == True:
                uhoh = f"{person} made a mistake   //   Their total was off by {wrong} grams   //   The type of coin was {typecoin} with a weight of {weight} grams \n"
                f.write(uhoh)
            
            
            
            
            #DO NOT TOUCH UNDER ANY CIRCUMSTANCE#
            #It increments the 1.txttotal to calculate an average#
            
            fix=False
            att=0
            h=open(z,"r")
            x=h.read()
            if x=="":
                h.close()
                h=open(z,"w")
                h.write("1")
                fix=True
            if fix == False:
                x= int(x)
                h.close()
                h=open(z,"w")
                x += 1
                x= str(x)
                h.write(x)
                h.close()

            #This bit will increment if it is successful#
            if wrongtype != True and correct == True and strange == 0:
                fix=False
                att=0
                g=open(y,"r")
                x=g.read()
                if x=="":
                    g.close()
                    g=open(y,"w")
                    g.write("1")
                    fix=True
                if fix == False:
                    x= int(x)
                    g.close()
                    g=open(y,"w")
                    x += 1
                    x= str(x)
                    g.write(x)
                    g.close()
                yess=f"{person} did something right!   //   The coins weighed {weight}   //   They weighed {typecoin} coins"
                print("Success!!")
                f.write(yess)
            
            #LEAVE THIS ALONE#


