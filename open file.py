error =0
f= open("volunteer.txt","a")
name= input("What is your name?")
bags= input("How many correct bags have you made")
try:
    int(bags)
except:
    print("error")
    error=1
bad =input("How many mistakes?")
try:
    int(bad)
except:
    print("error")
    error=1
if error != 1:
    percent=str((int(bags)/int(bad))) + "%"
    a = name +","+ str(bags) +","+ str(bad) +","+ str(percent)
    print(a)
    f.write(a + "\n")
    f.close()
