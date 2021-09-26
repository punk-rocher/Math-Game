#Declare varaiables
import random #To get numbers
import mysql.connector

name=""
ans=""

def Easy_game_mode():
        print("#----------Easy_game_mode----------#")
        print()
        name=input("Enter user Name :")
        q_count = int(input("How many questions you need :"))
        names=[]
        tot=0
        score=0
        numofq=5
        precentage=0

        for i in range(0,q_count):
            num1=random.randrange(1,10)
            num2=random.randrange(1,10)
            ans=int(input(str(num1)+" "+"+"+" "+str(num2)+"="+" "))
            q=num1+num2
            
            
            if (ans==q):
                names.append(str(num1)+" "+"+"+" "+str(num2)+"="+str(ans)+"  "+"is correct")
                tot=tot+1
                
                
            else:
                names.append(str(num1)+" "+"+"+" "+str(num2)+"="+str(ans)+"  "+"is incorrect"+" "+"correct answer is="+str(q))

            while (ans==q):
                ans=score
                score=score+1

        print("<<<<<<<<<<.Game result.>>>>>>>>>>")
        for answer in names:
            precentage=(tot/numofq)*100
            print(answer)
        print("correct answers",tot,"out of",numofq)
        print("you have got",score,"points")
        print("precentage=",int(precentage),"%")
        print("____THANK___YOU___")

        conDict = {"host":"localhost","user":"root","password":"","database":"math_game"}
    
        try:
                db = mysql.connector.connect(**conDict)
                print("Connection Successful")
                cursor = db.cursor()
                try:
                    mySQLtxt = "INSERT INTO sample (player,correctquestions,totalquestions,precentage) VALUES (%s,%s,%s,%s)"
                    myValues = (name, tot, numofq, precentage)
                    cursor.execute(mySQLtxt,myValues)
                    db.commit()
                    print(cursor.rowcount, "Record added to Database")
                except:
                    print("Error ocuurs in inserting data")
                db.close()
        except:
                print("Connection Fails")

    
