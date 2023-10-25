#code for KBC
x=int(input("enter question number 1:"))
sum=0
if x==1:
        print("Question 1:")
        print("Thomas Cup is related to which among the following sports?")
        a=input("do you want options? yes/no:")
        if a=="yes":
            print("[A] Table Tennis \n [B] Lawn Tennis \n [C] Badminton \n [D] Golf")
            b=input("enter your option:")
            if b=="c":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                print("YOU HAVE WON 1000/-")
                sum=1000
            else:
                print("YOU GAVE WRONG ANSWER")
                sum=0   
        else:
            c=input("enter your answer:")
            if c=="badminton":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                print("YOU HAVE WON 1000/-")
                sum+=1000
            else:
                print("YOU GAVE WRONG ANSWER")
                sum=sum+0
x=int(input("enter question number 2:"))
if x==2:
        print("Question 2:")
        print("What is the approximate maximum weight of Golf Ball as per Rules of Golf?")
        a=input("do you want options? yes/no:")
        if a=="yes":
            print("[A] 20 gms \n[B] 25 gms \n[C] 40 gms \n[D] 45 gms")
            b=input("enter your option:")
            if b=="d":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                sum=sum+1000
                print("YOU HAVE WON 1000/-")
            else:
                print("YOU GAVE WRONG ANSWER:")
                sum=sum+0
        else:
           c=input("enter your answer:")
           if c=="45":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                sum=sum+1000
                print("YOU HAVE WON 1000/-")
           else:
                print("YOU GAVE WRONG ANSWER:")
                sum=sum+0

x=int(input("enter question number 3:"))
if x==3:
        print("Question 3:")
        print("Which among the following was the venue of first South Asian Games?")
        a=input("do you want options? yes/no:")
        if a=="yes":
            print("[A] Kathmandu \n[B] Dhaka \n[C] Colombo \n[D] New Delhi")
            b=input("enter your option:")
            if b=="a":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                sum=sum+1000
                print("YOU HAVE WON 1000/-")
            else:
                print("YOU GAVE WRONG ANSWER:")
                sum=sum+0
        else:
            c=input("enter your answer:")
            if c=="kathmandu":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                sum=sum+1000
                print("YOU HAVE WON 1000/-")
            else:
                print("YOU GAVE WRONG ANSWER:")
                sum=sum+0
x=int(input("enter question number 4:"))
if x==4:
        print("Question 4:")
        print("What is the duration of a Test Match?")
        a=input("do you want options? yes/no:")
        if a=="yes":
            print("[A] 3 days \n[B] 4 days \n[C] 1 day \n[D] 5 days")
            b=input("enter your option:")
            if b=="d":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                sum=sum+1000
                print("YOU HAVE WON 1000/-")
            else:
                print("YOU GAVE WRONG ANSWER:")
                sum=sum+0
        else:
            c=input("enter your answer:")
            if c=="5":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                sum=sum+1000
                print("YOU HAVE WON 1000/-")
            else:
                print("YOU GAVE WRONG ANSWER:")
                sum=sum+0
x=int(input("enter question number 5:"))
if x==5:
        print("Question 5:")
        print("“National Football Museum” which keeps FIFA collection is located in which country?")
        a=input("do you want options? yes/no:")
        if a=="yes":
            print("[A] Switzerland \n[B] Canada \n[C] England \n[D] France")
            b=input("enter your option:")
            if b=="c":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                sum=sum+1000
                print("YOU HAVE WON 1000/-")
            else:
                print("YOU GAVE WRONG ANSWER:")
                sum=sum+0
        else:
            c=input("enter your answer:")
            if c=="england":
                print("CONGRULATIONS YOU GAVE RIGHT ANSWER!!")
                print("YOU HAVE WON 1000/-")
                sum=sum+1000
            else:
                print("YOU GAVE WRONG ANSWER:")
                sum=sum+0
print("amount won by you:",sum)
if sum==5000:
    print("YOU ARE WINNER!")
    print("5000/- IS YOURS")
elif sum==4000:
    print("YOU WON ONLY 4000/-")
elif sum==3000:
    print("YOU WON ONLY 3000/-")
elif sum==2000:
    print("YOU WON ONLY 2000/-")
elif sum==1000:
    print("YOU WON ONLY 1000/-")
else:
    print("BEST LUCK NEXT TIME")
    print("YOU WON ONLY EXPERINCE")









            
    
