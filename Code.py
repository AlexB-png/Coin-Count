#define variables#
bag=0
value=0
fail=0
correct = True
#Input Parameters
person = input("What is the voulenteers name?")
typecoin = input("What type of coin is it")
weight = input("What is the weight of the coins?")

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
            if weight % 12 != 0:
                print("FAIL")
                correct = False
            else:
                print("It is all £2 coins")
        
        case "£1":
            bag=20
            value=1
            if weight % 8.75 != 0:
                print("FAIL")
                correct = False
            else:
                print("It is all £1 coins")

        case "50p":
            bag = 10
            value = 0.5
            if weight % 8 != 0:
                print("FAIL")
                correct = False
            else:
                print("It is all 50p coins")

        case "20p":
            bag = 10
            value = 0.2
            if weight % 5 != 0:
                print("FAIL")
                correct = False
            else:
                print("It is all 20p coins")
        case "10p":
            bag = 5
            value = 0.1
            if weight % 6.50 != 0:
                print("FAIL")
                correct = False
            else:
                print("It is all 10p coins")
        case "5p":
            bag = 5
            value = 0.05
            if weight % 2.35 != 0:
                print("FAIL")
                correct = False
            else:
                print("It is all 5p coins")
        case "2p":
            bag = 1
            value = 0.02
            if weight % 7.12 != 0:
                print("FAIL")
                correct = False
            else:
                print("It is all 2p coins")
        case "1p":
            bag = 1
            value = 0.01
            if weight % 3.56 != 0:
                print("FAIL")
                correct = False
            else:
                print("It is all 1p coins")
        case _:
            print("Misinput detected / Coin type not detected")
            fail = 1
            print("reinput to fix the issue")
