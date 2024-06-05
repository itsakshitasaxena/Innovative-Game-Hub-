#final project
import random
def func():
    print("\t\t Main Menu \t\t")
    game=["1.) Quiz Game\n","2.) Number Guessing Game\n","3.) Tic-Tac-Toe Game \n"]
    for i in game:
        print(i)
    print("\t**Select a game you want to play at first\t\n")
    an=int(input("Press any key from 1 to 3 to select a game"))
    print(f'You opt for the {game[an-1]}')


    if an==1:
        questions=[["Who is known as filmy kudi?","sharddha arya\t\t\t","shreya mehta","alia bhatt\t\t\t\t","pranali rathore",2],
       ["Capital of Haryana","chattisgrah\t\t\t","Faridabad","Chandigarh\t\t\t","Delhi",3],
       ["Which city is known as Pink City in India?","raipur\t\t\t\t","jaipur","kanpur\t\t\t\t","malyalam",2],
       ["Capital of Australia","Canberra\t\t\t\t","sydney","Berlin\t\t\t\t","Grey city",1],
       ["Full form of ECG","Electrocardiogramophone\t\t","Electroniccargram","Electroniccargramophone\t\t","Electrocardiogram",4],
       ["Which city is known as GREY CITY?","Breadbury\t\t\t","Berlin","Sydney\t\t\t\t","California",2],
       ["What emotion does the phrase 'Phule Na Samana' represent?","sadness\t\t\t\t","happy","angry\t\t\t\t","dizzy",2],
       ["Which of the following states does not border Gujarat?","Maharashtra\t\t\t","MP","Rajasthan\t\t\t\t","Gandhinagar",2],
       ["What does 'G' stand for in NGO, an example of which is the World Wildlife Fund?","Guidance\t\t\t\t","Governmental","Girl\t\t\t\t","Global",2],
       ["What is the meaning of Education Degree, Ph.D.?","Doctor of philosphy\t\t","Doctor of philospher","philosphical doctoral\t\t","Philosphy Doctoral",1],
       ["Current Railway Minister of India is?","Mamta Banerjee\t\t\t","Ashwini Vaishnaw","Ram Vilas\t\t\t\t","Piyush Goyal",2],
       ["Which god is also known as ‘Gauri Nandan’?","ganesha\t\t\t\t","hanuman","inder\t\t\t\t","agni",1],
       ["What does not grow on tree according to a popular Hindi saying?","papaya\t\t\t\t","banana","money\t\t\t\t","mango",3],
       ["How many religions are there in India?","27\t\t\t\t","7","28\t\t\t\t","6",4],
       ['How many Bits make one Byte?',"16\t\t\t\t" , '32' , '8\t\t\t\t' , '1028' , 3],
       ['Who is the founder of Facebook?','Andrew Maclin\t\t\t','Mark Adon','Mark Zuckerberg\t\t\t','None of these',3],
       ['What is the full form of VIRUS?','1.Vital Information Rest Under System\n','2.Vital Information Rest Under Siege','3.Virtual Information Resources Under Siege\n','4.Vital Information Resources Under Siege',4],
       ['Who is called the Father of the Computer?','Andrew N.\t\t\t','Dinnis Ritchie','Mark Zuckerberg\t\t\t','Charles Babbage',4],
       ['A program that translates High-Level Language to a Machine Level Language is called?','Compiler\t\t\t\t','Interpreter','Assembler\t\t\t','Operating system',1],
       ['In the binary language each letter of the alphabet, each number, and each special character is made up of a unique combination of?','32 bits\t\t\t\t','16 bits','8 bits\t\t\t\t','128 bits',3]]

        score=0
        try:
            for question in questions:
                print(question[0])
                print(f'{question[1]}{question[2]}\n{question[3]}{question[4]}')
                a = int(input())
                if a==question[5]:
                    score+=1
                    pass
                else:
                    a = 'WRONG ANSWER!'
                    print(a.center(80))
                    break
        except ValueError() :
            print("Sorry Your Game has ended due to pressing wrong key")
        a = "THANKYOU FOR PLAYING QUIZ GAME"
        b = '  You have scored '+str(score) + ' scores'
        print(a.center(80))
        print(b.center(80))


    
    elif an==2:
        print("Choose level of game:\n1.Hard\n2.Medium\n3.Easy: ")
        a= int(input("Press 1 , 2 or 3: "))
        if a==3:
            no = random.randrange(1,9)
            print("Enter a no. between 1-9")
            A=10
        elif a==2:
            no = random.randrange(1,99)
            print("Enter a no. between 1-99")
            A=16
        elif a==1:
            no = random.randrange(1,999)
            print("Enter a no. between 1-999 ")
            A=30
        else:
            print("pressed wrong key")
        if a==1 or a==2 or a==3:
            num=int(input("Your Guessed number is:"))
            while num!=no:
                if num>no:
                    print("You are high . Think Lower number!!!!")
                elif num<no:
                    print("You are low . Think High number!!!")
                num = int(input())
                A-=2
                if A<0:
                    print("Sorry! You are out of your attempts.")
                    print(f"Guessed no. is {no}")
                    break
            if num==no:
                print(f"YUPPIE! You made it!!\nYou have scored  {A} Scores")
                print("="*25+"YEAH"+"="*25)



    elif an==3:
        def pattern(xstate,ystate):
            zero= "X" if xstate[0]==1 else ("o" if ystate[0]==1 else 0)
            one= "X" if xstate[1]==1 else ("o" if ystate[1]==1 else 1)
            two= "X" if xstate[2]==1 else ("o" if ystate[2]==1 else 2)
            three= "X" if xstate[3]==1 else ("o" if ystate[3]==1 else 3)
            four= "X" if xstate[4]==1 else ("o" if ystate[4]==1 else 4)
            five= "X" if xstate[5]==1 else ("o" if ystate[5]==1 else 5)
            six= "X" if xstate[6]==1 else ("o" if ystate[6]==1 else 6)
            seven= "X" if xstate[7]==1 else ("o" if ystate[7]==1 else 7)
            eight= "X" if xstate[8]==1 else ("o" if ystate[8]==1 else 8)
            print(f" {zero} |  {one}  |  {two} ")
            print("---|---|---")
            print(f" {three} | {four} |  {five} ")
            print("---|---|---")
            print(f" {six} | {seven} |  {eight} ")

        def winner(xstate,ystate):
            wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
            for win in wins:
                if(xstate[win[0]] + xstate[win[1]] + xstate[win[2]]==3):
                    print("X wins")
                    return 1
                elif (ystate[win[0]] + ystate[win[1]] + ystate[win[2]]==3):
                    print("o wins")
                    return 0
            return 2
    
        xstate=[0,0,0,0,0,0,0,0,0]
        ystate=[0,0,0,0,0,0,0,0,0]
        print("Welcome to tic-tac-toe Game")
        turn=1
        pattern(xstate,ystate)
        while(True):
            if(turn==1):
                print("player X's turn")
                xstate[int(input())]=1
            else:
                print("player o's turn")
                ystate[int(input())]=1
            pattern(xstate,ystate)
            winn=winner(xstate,ystate)
            if(winn!=2):
                break
            turn=1-turn

def filee():
    con = 1
    while(con):
        func()
        con = int(input('Enter 0 to exit\nto continue press any key'))
user = open('username.txt','a+')
print("\t*User Authentication System*\t\n")
print(f'You want to \t Register for new users\t or \t Login for old user \n')
a=input("Press A for register and B for login \n")
def login():
    print("Login to your account\n")
    p=input("username--").strip()
    q=input("Password--").strip()
    user.seek(0)
    x = user.readlines()
    for lines in x:
        if lines==str(p+'-'+q+'\n'):
            print("\nLet's move to the Game Hub\n")
            break
    else:
        print("Wrong id password\n\n"+"="*20 +"retry"+"="*20)
        login()
if a=='A' or a=='a':
    print("Create Your Account\n")
    p=input("Username--").strip()
    q=input("Password--").strip()
    user.write(str(p+'-'+q+'\n'))
    print(f"Your id and password are generated\nusername-{p}\npassword-{q}")
    login()
    filee()
elif a=='b' or a=='B':
    login()
    filee()
else:
    print("Sorry! You can't play as pressed wrong key")


user.close()
