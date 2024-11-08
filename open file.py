f= open("volunteer.txt","a")
name= input("What is your name?")
bags= int(input("How many correct bags have you made"))
bad = int(input("How many mistakes?"))
percent=str((bags/bad)) + "%"
a = name +","+ str(bags) +","+ str(bad) +","+ str(percent)
print(a)
f.write(a + "\n")
f.close()
